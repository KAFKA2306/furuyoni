import os
import re
from pathlib import Path

# Mapping of terms to their relative path from 'docs/'
# Note: Anchors are omitted for robustness, but can be added if we are sure about slugs.
TERM_MAPPING = {
    # Megami names -> megami/index.md
    "ユリナ": "megami/index.md",
    "サイネ": "megami/index.md",
    "ヒミカ": "megami/index.md",
    "トコヨ": "megami/index.md",
    "オボロ": "megami/index.md",
    "ユキヒ": "megami/index.md",
    "シンラ": "megami/index.md",
    "ハガネ": "megami/index.md",
    "チカゲ": "megami/index.md",
    "クルル": "megami/index.md",
    "サリヤ": "megami/index.md",
    "ライラ": "megami/index.md",
    "ウツロ": "megami/index.md",
    "ホノカ": "megami/index.md",
    "コルヌ": "megami/index.md",
    "ヤツハ": "megami/index.md",

    # Resources -> mechanics/index.md
    "桜花結晶": "mechanics/index.md",
    "ライフ": "mechanics/index.md",
    "オーラ": "mechanics/index.md",
    "フレア": "mechanics/index.md",
    "間合": "mechanics/index.md",
    "ダスト": "mechanics/index.md",
    "集中力": "mechanics/index.md",
    
    # Card Types -> mechanics/index.md
    "通常札": "mechanics/index.md",
    "切札": "mechanics/index.md",
    "終焉影": "mechanics/index.md",

    # Basic Actions -> mechanics/index.md
    "前進": "mechanics/index.md",
    "後退": "mechanics/index.md",
    "纏い": "mechanics/index.md",
    "宿し": "mechanics/index.md",

    # Phases & Flow -> mechanics/flow.md
    "開始フェイズ": "mechanics/flow.md",
    "メインフェイズ": "mechanics/flow.md",
    "終了フェイズ": "mechanics/flow.md",
    "再構成": "mechanics/flow.md",
    "眼前構築": "mechanics/flow.md",
    "双掌繚乱": "mechanics/flow.md",

    # Keywords -> mechanics/index.md
    "連火": "mechanics/index.md",
    "決死": "mechanics/index.md",
    "八相": "mechanics/index.md",
    "境地": "mechanics/index.md",
    "設置": "mechanics/index.md",
    "開閉": "mechanics/index.md",
    "計略": "mechanics/index.md",
    "遠心": "mechanics/index.md",
    "毒": "megami/index.md", # Specific to Chikage but mechanic is often looked up
    "機巧": "mechanics/index.md",
    "騎動": "mechanics/index.md",
    "造花": "mechanics/index.md",
    "帯電": "mechanics/index.md",
    "灰塵": "mechanics/index.md",
    "守護": "mechanics/index.md",
    "凍結": "mechanics/index.md",
    "鏡映": "mechanics/index.md",
}

DOCS_DIR = Path("docs")

def get_relative_link(source_file, target_file):
    """Calculates relative link from source_file to target_file."""
    # Source file is absolute or relative to cwd. We need it relative to docs root to find depth
    # But here target_file is 'megami/index.md' (relative to docs root)
    # We need to construct ../megami/index.md from source_file
    
    # Example: source = docs/mechanics/flow.md, target = megami/index.md
    # source_dir = docs/mechanics
    # rel_path = ../megami/index.md
    
    source_dir = source_file.parent
    target_abs = DOCS_DIR / target_file
    try:
        rel_path = os.path.relpath(target_abs, source_dir)
        return rel_path
    except ValueError:
        return str(target_abs)

def process_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Sort terms by length (descending) to match longest first (e.g. "桜花結晶" before "結晶" if we had both)
    sorted_terms = sorted(TERM_MAPPING.keys(), key=len, reverse=True)
    
    # Create regex pattern
    # 1. Existing markdown links: \[.*?\]\(.*?\)
    # 2. HTML tags: <[^>]*>
    # 3. Code blocks: `[^`]*` or ```[\s\S]*?``` (simplistic)
    # 4. Headers: ^#+ .* (We might want to avoid linking in headers?) -> Let's avoid linking in headers for now as it breaks ToC sometimes
    # 5. Terms: (Term)
    
    # Note: Regex for markdown is hard. We do a best effort.
    # Group 1: Protected content (Links, Code, Tags)
    # Group 2: Terms
    
    # Protected patterns
    p_link = r'\[.*?\]\(.*?\)'
    p_image = r'!\[.*?\]\(.*?\)'
    p_code_inline = r'`[^`\n]+`'
    p_code_block = r'```[\s\S]*?```'
    p_html = r'<[^>]+>'
    p_header = r'^#{1,6}\s.*$' # Match headers
    
    protected_pattern = f"({p_code_block}|{p_link}|{p_image}|{p_code_inline}|{p_html}|{p_header})"
    
    # Term pattern
    terms_pattern = "(" + "|".join(re.escape(t) for t in sorted_terms) + ")"
    
    # Combined pattern
    # We want to match Protected OR Term
    pattern = re.compile(f"{protected_pattern}|{terms_pattern}", re.MULTILINE)

    def replace_func(match):
        g1 = match.group(1) # Protected
        g2 = match.group(2) # Term
        
        if g1:
            return g1 # Return protected content as is
        
        if g2:
            term = g2
            target_file_key = TERM_MAPPING[term]
            
            # Avoid self-linking
            # Check if current file matches target file
            # file_path is something like 'docs/megami/index.md'
            # target_file_key is 'megami/index.md'
            rel_source = os.path.relpath(file_path, DOCS_DIR)
            if rel_source == target_file_key:
                return term # Don't link to self
                
            link_url = get_relative_link(file_path, target_file_key)
            return f"[{term}]({link_url})"
            
        return match.group(0)

    new_content = pattern.sub(replace_func, content)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  Updated {file_path}")
    else:
        print(f"  No changes for {file_path}")

def main():
    if not DOCS_DIR.exists():
        print("docs directory not found.")
        return

    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = Path(root) / file
                process_file(file_path)

if __name__ == "__main__":
    main()
