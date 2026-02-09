import os
import re
import requests
from concurrent.futures import ThreadPoolExecutor

DOCS_DIR = "/home/kafka/furuyoni/docs"

def get_markdown_files(directory):
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def extract_links(file_path):
    links = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Regex for markdown links [text](url)
            # focusing on http/https
            md_links = re.findall(r'\[.*?\]\((http[s]?://[^\s\)]+)\)', content)
            links.extend(md_links)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return links

def check_link(url):
    try:
        # Some sites block HEAD requests, use GET with stream=True to avoid downloading large content
        response = requests.get(url, stream=True, timeout=5)
        if response.status_code >= 400:
            return url, response.status_code, "Broken"
        return url, response.status_code, "OK"
    except requests.RequestException as e:
        return url, None, str(e)

def main():
    files = get_markdown_files(DOCS_DIR)
    file_link_map = {}
    all_links = set()

    for file in files:
        file_links = extract_links(file)
        if file_links:
            relative_path = os.path.relpath(file, "/home/kafka/furuyoni")
            file_link_map[relative_path] = file_links
            for link in file_links:
                all_links.add(link)

    print(f"Found {len(all_links)} unique links in {len(file_link_map)} files.")

    results = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_link, url): url for url in all_links}
        for future in future_to_url:
            url, status, msg = future.result()
            results[url] = (status, msg)

    broken_found = False
    print("\n--- LINK CHECK REPORT ---\n")
    for file, links in file_link_map.items():
        file_broken = []
        for link in set(links): # Check unique links per file
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
