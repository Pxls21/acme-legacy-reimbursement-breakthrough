#!/usr/bin/env python3
import json
import joblib
import numpy as np
import os

# Load the trained decision tree
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'decision_tree_model.pkl')
tree = joblib.load(model_path)

# Load test cases
with open('public_cases.json', 'r') as f:
    data = json.load(f)

print(f"Generating answers for {len(data)} cases...")

answers = []
for i, case in enumerate(data):
    days = case['input']['trip_duration_days']
    miles = case['input']['miles_traveled']
    receipts = case['input']['total_receipts_amount']
    
    # Make prediction using decision tree
    X = np.array([[days, miles, receipts]])
    prediction = float(tree.predict(X)[0])
    answers.append(prediction)
    
    if (i+1) % 100 == 0:
        print(f"Progress: {i+1}/{len(data)}")

# Write answers to file
with open('answers.txt', 'w') as f:
    for answer in answers:
        f.write(f"{answer}\n")

print(f"✅ Generated answers.txt with {len(answers)} predictions!")
print(f"First few answers: {answers[:5]}")
print(f"Last few answers: {answers[-5:]}") 