#!/usr/bin/env python
import sys
import joblib
import numpy as np
import os

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'decision_tree_model.pkl')

# Load the trained decision tree
tree = joblib.load(model_path)

def predict(days, miles, receipts):
    X = np.array([[days, miles, receipts]])
    return float(tree.predict(X)[0])

if __name__ == "__main__":
    days = int(sys.argv[1])
    miles = float(sys.argv[2])
    receipts = float(sys.argv[3])
    print(predict(days, miles, receipts))
