import re
from pathlib import Path

def debug_saine():
    p = Path("docs/megami/02_saine.md")
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()

    header_pat = re.compile(r"^#{3}\s+[NS]\d+\s+(.+)$", re.MULTILINE)
    
    print(f"Scanning {p}...")
    valid_names = set()
    for m in header_pat.finditer(content):
        raw_name = m.group(1).strip()
        print(f"Raw Header: '{raw_name}'")
        
        # Clean up: remove reading in parens, e.g. "Name (Reading)" -> "Name"
        clean = re.split(r"[（(]", raw_name)[0].strip()
        
        # Remove markdown images/links: [![Alt](Url)] -> Alt, [Text](Url) -> Text
        # Regex to replace ![Alt](Url) with Alt
        # clean = re.sub(r"!\[([^\]]*)\]\(.*?\)", r"\1", clean)
        # Regex to replace [Text](Url) with Text
        # clean = re.sub(r"\[([^\]]+)\]\(.*?\)", r"\1", clean)
        
        # Combined logic from maintain.py
        clean = re.sub(r"!\[([^\]]*)\]\(.*?\)", r"\1", clean)
        clean = re.sub(r"\[([^\]]+)\]\(.*?\)", r"\1", clean)
        
        clean = clean.strip()
        print(f"Cleaned: '{clean}'")
        
        if clean:
            valid_names.add(clean)
            
    print(f"Valid Names: {valid_names}")
    
    img_pat = re.compile(r"!\[([^\]]*)\]\((?:[^)]*/)?([^/]+\.png)(?:\s.*?)?\)")
    for m in img_pat.finditer(content):
        alt = m.group(1).strip()
        fn = m.group(2).strip()
        if alt in valid_names:
            print(f"MATCH: {fn} -> {alt}")
        else:
            print(f"MISS: {fn} -> {alt} (Alt not in valid names)")

if __name__ == "__main__":
    debug_saine()
