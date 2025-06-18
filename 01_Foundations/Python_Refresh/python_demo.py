#!/usr/bin/env python3
"""
Python Demo Script
A comprehensive demonstration of Python features and best practices.
"""

import datetime
import json
import logging
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from functools import wraps
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 1. Enums
class Color(Enum):
    """Color enumeration."""
    RED = 1
    GREEN = 2
    BLUE = 3

# 2. Dataclasses
@dataclass
class Person:
    """Person data class."""
    name: str
    age: int
    email: Optional[str] = None

# 3. Abstract Base Class
class Shape(ABC):
    """Abstract base class for shapes."""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter of the shape."""
        pass

# 4. Concrete Class
class Circle(Shape):
    """Circle class implementing Shape."""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14159 * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius

# 5. Decorator
def timer(func):
    """Decorator to measure function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        duration = (end_time - start_time).total_seconds()
        logger.info(f"{func.__name__} took {duration:.2f} seconds to execute")
        return result
    return wrapper

# 6. Context Manager
class FileHandler:
    """Context manager for file operations."""
    
    def __init__(self, filename: str, mode: str = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# 7. Generator Function
def fibonacci(n: int):
    """Generate Fibonacci sequence up to n."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 8. Type Hints and Modern Python Features
def process_data(data: List[Dict[str, Any]]) -> Dict[str, Union[int, float, str]]:
    """Process a list of dictionaries and return aggregated data."""
    result = {
        'count': len(data),
        'total': sum(item.get('value', 0) for item in data),
        'average': sum(item.get('value', 0) for item in data) / len(data) if data else 0
    }
    return result

# 9. Async Function (Python 3.7+)
async def async_operation():
    """Demonstrate async/await syntax."""
    import asyncio
    await asyncio.sleep(1)
    return "Async operation completed"

# 10. Main Function with Examples
@timer
def main():
    """Main function demonstrating various features."""
    
    # Demonstrate Enum
    logger.info(f"Color.RED: {Color.RED}")
    
    # Demonstrate Dataclass
    person = Person("John Doe", 30, "john@example.com")
    logger.info(f"Person: {person}")
    
    # Demonstrate Class Inheritance
    circle = Circle(5)
    logger.info(f"Circle area: {circle.area():.2f}")
    logger.info(f"Circle perimeter: {circle.perimeter():.2f}")
    
    # Demonstrate Generator
    logger.info("Fibonacci sequence:")
    for num in fibonacci(5):
        logger.info(num)
    
    # Demonstrate File Operations
    with FileHandler("demo.txt", "w") as f:
        f.write("Hello, Python!")
    
    # Demonstrate Data Processing
    data = [
        {"value": 10},
        {"value": 20},
        {"value": 30}
    ]
    result = process_data(data)
    logger.info(f"Processed data: {result}")
    
    # Demonstrate Path Operations
    current_dir = Path.cwd()
    logger.info(f"Current directory: {current_dir}")
    
    # Demonstrate JSON Operations
    json_data = json.dumps(result, indent=2)
    logger.info(f"JSON data:\n{json_data}")

if __name__ == "__main__":
    main() 