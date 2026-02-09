import os
from pathlib import Path

# Base directories
PROJECT_ROOT = Path(__file__).resolve().parents[3]
DOCS_DIR = PROJECT_ROOT / "docs"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
SRC_DIR = PROJECT_ROOT / "src"

def get_relative_docs_path(path: Path) -> str:
    """Returns path relative to docs directory."""
    try:
        return os.path.relpath(path, DOCS_DIR)
    except ValueError:
        return str(path)

def get_relative_path(target: Path, base: Path) -> str:
    """Calculates relative path from base to target."""
    try:
        return os.path.relpath(target, base)
    except ValueError:
        return str(target)
