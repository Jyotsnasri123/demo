# hello.py
"""
Sample Python file for GitHub upload.
This script demonstrates a simple function, a class, and main execution.
"""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

class Calculator:
    """A simple calculator class."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

if __name__ == "__main__":
    # Example usage
    print(greet("World"))

    calc = Calculator()
    print("Addition:", calc.add(10, 5))
    print("Subtraction:", calc.subtract(10, 5))
