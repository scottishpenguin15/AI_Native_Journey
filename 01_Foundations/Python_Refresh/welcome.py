#!/usr/bin/env python3

from datetime import datetime

def get_learning_paths():
    return {
        "1": "Machine Learning Basics",
        "2": "Deep Learning",
        "3": "Natural Language Processing",
        "4": "Computer Vision"
    }

def get_welcome_message(name, learning_path):
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  Welcome to your AI Native Journey, {name}!                ║
║                                                            ║
║  Current time: {current_time}                              ║
║                                                            ║
║  Selected Path: {learning_path}                            ║
║                                                            ║
║  Let's begin our exploration of AI and machine learning!   ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
"""

def main():
    # Get user's name
    name = input("Please enter your name: ").strip()
    if not name:
        name = "Explorer"
    
    # Show available learning paths
    print("\nAvailable Learning Paths:")
    paths = get_learning_paths()
    for key, value in paths.items():
        print(f"{key}. {value}")
    
    # Get user's path choice
    while True:
        choice = input("\nSelect your learning path (1-4): ").strip()
        if choice in paths:
            selected_path = paths[choice]
            break
        print("Invalid choice. Please select a number between 1 and 4.")
    
    # Display welcome message
    print(get_welcome_message(name, selected_path))

if __name__ == "__main__":
    main() 