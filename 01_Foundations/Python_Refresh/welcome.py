#!/usr/bin/env python3

from datetime import datetime

def get_learning_paths():
    # Now returns a list of dictionaries for better data organization
    return [
        {"id": "1", "name": "Machine Learning Basics"},
        {"id": "2", "name": "Deep Learning"},
        {"id": "3", "name": "Natural Language Processing"},
        {"id": "4", "name": "Computer Vision"}
    ]

def get_welcome_message(name, learning_path):
    current_time = datetime.now().strftime("%H:%M:%S")
    # Special greeting for the AI Director
    if name.lower() == "scott":
        greeting = f"Hey, it's the awesome AI Director, {name}!"
    else:
        greeting = f"Welcome to your AI Native Journey, {name}!"
    box_width = 60
    lines = [
        greeting,
        f"Current time: {current_time}",
        f"Selected Path: {learning_path}",
        "Let's begin our exploration of AI and machine learning!"
    ]
    box = "\n" + "╔" + "═" * (box_width - 2) + "╗\n"
    for line in lines:
        box += f"║ {line.ljust(box_width - 4)} ║\n"
    box += "╚" + "═" * (box_width - 2) + "╝\n"
    return box

def get_user_words():
    """
    Prompts the user to enter a noun, a verb, and an adjective, and returns them as a tuple.
    Returns:
        tuple: (noun, verb, adjective)
    """
    noun = input("Enter a noun: ").strip()
    verb = input("Enter a verb: ").strip()
    adjective = input("Enter an adjective: ").strip()
    return noun, verb, adjective

def main():
    # Get user's name with validation
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please try again.")
    
    # Show available learning paths
    print("\nAvailable Learning Paths:")
    paths = get_learning_paths()
    for path in paths:
        print(f"{path['id']}. {path['name']}")
    
    # Get user's path choice with validation
    while True:
        choice = input("\nSelect your learning path (1-4): ").strip()
        selected_path = next((p['name'] for p in paths if p['id'] == choice), None)
        if selected_path:
            break
        print("Invalid choice. Please select a number between 1 and 4.")
    
    # Display welcome message
    print(get_welcome_message(name, selected_path))

if __name__ == "__main__":
    main() 