import os
import re
from collections import defaultdict

DOCS_DIR = "/home/kafka/furuyoni/docs"
MKDOCS_FILE = "/home/kafka/furuyoni/mkdocs.yml"

def get_all_md_files():
    files = []
    for root, _, filenames in os.walk(DOCS_DIR):
        for filename in filenames:
            if filename.endswith(".md"):
                full_path = os.path.join(root, filename)
                files.append(full_path)
    return sorted(files)

def parse_mkdocs_nav():
    referenced = set()
    if not os.path.exists(MKDOCS_FILE):
        print(f"Error: {MKDOCS_FILE} not found.")
        return referenced
        
    with open(MKDOCS_FILE, 'r') as f:
        lines = f.readlines()
    
    in_nav = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("nav:"):
            in_nav = True
            continue
            
        if in_nav:
            # Check if we exited nav (heuristic: unindented top-level key)
            if line and not line.startswith(" ") and not line.startswith("#") and ":" in line:
                in_nav = False
                continue
                
            # Extract .md file
            # Common patterns: "- Title: path/to/file.md", "- path/to/file.md", "    - Title: path/to/file.md"
            # We look for value ending in .md
            # Or simplified regex finding .md in value position
            
            # Find .md file path in the line
            matches = re.findall(r'[\s:]([\w\-/]+\.md)', line)
            for m in matches:
                # Add docs prefix since nav relative to docs_dir
                full_path = os.path.join(DOCS_DIR, m.strip())
                referenced.add(full_path)

    return referenced

def audit_headers(file_path):
    issues = []
    h1_count = 0
    last_level = 0
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if line.startswith("#"):
            # Check for header format
            match = re.match(r'^(#+)\s', line)
            if match:
                level = len(match.group(1))
                if level == 1:
                    h1_count += 1
                
                # Check skipping levels (e.g. H2 -> H4)
                if level > last_level + 1:
                    issues.append(f"Line {i+1}: Skipped heading level (H{last_level} -> H{level})")
                
                last_level = level

    if h1_count == 0:
        issues.append("Missing H1 header")
    elif h1_count > 1:
        issues.append(f"Multiple ({h1_count}) H1 headers found")
        
    return issues

def audit_links(file_path, all_files_set):
    outgoing_internal = []
    issues = []
    file_dir = os.path.dirname(file_path)
    
    with open(file_path, 'r') as f:
        content = f.read()
        
    # Find all links [text](target)
    # Be careful with images ![alt](src) - we want to audit src existence but not count as nav link
    # We also want to check if src exists
    
    # Iterate over all [.*](.*) matches
    # We use iterator to get position if needed, but regex findall is easier
    
    # Pattern: (!?)\[(.*?)\]\((.*?)\)
    # Group 1: ! or empty
    # Group 2: text
    # Group 3: url (may contain "title")
    
    refs = re.findall(r'(!?)\[(.*?)\]\((.*?)\)', content)
    
    for is_img, text, raw_link in refs:
        link = raw_link.split()[0] # remove title
        if not link: continue
        
        if link.startswith("http") or link.startswith("mailto:"):
            continue
            
        if link.startswith("#"):
            # Internal anchor, ignore file check
            continue
            
        # Parse link
        # Handle anchors
        if "#" in link:
            target_file_part = link.split("#")[0]
            if not target_file_part:
                continue # just #anchor
        else:
            target_file_part = link
        
        # Resolve path
        # If / start, relative to docs_dir? MkDocs standard behavior is relative to current file usually
        # But if user uses / for root relative
        if target_file_part.startswith("/"):
            # Assume relative to docs root
            abs_target = os.path.normpath(os.path.join(DOCS_DIR, target_file_part.lstrip("/")))
        else:
            abs_target = os.path.normpath(os.path.join(file_dir, target_file_part))
            
        if not os.path.exists(abs_target):
            # Try appending .md? No, links should be exact usually
            # But wait, sometimes links are to directory (index.md implicitly)?
            # MkDocs supports directory links -> index.md
            if os.path.isdir(abs_target):
                index_check = os.path.join(abs_target, "index.md")
                if os.path.exists(index_check):
                    abs_target = index_check
                else:
                    issues.append(f"Broken link: {link}")
                    continue
            else:
                issues.append(f"Broken link: {link}")
                continue
                
        # If it is a markdown file
        if abs_target.endswith(".md"):
            if not is_img:
                outgoing_internal.append(abs_target)

    # Dedup outgoing
    return list(set(outgoing_internal)), issues

def main():
    print("Running SEO Audit...")
    all_files = get_all_md_files()
    all_files_set = set(all_files)
    nav_files = parse_mkdocs_nav()
    
    # 1. Nav Consistency
    print("\n=== Nav Consistency Check ===")
    nav_orphans = []
    for f in all_files:
        if f not in nav_files:
            nav_orphans.append(f)
            
    if nav_orphans:
        print(f"Files not in 'nav' ({len(nav_orphans)}):")
        for f in nav_orphans:
            print(f"  - {os.path.relpath(f, DOCS_DIR)}")
    else:
        print("All files are in 'nav'.")

    # 2. Structure & Links
    print("\n=== Structure & Link Audit ===")
    
    link_graph = defaultdict(list)
    backlinks = defaultdict(int)
    total_issues = 0
    
    for f in all_files:
        rel_path = os.path.relpath(f, DOCS_DIR)
        
        # Headers
        h_issues = audit_headers(f)
        if h_issues:
            print(f"\n{rel_path} [HEADERS]:")
            for i in h_issues:
                print(f"  - {i}")
            total_issues += len(h_issues)
            
        # Links
        outgoing, l_issues = audit_links(f, all_files_set)
        if l_issues:
            print(f"\n{rel_path} [LINKS]:")
            for i in l_issues:
                print(f"  - {i}")
            total_issues += len(l_issues)
            
        link_graph[f] = outgoing
        for distinct_target in outgoing:
            backlinks[distinct_target] += 1
            
    # 3. Graph Analysis
    print("\n=== Graph Analysis ===")
    
    # Orphans (No backlinks)
    orphans = []
    for f in all_files:
        if f.endswith("index.md"): continue # Index usually entry point
        if backlinks[f] == 0:
            orphans.append(f)
            
    if orphans:
        print(f"Orphan files (0 internal backlinks):")
        for f in orphans:
            print(f"  - {os.path.relpath(f, DOCS_DIR)}")
            
    # Dead ends (No outgoing)
    dead_ends = []
    for f in all_files:
        if not link_graph[f]:
            dead_ends.append(f)
            
    if dead_ends:
        print(f"Dead-end files (0 outgoing internal links):")
        for f in dead_ends:
            print(f"  - {os.path.relpath(f, DOCS_DIR)}")

    # 4. Feature Enhancements
    print("\n=== Feature Usage ===")
    for f in all_files:
        with open(f, 'r') as file:
            c = file.read()
            # Check for missed admonitions
            if "> **" in c or "> [!" in c:
                print(f"  - {os.path.relpath(f, DOCS_DIR)}: Potential legacy blockquote.")

if __name__ == "__main__":
    main()
