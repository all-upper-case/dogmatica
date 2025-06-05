"""Entry point for training the XOR neural network."""

from __future__ import annotations

import numpy as np

from neural_network import SimpleNeuralNetwork
from utils import generate_xor_data, plot_loss


def main() -> None:
    """Train ``SimpleNeuralNetwork`` on the XOR dataset and display results."""
    # 1. Generate XOR dataset (four samples with two features each)
    X, y = generate_xor_data()

    # 2. Initialize the neural network
    #    input_size = 2 for the two XOR inputs
    #    hidden_size = 2 is sufficient to learn XOR
    #    learning_rate = 0.1 is a common default
    model = SimpleNeuralNetwork(input_size=2, hidden_size=2, learning_rate=0.1)

    # 3. Train the model for a fixed number of epochs
    epochs = 10000
    loss_history = model.train(X, y, epochs)

    # 4. Display predictions after training
    predictions = model.predict(X)
    for inp, pred in zip(X, predictions):
        print(f"Input: {inp} -> Predicted: {int(pred[0])}")

    # 5. Plot the loss curve
    plot_loss(loss_history)

    # 6. Assess final performance
    accuracy = np.mean(predictions == y)
    print(f"Training accuracy: {accuracy * 100:.1f}%")


if __name__ == "__main__":
    main()

