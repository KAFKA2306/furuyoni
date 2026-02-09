import argparse
import json
import os
import re
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Optional

PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
SRC_DIR: Path = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from furuyoni.infrastructure.paths import DOCS_DIR, PROJECT_ROOT as DATA_PROJECT_ROOT
from furuyoni.domain.validator import LinkValidator

def load_config(config_path: str) -> Dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def check_links() -> None:
    validator: LinkValidator = LinkValidator()
    file_link_map: Dict[str, List[str]] = {}
    all_links: set[str] = set()

    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path: Path = Path(root) / file
                with open(file_path, "r", encoding="utf-8") as f:
                    content: str = f.read()
                links: List[str] = validator.extract_links(content)
                if links:
                    rel_path: str = os.path.relpath(file_path, DATA_PROJECT_ROOT)
                    file_link_map[rel_path] = links
                    for link in links:
                        all_links.add(link)

    print(f"Found {len(all_links)} unique links in {len(file_link_map)} files.")

    results: Dict[str, tuple[str, str]] = validator.validate_batch(list(all_links))

    broken_found: bool = False
    print("\n--- LINK CHECK REPORT ---\n")
    for file, links in file_link_map.items():
        file_broken: List[tuple[str, str, str]] = []
        for link in set(links):
            status, msg = results[link]
            if msg != "OK":
                file_broken.append((link, status, msg))
        
        if file_broken:
            broken_found = True
            print(f"File: {file}")
            for link, status, msg in file_broken:
                print(f"  - {link} : [{status}] {msg}")
            print("")

    if not broken_found:
        print("All weblinks are valid!")

def get_relative_link(source_file: Path, target_file_key: str, docs_dir: Path) -> str:
    source_dir: Path = source_file.parent
    target_abs: Path = docs_dir / target_file_key
    return os.path.relpath(target_abs, source_dir)

def process_file_links(file_path: Path, term_mapping: Dict[str, str], docs_dir: Path) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        content: str = f.read()

    sorted_terms: List[str] = sorted(term_mapping.keys(), key=len, reverse=True)
    
    p_link: str = r'\[.*?\]\(.*?\)'
    p_image: str = r'!\[.*?\]\(.*?\)'
    p_code_inline: str = r'`[^`\n]+`'
    p_code_block: str = r'```[\s\S]*?```'
    p_html: str = r'<[^>]+>'
    p_header: str = r'^#{1,6}\s.*$'
    
    protected_pattern: str = f"({p_code_block}|{p_link}|{p_image}|{p_code_inline}|{p_html}|{p_header})"
    terms_pattern: str = "(" + "|".join(re.escape(t) for t in sorted_terms) + ")"
    pattern: re.Pattern = re.compile(f"{protected_pattern}|{terms_pattern}", re.MULTILINE)

    def replace_func(match: re.Match) -> str:
        g1: Optional[str] = match.group(1)
        g2: Optional[str] = match.group(2)
        
        if g1: return g1
        
        if g2:
            term: str = g2
            target_file_key: str = term_mapping[term]
            rel_source: str = os.path.relpath(file_path, docs_dir)
            if rel_source == target_file_key:
                return term
            link_url: str = get_relative_link(file_path, target_file_key, docs_dir)
            return f"[{term}]({link_url})"
        return str(match.group(0))

    new_content: str = pattern.sub(replace_func, content)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated links in: {file_path}")

def add_links(config_path: str) -> None:
    config: Dict = load_config(config_path)
    docs_dir: Path = PROJECT_ROOT / config["paths"]["docs_dir"]
    term_mapping: Dict[str, str] = config["term_mapping"]

    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                process_file_links(Path(root) / file, term_mapping, docs_dir)

def sync_cards(config_path: str) -> None:
    config: Dict = load_config(config_path)
    data_js_path: str = str(PROJECT_ROOT / config["paths"]["data_js"])
    base_url: str = config["urls"]["base_card_url"]
    output_path: str = str(PROJECT_ROOT / config["paths"]["output_cards"])

    with open(data_js_path, "r", encoding="utf-8") as f:
        content: str = f.read()

    start_idx: int = content.find("export const cards = {") + len("export const cards = {")
    end_idx: int = content.find("};", start_idx)
    cards_str: str = "{" + content[start_idx:end_idx].strip() + "}"
    cards_str = cards_str.replace("'", '"')
    cards_str = re.sub(r",\s*([}\]])", r"\1", cards_str)
    
    cards_data: Dict[str, List[str]] = json.loads(cards_str)

    output: str = "# メガミカードギャラリー\n\n各メガミの通常札一覧です。画像をクリックすると拡大表示されます。\n\n"

    for megami, card_paths in cards_data.items():
        output += f"## {megami}\n\n"
        output += '<div class="grid cards" markdown>\n\n'
        for path in card_paths:
            full_url: str = f"{base_url}{path}"
            output += f'-   [:external-link: ![{megami} Card]({full_url})]({full_url}){{ .glightbox }}\n\n'
        output += "</div>\n\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Updated card gallery: {output_path}")

def verify_nav(config_path: str) -> None:
    from playwright.sync_api import sync_playwright
    config: Dict = load_config(config_path)
    test_url: str = config["urls"]["test_server_url"]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 600})
        
        page.on("console", lambda msg: print(f"Browser Console: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Page Error: {err}"))
        
        page.goto(test_url)
        print("Checking initial state...")
        
        if page.locator("#pair-view").is_visible():
            print("Initial view (Pair Guide) is visible.")
        else:
            print("Error: #pair-view not visible initially.")
            sys.exit(1)

        print("Navigation verification successful (basic check).")
        browser.close()

def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Furuyoni Project Maintenance Tool")
    subparsers: argparse._SubParsersAction = parser.add_subparsers(dest="command", help="Command to run")

    subparsers.add_parser("check-links", help="Validate links in documentation")
    subparsers.add_parser("add-links", help="Automatically add internal links")
    subparsers.add_parser("sync-cards", help="Update the card gallery from data.js")
    subparsers.add_parser("verify-nav", help="Verify site navigation using Playwright")

    args: argparse.Namespace = parser.parse_args()

    if args.command == "check-links":
        check_links()
    elif args.command == "add-links":
        add_links("config.yaml")
    elif args.command == "sync-cards":
        sync_cards("config.yaml")
    elif args.command == "verify-nav":
        verify_nav("config.yaml")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
