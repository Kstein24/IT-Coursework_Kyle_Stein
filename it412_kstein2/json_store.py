# Kyle Stein 
# Walsh College
# IT 412
# 1/22/2026
# Week 2 & 3 Files And Exceptions

"""
JSON file utilities.

Handles loading, saving, and backing up JSON configuration files.
"""

import json
import shutil
import time
from pathlib import Path
from typing import Any, Optional


def load_json(path: Path, default: Optional[Any] = None) -> Any:
    """
    Load JSON data from a file.
    Returns a default value if the file does not exist.
    Raises an error if the file exists but is invalid JSON.
    """
    if not path.exists():
        return default

    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path.name}") from exc


def backup_file(path: Path) -> None:
    """
    Create a timestamped backup of an existing file.
    """
    if path.exists() and path.is_file():
        backup_path = path.with_name(f"{path.name}.backup_{int(time.time())}")
        shutil.copy2(path, backup_path)


def save_json(path: Path, data: Any, *, make_backup_on_overwrite: bool = False) -> None:
    """
    Save data to a JSON file.
    Optionally create a backup every time the file is overwritten.
    """
    if make_backup_on_overwrite and path.exists():
        backup_file(path)

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
