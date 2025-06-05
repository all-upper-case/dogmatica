"""Simple neural network implementation for the XOR problem.

This module defines ``SimpleNeuralNetwork`` which is a tiny feedforward
network with one hidden layer trained using batch gradient descent. Only
``numpy`` is required. The network uses the sigmoid activation function
and binary cross-entropy loss.
"""

from __future__ import annotations

import numpy as np


class SimpleNeuralNetwork:
    """A minimal feedforward neural network with one hidden layer.

    Parameters
    ----------
    input_size : int
        Number of features in the input data.
    hidden_size : int
        Number of neurons in the hidden layer.
    learning_rate : float
        Step size used during gradient descent updates.
    """

    def __init__(self, input_size: int, hidden_size: int, learning_rate: float) -> None:
        self.learning_rate = learning_rate
        # Initialize weights with small random values for symmetry breaking
        rng = np.random.default_rng()
        self.W1 = rng.standard_normal((input_size, hidden_size)) * 0.1
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = rng.standard_normal((hidden_size, 1)) * 0.1
        self.b2 = np.zeros((1, 1))

    @staticmethod
    def _sigmoid(z: np.ndarray) -> np.ndarray:
        """Compute the sigmoid activation function."""
        return 1 / (1 + np.exp(-z))

    def forward(self, X: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Perform the forward pass.

        Parameters
        ----------
        X : ndarray of shape (n_samples, input_size)
            Input data.

        Returns
        -------
        hidden : ndarray of shape (n_samples, hidden_size)
            Activations of the hidden layer.
        output : ndarray of shape (n_samples, 1)
            Network output after the final sigmoid activation.
        """
        # Hidden layer computation
        hidden_linear = X @ self.W1 + self.b1
        hidden = self._sigmoid(hidden_linear)

        # Output layer computation
        output_linear = hidden @ self.W2 + self.b2
        output = self._sigmoid(output_linear)
        return hidden, output

    def backward(self, X: np.ndarray, y: np.ndarray, output: np.ndarray, hidden: np.ndarray) -> None:
        """Backpropagate the error and update weights.

        Parameters
        ----------
        X : ndarray of shape (n_samples, input_size)
            Training inputs.
        y : ndarray of shape (n_samples, 1)
            Target labels (0 or 1).
        output : ndarray of shape (n_samples, 1)
            Predictions from the forward pass.
        hidden : ndarray of shape (n_samples, hidden_size)
            Hidden layer activations from the forward pass.
        """
        n_samples = X.shape[0]

        # Binary cross-entropy loss derivative w.r.t. output layer input
        d_output = output - y  # shape (n_samples, 1)

        # Gradients for W2 and b2
        dW2 = hidden.T @ d_output / n_samples
        db2 = np.sum(d_output, axis=0, keepdims=True) / n_samples

        # Backpropagate through hidden layer
        d_hidden = (d_output @ self.W2.T) * hidden * (1 - hidden)
        dW1 = X.T @ d_hidden / n_samples
        db1 = np.sum(d_hidden, axis=0, keepdims=True) / n_samples

        # Update parameters
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1

    def train(self, X: np.ndarray, y: np.ndarray, epochs: int) -> list[float]:
        """Train the network.

        Parameters
        ----------
        X : ndarray of shape (n_samples, input_size)
            Training data.
        y : ndarray of shape (n_samples, 1)
            Binary targets.
        epochs : int
            Number of times to iterate over ``X`` and ``y``.

        Returns
        -------
        list of float
            History of loss values for each epoch.
        """
        loss_history = []
        for _ in range(epochs):
            hidden, output = self.forward(X)

            # Compute binary cross-entropy loss
            loss = -np.mean(y * np.log(output + 1e-8) + (1 - y) * np.log(1 - output + 1e-8))
            loss_history.append(loss)

            # Update parameters using backpropagation
            self.backward(X, y, output, hidden)
        return loss_history

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict class labels for ``X``.

        Parameters
        ----------
        X : ndarray of shape (n_samples, input_size)
            Input samples.

        Returns
        -------
        ndarray of shape (n_samples, 1)
            Predicted classes (0 or 1).
        """
        _, output = self.forward(X)
        return (output >= 0.5).astype(int)

