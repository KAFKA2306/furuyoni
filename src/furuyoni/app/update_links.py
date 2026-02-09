import os
from pathlib import Path
from furuyoni.infrastructure.paths import DOCS_DIR
from furuyoni.domain.linker import Linker

class UpdateLinksUseCase:
    def __init__(self, linker: Linker) -> None:
        self.linker: Linker = linker

    def execute(self) -> None:
        for root, _, files in os.walk(DOCS_DIR):
            for file in files:
                if file.endswith(".md"):
                    file_path: Path = Path(root) / file
                    self._process_file(file_path)

    def _process_file(self, file_path: Path) -> None:
        with open(file_path, "r", encoding="utf-8") as f:
            content: str = f.read()
        new_content: str = self.linker.process_content(content, file_path)
        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {file_path}")
