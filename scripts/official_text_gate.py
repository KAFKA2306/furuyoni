#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "official_sources.yaml"
MARKER = re.compile(r"<!--\s*official-source:\s*([\w-]+)#([^|\s]+)\s*\|\s*quote:\s*(.*?)\s*-->")
CARD_MARKER = re.compile(r"<!--\s*official-card:\s*([\w-]+)#([^|\s]+)\s*\|\s*quote:\s*(.*?)\s*-->")


class VisibleText(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.hidden = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self.hidden += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.hidden:
            self.hidden -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden:
            self.parts.append(data)


@dataclass(frozen=True)
class Violation:
    path: str
    line: int
    message: str
    text: str


def normalize(value: str) -> str:
    return re.sub(r"\s+", "", html.unescape(value)).replace("「", "『").replace("」", "』")


def load_manifest() -> dict[str, Any]:
    return yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))


def download_sources(manifest: dict[str, Any], offline: bool) -> dict[str, str]:
    cache = ROOT / manifest["policy"]["cache_dir"]
    cache.mkdir(parents=True, exist_ok=True)
    paths: dict[str, str] = {}
    for source_id, source in manifest["sources"].items():
        suffix = ".html" if source["format"] == "html" else ".bin"
        path = cache / f"{source_id}{suffix}"
        if not path.exists():
            if offline:
                raise RuntimeError(f"missing offline source: {source_id}")
            request = urllib.request.Request(source["url"], headers={"User-Agent": "furuyoni-official-text-gate/1"})
            with urllib.request.urlopen(request, timeout=30) as response:
                path.write_bytes(response.read())
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != source["sha256"]:
            raise RuntimeError(f"official source changed: {source_id}: expected {source['sha256']}, got {actual}")
        paths[source_id] = str(path)
    return paths


def source_text(source: dict[str, Any], path: str) -> str:
    raw = Path(path).read_bytes()
    if source["format"] == "binary":
        return ""
    if source["format"] == "html":
        parser = VisibleText()
        parser.feed(raw.decode("utf-8", errors="replace"))
        return normalize("\n".join(parser.parts))
    if source["format"] == "pdf_ocr":
        return ocr_pdf(path, source)
    if not shutil.which("pdftotext"):
        raise RuntimeError("pdftotext is required for PDF sources")
    result = subprocess.run(["pdftotext", "-layout", path, "-"], check=True, capture_output=True, text=True)
    return normalize(result.stdout)


def ocr_pdf(path: str, source: dict[str, Any]) -> str:
    cache = ROOT / ".cache" / "official-sources"
    output = cache / "cardlist.ocr.txt"
    if output.exists():
        return normalize(output.read_text(encoding="utf-8"))
    if not shutil.which("pdftoppm") or not shutil.which("tesseract"):
        raise RuntimeError("pdftoppm and tesseract are required for official card text OCR")
    prefix = cache / "cardlist-page"
    subprocess.run(["pdftoppm", "-r", "200", "-png", path, str(prefix)], check=True, capture_output=True)
    pages = sorted(cache.glob("cardlist-page-*.png"))
    if not pages:
        raise RuntimeError("official card list OCR produced no pages")
    texts: list[str] = []
    for page in pages:
        result = subprocess.run(["tesseract", str(page), "stdout", "-l", "jpn+eng", "--psm", "6"], check=True, capture_output=True, text=True)
        texts.append(result.stdout)
    output.write_text("\n".join(texts), encoding="utf-8")
    return normalize("\n".join(texts))


def target_files(policy: dict[str, Any]) -> list[Path]:
    extensions = set(policy["extensions"])
    files: list[Path] = []
    for directory in policy["target_dirs"]:
        root = ROOT / directory
        if root.exists():
            files.extend(path for path in root.rglob("*") if path.is_file() and path.suffix in extensions)
    return sorted(files)


def is_claim(line: str, terms: list[str], patterns: list[str]) -> bool:
    if not line.strip() or line.lstrip().startswith("<!--"):
        return False
    if re.fullmatch(r"\s*[#|`>\-*_:.()\[\]、。]+\s*", line):
        return False
    if not any(term in line for term in terms):
        return False
    return any(re.search(pattern, line) for pattern in patterns)


