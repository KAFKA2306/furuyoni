import os
import re
import urllib.request
from urllib.error import HTTPError
import time

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DEST_DIR = os.path.join(DOCS_DIR, 'assets/images')
BASE_URL = 'https://main-bakafire.ssl-lolipop.jp/furuyoni/na/images/'

# Regex to find these specific external images
# Matches: https://main-bakafire.ssl-lolipop.jp/furuyoni/na/images/...
URL_PATTERN = r'https://main-bakafire\.ssl-lolipop\.jp/furuyoni/na/images/([^\s\)\"\']+)'

def download_image(rel_path):
    full_url = f"{BASE_URL}{rel_path}"
    local_path = os.path.join(DEST_DIR, rel_path)
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    if os.path.exists(local_path):
        return True # Already downloaded
    
    try:
        # Add User-Agent to mimic browser
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(local_path, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Downloaded: {rel_path}")
        time.sleep(0.5) # Be nice to the server
        return True
    except HTTPError as e:
        print(f"Failed to download {full_url}: {e.code}")
        return False
    except Exception as e:
        print(f"Error downloading {full_url}: {e}")
        return False

def process_file_content(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    matches = list(set(re.findall(URL_PATTERN, content)))
    if not matches:
        return
    
    print(f"Processing {file_path} - Found {len(matches)} images")
    
    # Download images
    for match in matches:
        download_image(match)
    
    # Calculate relative path from this file to docs/assets/images
    # file_path: /home/kafka/furuyoni/docs/subdir/file.md
    # DEST_DIR: /home/kafka/furuyoni/docs/assets/images
    
    # We want relative path from file_dir to dest_dir
    # e.g. ../assets/images
    rel_path_to_assets = os.path.relpath(DEST_DIR, os.path.dirname(file_path))

    def replacer(match_obj):
        # original match: na_01_o_n/na_01_o_n_1.png (captured group 1)
        image_rel_path = match_obj.group(1)
        # return relative path to local image
        return f"{rel_path_to_assets}/{image_rel_path}"

    new_content = re.sub(URL_PATTERN, replacer, content)
    
    with open(file_path, 'w') as f:
        f.write(new_content)

def main():
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith('.md'):
                process_file_content(os.path.join(root, file))

if __name__ == '__main__':
    main()
