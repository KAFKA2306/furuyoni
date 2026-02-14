import argparse
import json
import os
import re
import sys
import yaml
import urllib.request
from pathlib import Path
from typing import Dict, List, Tuple

# noqa: E402
# Adjust path to import src modules if needed, though we are removing unused ones.
PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from furuyoni.infrastructure.paths import DOCS_DIR, PROJECT_ROOT as DATA_PROJECT_ROOT  # noqa: E402
from furuyoni.domain.validator import LinkValidator  # noqa: E402


def load_config(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# --- Anchor Management ---
def add_anchors(card_file: Path = DOCS_DIR / "megami/cards.md") -> None:
    """Adds HTML anchors to card entries in cards.md."""
    if not card_file.exists():
        print(f"Error: {card_file} not found.")
        sys.exit(1)

    with open(card_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    updated = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Heuristic: Card name line usually follows an image line
        if i > 0:
            prev_line = lines[i - 1].strip()
            # Image line detection: start with - and contains image tag
            if prev_line.startswith("- ") and "[:external-link:" in prev_line:
                # Current line is the card name line if it's indented and text
                if (
                    line.startswith("    ")
                    and not stripped.startswith("-")
                    and stripped
                ):
                    # Check if already has anchor
                    if "{: #" in stripped:
                        new_lines.append(line)
                        continue

                    base_text = stripped.split("{")[0].strip()
                    # Create anchor
                    new_line = f"    {base_text} {{: #{base_text} }}\n"
                    new_lines.append(new_line)
                    updated = True
                    continue
        new_lines.append(line)

    if updated:
        with open(card_file, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"Updated {card_file} with anchors.")
    else:
        print("No new anchors needed.")


# --- Link Management ---
def extract_card_mapping() -> Dict[str, str]:
    """Extract Card Name -> Image URL mapping from cards.md"""
    mapping = {}
    card_file = DOCS_DIR / "megami/cards.md"
    if not card_file.exists():
        return mapping

    with open(card_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern: <span id="CardName"></span>[:external-link: ![MegamiName](ImageURL)](ImageURL)
    # Also support markdown attribute style: CardName {: #CardName }
    # But for linking purposes, we want the Image URL or just the link.
    # Actually, universal_linker used the Image URL to create an image link.
    # Let's verify the pattern from universal_linker.py
    pattern = re.compile(
        r'<span id="([^"]+)"></span>\[:external-link: !\[[^\]]+\]\(([^)]+)\)\]\(([^)]+)\)'
    )
    for match in pattern.finditer(content):
        name = match.group(1)
        url = match.group(2)
        mapping[name] = url
    return mapping


def extract_megami_mapping() -> Dict[str, str]:
    """Extract Megami Name -> File mapping from index.md"""
    mapping = {}
    index_file = DOCS_DIR / "megami/index.md"
    if not index_file.exists():
        return mapping

    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")
    for match in pattern.finditer(content):
        name = match.group(1)
        file_path = match.group(2)
        if re.match(r"^(0[1-9]|1[0-6]|index|cards)", file_path):
            mapping[name] = f"megami/{file_path}"
    return mapping


def add_links(config_path: str) -> None:
    cfg: Dict = load_config(config_path)
    static_mapping: Dict[str, str] = cfg.get("term_mapping", {})

    # Dynamic mappings
    card_map = extract_card_mapping()
    megami_map = extract_megami_mapping()

    # Merge mappings: Dynamic > Static (or separate handling)
    # We'll treat them separately to apply different link formats if needed

    all_terms = sorted(
        list(static_mapping.keys()) + list(card_map.keys()) + list(megami_map.keys()),
        key=len,
        reverse=True,
    )

    # Skip pattern: don't link inside existing links, images, code blocks, or HTML tags
    skip_pattern = re.compile(
        r"(```[\s\S]*?```|\[[^\]]*?\]\([^\)]*?\)|!\[.*?\]\(.*?\)|`[^`\n]+`|<[^>]+>)"
    )

    term_regex = "|".join(re.escape(t) for t in all_terms)
    if not term_regex:
        print("No terms to link.")
        return

    # Master pattern: Skip | Term
    master_pattern = re.compile(
        f"({skip_pattern.pattern})|({term_regex})", re.MULTILINE
    )

    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if not file.endswith(".md"):
                continue
            p = Path(root) / file

            with open(p, "r", encoding="utf-8") as f:
                content = f.read()

            def replace_func(match: re.Match) -> str:
                # Group 1 is skip pattern
                if match.group(1):
                    # Check if it's a link we should update [Term](Url)
                    link_match = re.match(r"^\[([^\]]+)\]\([^\)]+\)$", match.group(1))
                    if link_match:
                        term = link_match.group(1)
                        if term in card_map or term in megami_map or term in static_mapping:
                            # Fall through to re-generate link
                            pass
                        else:
                            return match.group(1)
                    else:
                        return match.group(1)
                else:
                    term = match.group(0)

                if skip_pattern.match(term) and not (match.group(1) and link_match):
                    # Double check if term matches skip pattern (should have been caught by group 1 check?)
                    # If we fell through from group 1, we don't want to return here.
                    return term

                # It's a term
                if term in card_map:
                    url = card_map[term]
                    return f"[![{term}]({url})]({url}){{ .glightbox }}"

                target = None
                if term in megami_map:
                    target = megami_map[term]
                elif term in static_mapping:
                    target = static_mapping[term]

                if target:
                    # If target is the file itself, don't link (or specific check)
                    # Simple check: if abspath(target) == abspath(p)
                    # But target is relative to docs_dir usually
                    # Construct absolute target path

                    # Target might be "megami/index.md" or "mechanics/glossary.md#aura"
                    target_file = target
                    anchor_part = ""
                    if "#" in target:
                        parts = target.rsplit("#", 1)
                        target_file = parts[0]
                        anchor_part = "#" + parts[1]

                    target_abs = DOCS_DIR / target_file
                    if target_abs.resolve() == p.resolve():
                        if anchor_part:
                            return f"[{term}]({anchor_part})"
                        return term  # Don't link to self if no anchor

                    rel_path = os.path.relpath(DOCS_DIR / target_file, p.parent)
                    return f"[{term}]({rel_path}{anchor_part})"

                return term

            new_content = master_pattern.sub(replace_func, content)

            if new_content != content:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(new_content)
                # print(f"Linked {p.name}")


# --- Asset Management ---
def download_assets() -> None:
    dest: Path = DOCS_DIR / "assets/images"
    dest.mkdir(parents=True, exist_ok=True)
    pat: str = (
        r"https://main-bakafire\.ssl-lolipop\.jp/furuyoni/na/images/([^\s\)\"\']+)"
    )
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                p: Path = Path(root) / file
                with open(p, "r", encoding="utf-8") as f:
                    content: str = f.read()
                ms: List[str] = list(set(re.findall(pat, content)))
                if not ms:
                    continue
                for m in ms:
                    lp: Path = dest / m
                    lp.parent.mkdir(parents=True, exist_ok=True)
                    # Zero-Fat: No "if not exists" check, always overwrite/ensure
                    # Actually for assets, "if not exists" saves bandwidth.
                    # But prompt said "redundant logic... unused code... redundant checks".
                    # Checking existence is NOT redundancy if it prevents network call.
                    # HOWEVER, "Fail Fast" implies if I want to download, I download.
                    # I will keep the check purely for speed but the plan said "Remove if not lp.exists()".
                    # I will follow strictly: ALWAYS DOWNLOAD. Be careful not to DDoS.
                    # Wait, the plan said "Remove time.sleep". It also said "Remove if not lp.exists()".
                    # I will follow the plan.
                    req = urllib.request.Request(
                        f"https://main-bakafire.ssl-lolipop.jp/furuyoni/na/images/{m}",
                        headers={"User-Agent": "Mozilla/5.0"},
                    )
                    with urllib.request.urlopen(req) as r:
                        with open(lp, "wb") as o:
                            o.write(r.read())

                rel: str = os.path.relpath(dest, p.parent)
                new: str = re.sub(pat, lambda x: f"{rel}/{x.group(1)}", content)
                with open(p, "w", encoding="utf-8") as f:
                    f.write(new)


# --- Cards Sync ---
    return card_map


    return card_map


def build_card_map(doc_root: Path) -> Dict[str, str]:
    """
    Scans megami docs to map image filenames to card names.
    Strategy:
    1. Identify valid card names from headers (e.g. '### N1 Slash').
    2. Map image filenames to these names if the image's Alt Text matches.
    This prevents mapping generic terms like "Role" or "Cost" to card images.
    """
    card_map = {}
    
    # Pattern for Headers: ### N1 Name or ### S1 Name
    # We catch the name part.
    header_pat = re.compile(r"^#{3}\s+[NS]\d+\s+(.+)$", re.MULTILINE)
    
    # Pattern for Images: ![Alt](Filename)
    # We capture Alt and Filename.
    img_pat = re.compile(r"!\[([^\]]*)\]\((?:[^)]*/)?([^/]+\.png)(?:\s.*?)?\)")

    for root, _, files in os.walk(doc_root / "megami"):
        for file in files:
            if file.endswith(".md") and file != "cards.md" and file != "index.md":
                p = Path(root) / file
                with open(p, "r", encoding="utf-8") as f:
                    content = f.read()

                # 1. Extract valid names from headers
                valid_names = set()
                for m in header_pat.finditer(content):
                    raw_name = m.group(1).strip()
                    # Clean up: remove reading in parens, e.g. "Name (Reading)" -> "Name"
                    clean = re.split(r"[（(]", raw_name)[0].strip()
                    
                    # Remove markdown images/links: [![Alt](Url)] -> Alt, [Text](Url) -> Text
                    # Regex to replace ![Alt](Url) with Alt
                    clean = re.sub(r"!\[([^\]]*)\]\(.*?\)", r"\1", clean)
                    # Regex to replace [Text](Url) with Text
                    clean = re.sub(r"\[([^\]]+)\]\(.*?\)", r"\1", clean)
                    
                    clean = clean.strip()
                    
                    if clean:
                        valid_names.add(clean)

                # 2. Extract images and check against valid names
                for m in img_pat.finditer(content):
                    alt_text = m.group(1).strip()
                    filename = m.group(2).strip()

                    # Direct match
                    if alt_text in valid_names:
                        card_map[filename] = alt_text
                        continue
                    
                    # Fallback: if alt text is part of a valid name or vice versa?
                    # Be conservative. If alt text is "Slash", and header is "Slash", good.
                    # If alt text is "Role", and no header "Role", we skip.
                    
                    # Special case: sometimes alt text is full name but header has extra info?
                    # We already cleaned header.
                    pass

    return card_map


def sync_cards(config_path: str) -> None:
    cfg: Dict = load_config(config_path)
    card_map = build_card_map(DOCS_DIR)

    with open(PROJECT_ROOT / cfg["paths"]["data_js"], "r", encoding="utf-8") as f:
        c: str = f.read()
    s_idx: int = c.find("export const cards = {") + len("export const cards = ")
    e_idx: int = c.find("};", s_idx) + 1
    raw: str = c[s_idx:e_idx].strip().replace("'", '"')
    data: Dict[str, List[str]] = json.loads(re.sub(r",\s*([}\]])", r"\1", raw))

    out: str = "# 全カード一覧\n\n"
    for m, ps in data.items():
        out += f'## {m}\n\n<div class="grid cards" markdown>\n\n'
        for p in ps:
            url: str = f"{cfg['urls']['base_card_url']}{p}"
            filename = p.split("/")[-1]
            anchor = ""
            if filename in card_map:
                clean_name = re.sub(r"\[([^\]]+)\]\(.*?\)", r"\1", card_map[filename])
                anchor = f' id="{clean_name}"'

            if anchor:
                out += f"-   <span{anchor}></span>[:external-link: ![{m}]({url})]({url}){{ .glightbox }}\n\n"
            else:
                out += f"-   [:external-link: ![{m}]({url})]({url}){{ .glightbox }}\n\n"
        out += "</div>\n\n"

    with open(PROJECT_ROOT / cfg["paths"]["output_cards"], "w", encoding="utf-8") as f:
        f.write(out)


# --- Audit ---
def check_headings(file_path: Path) -> List[str]:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    headings = re.findall(r"^(#+)\s+(.*)", content, re.MULTILINE)
    errors = []
    if not headings:
        errors.append("No headings found")
        return errors
    h1_count = sum(1 for level, title in headings if len(level) == 1)
    if h1_count != 1:
        errors.append(f"Expected 1 H1, found {h1_count}")
    prev_level = 0
    for level_str, title in headings:
        level = len(level_str)
        if level > prev_level + 1:
            errors.append(
                f"Header level skipped: H{prev_level} -> H{level} ('{title}')"
            )
        prev_level = level
    return errors


def audit_nav() -> List[str]:
    """Checks for files not in mkdocs.yml nav."""
    mkdocs_path = PROJECT_ROOT / "mkdocs.yml"
    if not mkdocs_path.exists():
        return ["mkdocs.yml not found"]

    with open(mkdocs_path, "r") as f:
        # Handle custom usage of !!python/name in mkdocs.yml
        class CustomLoader(yaml.SafeLoader):
            pass

        CustomLoader.add_multi_constructor(
            "tag:yaml.org,2002:python/name",
            lambda loader, suffix, node: str(node.value),
        )
        config = yaml.load(f, Loader=CustomLoader)

    # helper to extract paths from nav
    nav_paths = set()

    def extract_paths(nav):
        for item in nav:
            if isinstance(item, str):
                # Should not happen in pure nav list, usually dict or str
                pass
            if isinstance(item, dict):
                for k, v in item.items():
                    if isinstance(v, str):
                        nav_paths.add(v)
                    elif isinstance(v, list):
                        extract_paths(v)

    if "nav" in config:
        extract_paths(config["nav"])

    orphans = []
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                rel = str(Path(root).relative_to(DOCS_DIR) / file)
                if rel not in nav_paths:
                    orphans.append(rel)
    return orphans


def audit() -> None:
    print("--- Starting Audit ---")
    validator: LinkValidator = LinkValidator()
    file_map: Dict[str, List[str]] = {}
    links: set[str] = set()

    # 1. Collect Links & Check Headings
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                p: Path = Path(root) / file
                # Headings
                h_errors = check_headings(p)
                if h_errors:
                    print(f"Heading Error in {p.relative_to(DATA_PROJECT_ROOT)}:")
                    for err in h_errors:
                        print(f"  {err}")
                    sys.exit(1)  # Fail Fast!

                # Links
                with open(p, "r", encoding="utf-8") as f:
                    content: str = f.read()
                ls: List[str] = validator.extract_links(content)
                if ls:
                    file_map[str(p.relative_to(DATA_PROJECT_ROOT))] = ls
                    links.update(ls)

    # 2. Validate Links
    # validator.validate_batch actually runs requests.
    print(f"Validating {len(links)} unique links...")
    results: Dict[str, Tuple[str, str]] = validator.validate_batch(list(links))
    has_broken: bool = False
    for f, ls in file_map.items():
        for link_url in ls:
            status_msg = results[link_url][1]
            if status_msg == "OK":
                continue
            if status_msg in ("TIMEOUT", "CONNECTION_ERROR"):
                print(f"  WARN: {status_msg} for {link_url} in {f}")
                continue
            print(f"Broken link in {f}: {link_url} ({status_msg})")
            has_broken = True
    if has_broken:
        sys.exit(1)  # Fail Fast

    # 3. Nav Audit
    nav_orphans = audit_nav()
    if nav_orphans:
        print("Orphaned files (not in nav):")
        for o in nav_orphans:
            print(f"  - {o}")
        sys.exit(1)  # Fail Fast

    print("Audit Passed.")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("check-links")
    sub.add_parser("add-links")
    sub.add_parser("sync-cards")
    sub.add_parser("download-assets")
    sub.add_parser("audit")
    sub.add_parser("add-anchors")

    args = parser.parse_args()
    if args.cmd == "check-links":
        # Simplified check-links just runs part of audit?
        # For Zero-Fat, we should remove redundant commands if 'audit' covers them.
        # But maybe users want just links?
        # I'll implement it as just calling audit() or specific logic.
        # Since audit() is "Fail Fast" and comprehensive, let's just use audit().
        audit()
    elif args.cmd == "add-links":
        add_links("config.yaml")
    elif args.cmd == "sync-cards":
        sync_cards("config.yaml")
    elif args.cmd == "download-assets":
        download_assets()
    elif args.cmd == "add-anchors":
        add_anchors()
    elif args.cmd == "audit":
        audit()


if __name__ == "__main__":
    main()
