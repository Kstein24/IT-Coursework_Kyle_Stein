# Kyle Stein 
# Walsh College
# IT 412
# 1/22/2026
# Week 2 & 3 Files And Exceptions

"""
Primary configuration management.

Handles creation, loading, editing, and saving of primary_config.json.
"""

from pathlib import Path
from typing import Dict

from functions.cli import prompt_choice, prompt_nonempty, prompt_yes_no, print_header
from functions.json_store import load_json, save_json


# Default configuration required by the assignment
DEFAULT_PRIMARY: Dict[str, str] = {
    "Safe Mode": "On",
    "Memory": "32MB",
    "Error Log": "logs/errors.log",
}


def primary_config_path(base_dir: Path) -> Path:
    """
    Return the full path to primary_config.json.
    """
    return base_dir / "primary_config.json"


def ensure_primary_config_exists(base_dir: Path) -> None:
    """
    Ensure the primary configuration file exists and is valid.
    Also ensures the logs directory exists.
    """
    (base_dir / "logs").mkdir(parents=True, exist_ok=True)

    path = primary_config_path(base_dir)
    existing = load_json(path, default=None)

    # Create file if missing or invalid
    if existing is None or not isinstance(existing, dict) or len(existing) == 0:
        save_json(path, DEFAULT_PRIMARY)


def load_primary_config(base_dir: Path) -> Dict[str, str]:
    """
    Load the primary configuration from disk.
    """
    ensure_primary_config_exists(base_dir)
    data = load_json(primary_config_path(base_dir), default=DEFAULT_PRIMARY)
    return {str(k): str(v) for k, v in data.items()}


def save_primary_config(base_dir: Path, primary: Dict[str, str]) -> None:
    """
    Save the primary configuration to disk.
    Must contain at least one key/value pair.
    """
    if not primary:
        raise ValueError("Primary config must have at least one key/value pair.")
    save_json(primary_config_path(base_dir), primary)


def edit_primary_config(base_dir: Path, primary: Dict[str, str]) -> Dict[str, str]:
    """
    Interactive editor for the primary configuration.
    Allows add, modify, delete, and save operations.
    """
    while True:
        print_header("Modify Primary Configuration")

        for k, v in primary.items():
            print(f" - {k}: {v}")

        print("\nOptions:")
        print("1. Add a key/value pair")
        print("2. Modify an existing key")
        print("3. Delete a key")
        print("4. Save changes")
        print("5. Cancel")

        choice = prompt_choice("Choose (1-5): ", ["1", "2", "3", "4", "5"])

        if choice == "1":
            primary[prompt_nonempty("Key: ")] = prompt_nonempty("Value: ")

        elif choice == "2":
            key = prompt_nonempty("Key to modify: ")
            if key in primary:
                primary[key] = prompt_nonempty("New value: ")

        elif choice == "3":
            if len(primary) == 1:
                print("At least one key/value pair is required.")
                continue
            key = prompt_nonempty("Key to delete: ")
            primary.pop(key, None)

        elif choice == "4":
            save_primary_config(base_dir, primary)
            return primary

        elif choice == "5":
            if prompt_yes_no("Discard changes?"):
                return load_primary_config(base_dir)
