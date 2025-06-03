"""Example module with a simple greeting function."""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a friendly greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Running `python -m dogmatica.example` will display a greeting
    print(greet("World"))
