"""Utility functions for the XOR neural network example."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def generate_xor_data() -> tuple[np.ndarray, np.ndarray]:
    """Generate inputs and targets for the XOR problem.

    Returns
    -------
    X : ndarray of shape (4, 2)
        All possible pairs of binary inputs.
    y : ndarray of shape (4, 1)
        XOR outputs for each input pair.
    """
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1],
    ], dtype=float)
    y = np.array([[0], [1], [1], [0]], dtype=float)
    return X, y


def plot_loss(loss_history: list[float]) -> None:
    """Plot training loss versus epochs."""
    plt.figure(figsize=(6, 4))
    plt.plot(loss_history, label="Training loss")
    plt.xlabel("Epoch")
    plt.ylabel("Binary cross-entropy loss")
    plt.title("Training Loss Curve")
    plt.legend()
    plt.tight_layout()
    plt.show()

