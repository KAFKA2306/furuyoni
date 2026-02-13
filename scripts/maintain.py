import argparse
import json
import os
import re
import sys
import yaml
import urllib.request
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor
PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
SRC_DIR: Path = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))
from furuyoni.infrastructure.paths import DOCS_DIR, PROJECT_ROOT as DATA_PROJECT_ROOT
from furuyoni.domain.validator import LinkValidator
def load_config(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
def check_links() -> None:
    validator: LinkValidator = LinkValidator()
    file_map: Dict[str, List[str]] = {}
    links: set[str] = set()
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                p: Path = Path(root) / file
                with open(p, "r", encoding="utf-8") as f:
                    content: str = f.read()
                ls: List[str] = validator.extract_links(content)
                if ls:
                    file_map[str(p.relative_to(DATA_PROJECT_ROOT))] = ls
                    links.update(ls)
    results: Dict[str, Tuple[str, str]] = validator.validate_batch(list(links))
    has_error = False
    for f, ls in file_map.items():
        broken = [l for l in set(ls) if results[l][1] != "OK"]
        if broken:
            has_error = True
            print(f"File: {f}")
            for l in broken:
                print(f"  - {l} : {results[l]}")
    if has_error:
        sys.exit(1)
def add_links(config_path: str) -> None:
    cfg: Dict = load_config(config_path)
    mapping: Dict[str, str] = cfg["term_mapping"]
    terms: List[str] = sorted(mapping.keys(), key=len, reverse=True)
    p_prot: str = r"(```[\s\S]*?```|\[.*?\]\(.*?\)|!\[.*?\]\(.*?\)|`[^`\n]+`|<[^>]+>|^)"
    p_terms: str = "(" + "|".join(re.escape(t) for t in terms) + ")"
    pat: re.Pattern = re.compile(f"{p_prot}|{p_terms}", re.MULTILINE)
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                p: Path = Path(root) / file
                with open(p, "r", encoding="utf-8") as f:
                    content: str = f.read()
                def rep(m: re.Match) -> str:
                    if m.group(1): return m.group(1)
                    t: str = m.group(2)
                    target: str = mapping[t]
                    if str(p.relative_to(DOCS_DIR)) == target: return t
                    rel: str = os.path.relpath(DOCS_DIR / target, p.parent)
                    return f"[{t}]({rel})"
                new: str = pat.sub(rep, content)
                if new != content:
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(new)
def build_card_map() -> Dict[str, str]:
    """Scans megami docs to map image filenames to card names."""
    card_map = {}
    # Pattern to match: Image link followed by "CardName:"
    # We look for the image filename and the text immediately following definition list style or just text
    # Example:
    # -   [![...](path/to/file.png)](...)
    #     CardName: Description
    pat = re.compile(r"images/card/cards/[^/]+/([^/]+\.png).*?\n\s+([^:<\n]+)[:]", re.MULTILINE)
    
    for root, _, files in os.walk(DOCS_DIR / "megami"):
        for file in files:
            if file.endswith(".md") and file != "cards.md" and file != "index.md":
                with open(Path(root) / file, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Find all matches
                    for m in pat.finditer(content):
                        filename = m.group(1)
                        card_name = m.group(2).strip()
                        # Clean up card name (remove MD syntax if any)
                        card_name = card_name.replace("*", "").replace("`", "")
                        card_map[filename] = card_name
    print(f"Mapped {len(card_map)} cards.")
    return card_map

def sync_cards(config_path: str) -> None:
    cfg: Dict = load_config(config_path)
    card_map = build_card_map()
    
    with open(PROJECT_ROOT / cfg["paths"]["data_js"], "r", encoding="utf-8") as f:
        c: str = f.read()
    s_idx: int = c.find("export const cards = {") + len("export const cards = ")
    e_idx: int = c.find("};", s_idx) + 1
    raw: str = c[s_idx:e_idx].strip().replace("'", '"')
    data: Dict[str, List[str]] = json.loads(re.sub(r",\s*([}\]])", r"\1", raw))
    
    out: str = ""
    for m, ps in data.items():
        out += f"### {m}\n\n<div class=\"grid cards\" markdown>\n\n"
        for p in ps:
            url: str = f"{cfg['urls']['base_card_url']}{p}"
            filename = p.split("/")[-1]
            anchor = ""
            if filename in card_map:
                anchor = f" id=\"{card_map[filename]}\""
            
            # Add span with ID for anchor before the image
            # We put it inside the list item
            if anchor:
                out += f"-   <span{anchor}></span>[:external-link: ![{m}]({url})]({url}){{ .glightbox }}\n\n"
            else:
                out += f"-   [:external-link: ![{m}]({url})]({url}){{ .glightbox }}\n\n"
        out += "</div>\n\n"
    
    with open(PROJECT_ROOT / cfg["paths"]["output_cards"], "w", encoding="utf-8") as f:
        f.write(out)
def download_assets() -> None:
    dest: Path = DOCS_DIR / "assets/images"
    dest.mkdir(parents=True, exist_ok=True)
    pat: str = r"https://main-bakafire\.ssl-lolipop\.jp/furuyoni/na/images/([^\s\)\"\']+)"
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                p: Path = Path(root) / file
                with open(p, "r", encoding="utf-8") as f:
                    content: str = f.read()
                ms: List[str] = list(set(re.findall(pat, content)))
                if not ms: continue
                for m in ms:
                    lp: Path = dest / m
                    lp.parent.mkdir(parents=True, exist_ok=True)
                    if not lp.exists():
                        req = urllib.request.Request(f"https://main-bakafire.ssl-lolipop.jp/furuyoni/na/images/{m}", headers={"User-Agent": "Mozilla/5.0"})
                        with urllib.request.urlopen(req) as r:
                            with open(lp, "wb") as o: o.write(r.read())
                        time.sleep(0.1)
                rel: str = os.path.relpath(dest, p.parent)
                new: str = re.sub(pat, lambda x: f"{rel}/{x.group(1)}", content)
                with open(p, "w", encoding="utf-8") as f: f.write(new)
def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("check-links")
    sub.add_parser("add-links")
    sub.add_parser("sync-cards")
    sub.add_parser("download-assets")
    args = parser.parse_args()
    if args.cmd == "check-links": check_links()
    elif args.cmd == "add-links": add_links("config.yaml")
    elif args.cmd == "sync-cards": sync_cards("config.yaml")
    elif args.cmd == "download-assets": download_assets()
if __name__ == "__main__":
    main()
