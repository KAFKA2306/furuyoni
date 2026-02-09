import os
from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).resolve().parents[3]
DOCS_DIR: Path = PROJECT_ROOT / "docs"
SCRIPTS_DIR: Path = PROJECT_ROOT / "scripts"
SRC_DIR: Path = PROJECT_ROOT / "src"

def get_relative_docs_path(path: Path) -> str:
    return os.path.relpath(path, DOCS_DIR)

def get_relative_path(target: Path, base: Path) -> str:
    return os.path.relpath(target, base)
