import re
import requests
from typing import List, Tuple
from concurrent.futures import ThreadPoolExecutor

class LinkValidator:
    def __init__(self, timeout: int = 5, max_workers: int = 10):
        self.timeout = timeout
        self.max_workers = max_workers

    def extract_links(self, content: str) -> List[str]:
        # Regex for markdown links [text](url) focusing on http/https
        return re.findall(r'\[.*?\]\((http[s]?://[^\s\)]+)\)', content)

    def check_link(self, url: str) -> Tuple[str, int, str]:
        try:
            # Some sites block HEAD requests, use GET with stream=True to avoid downloading large content
            response = requests.get(url, stream=True, timeout=self.timeout)
            if response.status_code >= 400:
                return url, response.status_code, "Broken"
            return url, response.status_code, "OK"
        except requests.RequestException as e:
            return url, None, str(e)

    def validate_batch(self, urls: List[str]) -> dict:
        results = {}
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_url = {executor.submit(self.check_link, url): url for url in urls}
            for future in future_to_url:
                url, status, msg = future.result()
                results[url] = (status, msg)
        return results
