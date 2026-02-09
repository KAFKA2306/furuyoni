import sys
import os
from pathlib import Path

# Add src to sys.path to allow imports
SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from furuyoni.infrastructure.paths import DOCS_DIR, PROJECT_ROOT
from furuyoni.domain.validator import LinkValidator

def main():
    validator = LinkValidator()
    
    file_link_map = {}
    all_links = set()

    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = Path(root) / file
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    links = validator.extract_links(content)
                    if links:
                        rel_path = os.path.relpath(file_path, PROJECT_ROOT)
                        file_link_map[rel_path] = links
                        for link in links:
                            all_links.add(link)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    print(f"Found {len(all_links)} unique links in {len(file_link_map)} files.")

    results = validator.validate_batch(list(all_links))

    broken_found = False
    print("\n--- LINK CHECK REPORT ---\n")
    for file, links in file_link_map.items():
        file_broken = []
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

if __name__ == "__main__":
    main()
