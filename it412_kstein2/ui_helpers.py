# Kyle Stein 
# Walsh College
# IT 412
# 2/6/2026
# Week 6 & 7 Python Database

"""
ui_helpers.py

Helper functions for the CLI interface.
"""

def prompt_int(prompt: str) -> int:
    """Keep asking until the user types a valid integer."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")
