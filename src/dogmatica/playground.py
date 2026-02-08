"""Playground utilities for trying out ideas inside Dogmatica."""

from __future__ import annotations


def codex_playground() -> dict[str, str]:
    """Return metadata describing a lightweight experimental area.

    This function is intentionally simple: it defines a dedicated "playground"
    concept that can be extended with additional experiments over time.
    """
    return {
        "name": "Codex Playground",
        "description": "A safe area for trying ideas, prompts, and experiments.",
        "owner": "Codex",
    }
