# Simple Python Neural Network XOR

This repository implements a small neural network from scratch in Python to
solve the classic XOR problem. It only depends on `numpy` and `matplotlib`.

## Installation

Create a virtual environment (optional) and install the requirements:

```bash
pip install -r requirements.txt
```

## Usage

Run the `main.py` script to train the network and display results:

```bash
python main.py
```

## Repository structure

- `neural_network.py` – contains a minimal implementation of a feedforward
  neural network with one hidden layer.
- `utils.py` – helper functions to generate the XOR dataset and plot the loss
  during training.
- `main.py` – script that ties everything together: data generation,
  training the model, displaying predictions and plotting the loss curve.

## Example

After training, the network predicts the XOR outputs correctly and the loss
curve decreases over time.

