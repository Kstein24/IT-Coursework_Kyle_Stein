# Kyle Stein 
# Walsh College
# IT 412
# 2/15/2026
# Final Project

"""
ui_tools.py

Simple helper prompts.
"""

def prompt_int(prompt: str) -> int:
    """Keep asking until user enters an integer."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")

def prompt_choice(prompt: str, choices: list[str]) -> str:
    """Prompt for a choice from a list of string options."""
    while True:
        val = input(prompt).strip()
        if val in choices:
            return val
        print(f"Invalid choice. Choose one of: {', '.join(choices)}")
