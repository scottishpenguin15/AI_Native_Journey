#!/usr/bin/env python3

from datetime import datetime

def get_welcome_message(name):
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  Welcome to your AI Native Journey, {name}!                ║
║                                                            ║
║  Current time: {current_time}                              ║
║                                                            ║
║  Let's begin our exploration of AI and machine learning!   ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
"""

def main():
    name = input("Please enter your name: ").strip()
    if not name:
        name = "Explorer"
    print(get_welcome_message(name))

if __name__ == "__main__":
    main() 