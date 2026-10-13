# Kyle Stein
# Walsh College
# IT 412
# 1/22/2026
# Week 2 & 3 Files And Exceptions

"""
CLI helper functions.
"""

from typing import Iterable


def prompt_choice(prompt: str, valid_choices: Iterable[str]) -> str:
    """
    Prompt the user until they enter one of the allowed choices.
    """
    valid = {c.strip() for c in valid_choices}
    while True:
        choice = input(prompt).strip()
        if choice in valid:
            return choice
        print(f"Invalid choice. Choose one of: {', '.join(sorted(valid))}")


def prompt_nonempty(prompt: str) -> str:
    """
    Prompt the user until they enter a non-empty value.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def prompt_yes_no(prompt: str) -> bool:
    """
    Prompt the user for a yes/no answer and return True or False.
    """
    while True:
        val = input(prompt + " (y/n): ").strip().lower()
        if val in ("y", "yes"):
            return True
        if val in ("n", "no"):
            return False
        print("Please enter y or n.")


def print_header(title: str) -> None:
    """
    Print a formatted section header for readability.
    """
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
