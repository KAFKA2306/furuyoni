import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Optional

def load_config(config_path: str) -> Dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_relative_link(source_file: Path, target_file_key: str, docs_dir: Path) -> str:
    source_dir: Path = source_file.parent
    target_abs: Path = docs_dir / target_file_key
    return os.path.relpath(target_abs, source_dir)

def process_file(file_path: Path, term_mapping: Dict[str, str], docs_dir: Path) -> None:
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
        
        if g1:
            return g1
        
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

def main() -> None:
    config: Dict = load_config("config.yaml")
    docs_dir: Path = Path(config["paths"]["docs_dir"])
    term_mapping: Dict[str, str] = config["term_mapping"]

    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                process_file(Path(root) / file, term_mapping, docs_dir)

if __name__ == "__main__":
    main()