def validate_marker(marker: re.Match[str], source_texts: dict[str, str], manifest: dict[str, Any]) -> str | None:
    source_id, ref, quote = marker.group(1), marker.group(2), marker.group(3)
    if source_id not in manifest["sources"]:
        return f"unknown official source: {source_id}"
    source = manifest["sources"][source_id]
    if source["format"] == "binary":
        return f"binary source cannot verify text quote: {source_id}"
    if not any(ref.startswith(prefix) for prefix in source.get("refs", [])):
        return f"unknown source reference: {source_id}#{ref}"
    if normalize(quote) not in source_texts[source_id]:
        return f"quote not found in {source_id}#{ref}: {quote}"
    return None


def validate_card_marker(marker: re.Match[str], source_texts: dict[str, str], manifest: dict[str, Any]) -> str | None:
    source_id, ref, quote = marker.group(1), marker.group(2), marker.group(3)
    if source_id not in manifest["sources"]:
        return f"unknown official card source: {source_id}"
    source = manifest["sources"][source_id]
    if source["format"] != "pdf_ocr":
        return f"card source is not OCR-enabled: {source_id}"
    if not ref:
        return f"missing card reference: {source_id}"
    if normalize(quote) not in source_texts[source_id]:
        return f"card quote not found in {source_id}#{ref}: {quote}"
    return None


def audit_file(path: Path, policy: dict[str, Any], source_texts: dict[str, str], manifest: dict[str, Any]) -> list[Violation]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    violations: list[Violation] = []
    display_path = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
    pending: list[re.Match[str]] = []
    fenced = False
    for number, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            fenced = not fenced
            continue
        markers = list(MARKER.finditer(line))
        pending.extend(markers)
        if not line.strip():
            pending = []
            continue
        if fenced or not is_claim(line, policy["rule_terms"], policy["claim_patterns"]):
            continue
        if not pending:
            violations.append(Violation(display_path, number, "rule-bearing text has no official quote", line.strip()))
            continue
        for marker in pending:
            error = validate_marker(marker, source_texts, manifest)
            if error:
                violations.append(Violation(display_path, number, error, line.strip()))
        pending = []
    return violations


def card_anchor(line: str) -> str | None:
    match = re.search(r"cards\.md#([^)\]]+)", line)
    return match.group(1) if match else None


def is_card_claim(line: str, patterns: list[str]) -> bool:
    if not line.strip() or line.lstrip().startswith("<!--"):
        return False
    if re.fullmatch(r"\s*[#|`>\-*_:.()\[\]、。]+\s*", line):
        return False
    return any(re.search(pattern, line) for pattern in patterns)


def audit_card_file(path: Path, policy: dict[str, Any], source_texts: dict[str, str], manifest: dict[str, Any]) -> list[Violation]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    violations: list[Violation] = []
    display_path = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
    current_card: str | None = None
    pending: list[re.Match[str]] = []
    for number, line in enumerate(lines, 1):
        heading = re.match(r"^#{1,6}\s+", line)
        if heading:
            current_card = card_anchor(line)
        row_card = card_anchor(line)
        if row_card:
            current_card = row_card
        markers = list(CARD_MARKER.finditer(line))
        pending.extend(markers)
        if not line.strip():
            pending = []
            continue
        if not current_card or not is_card_claim(line, policy["card_claim_patterns"]):
            continue
        if not pending:
            violations.append(Violation(display_path, number, f"card effect text has no official quote: {current_card}", line.strip()))
            continue
        for marker in pending:
            error = validate_card_marker(marker, source_texts, manifest)
            if error:
                violations.append(Violation(display_path, number, error, line.strip()))
        pending = []
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description="Fail-closed official Furuyoni text provenance gate")
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    manifest = load_manifest()
    paths = download_sources(manifest, args.offline)
    source_texts = {source_id: source_text(manifest["sources"][source_id], path) for source_id, path in paths.items()}
    violations = []
    for path in target_files(manifest["policy"]):
        violations.extend(audit_file(path, manifest["policy"], source_texts, manifest))
        if path.parent.name == "megami" and path.name != "cards.md":
            violations.extend(audit_card_file(path, manifest["policy"], source_texts, manifest))
    report = {
        "status": "BLOCKED" if violations else "VERIFIED",
        "sources": {source_id: manifest["sources"][source_id]["sha256"] for source_id in paths},
        "violations": [violation.__dict__ for violation in violations],
    }
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "violations": len(violations), "sources": report["sources"]}, ensure_ascii=False))
    for violation in violations[:40]:
        print(f"{violation.path}:{violation.line}: {violation.message}: {violation.text}", file=sys.stderr)
    if len(violations) > 40:
        print(f"... {len(violations) - 40} more violations; use --json for the full report", file=sys.stderr)
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
