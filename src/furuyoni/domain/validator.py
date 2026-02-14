import re
import requests
from typing import List, Tuple, Dict, Optional
from concurrent.futures import ThreadPoolExecutor


class LinkValidator:
    def __init__(self, max_workers: int = 10) -> None:
        self.max_workers: int = max_workers

    def extract_links(self, content: str) -> List[str]:
        return re.findall(r"\[.*?\]\((http[s]?://[^\s\)]+)\)", content)

    def check_link(self, url: str) -> Tuple[str, Optional[int], str]:
        response: requests.Response = requests.get(url, stream=True)
        response.raise_for_status()
        return url, response.status_code, "OK"

    def validate_batch(self, urls: List[str]) -> Dict[str, Tuple[Optional[int], str]]:
        results: Dict[str, Tuple[Optional[int], str]] = {}
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_url = {executor.submit(self.check_link, url): url for url in urls}
            for future in future_to_url:
                url, status, msg = future.result()
                results[url] = (status, msg)
        return results
