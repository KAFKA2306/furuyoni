import os
import re

def check_headings(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    headings = re.findall(r'^(#+)\s+(.*)', content, re.MULTILINE)
    
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
            errors.append(f"Header level skipped: H{prev_level} -> H{level} ('{title}')")
        prev_level = level
    
    return errors

def check_links(file_path, all_files):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple relative link regex: [text](path.md)
    # This also catches image links ![alt](path.png)
    links = re.findall(r'\[.*?\]\((?!http|mailto)(.*?)(?:#.*?)?\)', content)
    img_links = re.findall(r'!\[.*?\]\((?!http)(.*?)\)', content)
    
    errors = []
    for link in links + img_links:
        if not link: continue
        # Handle links that start with / (relative to docs root if needed, but usually relative to file)
        # For simplicity, assume relative to file unless starts with /
        dir_name = os.path.dirname(file_path)
        if link.startswith('/'):
            target_path = os.path.join('docs', link.lstrip('/'))
        else:
            target_path = os.path.normpath(os.path.join(dir_name, link))
        
        if not os.path.exists(target_path):
            errors.append(f"Broken link: {link} (Target: {target_path})")
            
    return errors

def main():
    docs_dir = 'docs'
    all_files = []
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                all_files.append(os.path.join(root, file))
    
    print("--- Heading and Link Audit ---")
    for file_path in all_files:
        h_errors = check_headings(file_path)
        l_errors = check_links(file_path, all_files)
        
        if h_errors or l_errors:
            print(f"\nFile: {file_path}")
            for err in h_errors:
                print(f"  [HEADING] {err}")
            for err in l_errors:
                print(f"  [LINK] {err}")

if __name__ == "__main__":
    main()
