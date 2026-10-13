# Kyle Stein 
# Walsh College
# IT 412
# 2/15/2026
# Final Project

"""
file_tools.py

Creates timestamped backups of output files before overwriting.
"""

from pathlib import Path
from datetime import datetime
import shutil


def backup_if_exists(path: Path) -> None:
    """If file exists, copy to <name>.backup_<timestamp>"""
    if path.exists() and path.is_file():
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = path.with_name(f"{path.name}.backup_{ts}")
        shutil.copy2(path, backup_path)