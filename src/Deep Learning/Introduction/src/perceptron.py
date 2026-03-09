import numpy as np
from activation import sigmoid

def update_weights(weights, x, z, y, lr):
    m = len(y)
    d_w = (1/m) * np.dot(x.T, (z - y))
    return weights - lr * d_w

def update_bias(bias, z, y, lr):
    m = len(y)
    d_b = (1/m) * np.sum(z - y)
    return bias - lr * d_b

def predict_proba(x, weights, bias):
    return sigmoid(np.dot(x, weights) + bias)