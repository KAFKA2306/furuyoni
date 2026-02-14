import sys
from pathlib import Path
import os

# Add scripts/ to path to import maintain
sys.path.append(os.path.join(os.getcwd(), 'scripts'))

try:
    from maintain import build_card_map, DOCS_DIR
except ImportError:
    print("Could not import maintain.py")
    sys.exit(1)

def dump_map():
    print("Building card map using maintain.py logic...")
    card_map = build_card_map(DOCS_DIR)
    print(f"maintain.py found {len(card_map)} entries.")
    
    print("\n--- Internal Card Map Keys (Filename -> Name) ---")
    for k, v in sorted(card_map.items()):
        print(f"{k} -> [{v}]")
        
    # Now verify cards.md
    import re
    card_file = Path("docs/megami/cards.md")
    if not card_file.exists():
        print("cards.md not found")
        sys.exit(1)
        
    with open(card_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    pattern = re.compile(
        r'<span id="([^"]+)"></span>\[:external-link: !\[[^\]]+\]\(([^)]+)\)\]\(([^)]+)\)'
    )
    
    found = []
    for match in pattern.finditer(content):
        name = match.group(1)
        found.append(name)
        
    print(f"\nScanning cards.md found {len(found)} linked anchors.")
    print("--- Anchor Names ---")
    for name in sorted(found):
        print(f"[{name}]")

if __name__ == "__main__":
    dump_map()
