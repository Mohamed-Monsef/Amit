import numpy as np
from data import get_data
from perceptron import update_weights, update_bias, predict_proba
from eval import get_accuracy

# Setup
x_train, x_test, y_train, y_test = get_data()
weights = np.zeros(x_train.shape[1])
bias = 0
lr = 0.01

# Training Loop
for i in range(1000):
    probs = predict_proba(x_train, weights, bias)
    weights = update_weights(weights, x_train, probs, y_train, lr)
    bias = update_bias(bias, probs, y_train, lr)

# Final Eval
test_probs = predict_proba(x_test, weights, bias)
y_pred = [1 if p > 0.5 else 0 for p in test_probs]
print(f"Test Accuracy: {get_accuracy(y_pred, y_test)}")
