import numpy as np

def get_accuracy(y_pred, y_actual):
    return np.sum(y_pred == y_actual) / len(y_actual)