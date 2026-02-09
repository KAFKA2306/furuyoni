import os
from pathlib import Path
from furuyoni.infrastructure.paths import DOCS_DIR
from furuyoni.domain.linker import Linker

class UpdateLinksUseCase:
    def __init__(self, linker: Linker):
        self.linker = linker

    def execute(self):
        if not DOCS_DIR.exists():
            print(f"Directory not found: {DOCS_DIR}")
            return

        for root, _, files in os.walk(DOCS_DIR):
            for file in files:
                if file.endswith(".md"):
                    file_path = Path(root) / file
                    self._process_file(file_path)

    def _process_file(self, file_path: Path):
        print(f"Processing {file_path}...")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = self.linker.process_content(content, file_path)
        
        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  Updated {file_path}")
        else:
            print(f"  No changes for {file_path}")
