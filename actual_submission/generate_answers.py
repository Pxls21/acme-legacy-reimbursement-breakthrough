#!/usr/bin/env python3
import json
import subprocess

# Load test cases
with open('public_cases.json', 'r') as f:
    data = json.load(f)

print(f"Generating answers for {len(data)} cases...")

answers = []
for i, case in enumerate(data):
    days = case['input']['trip_duration_days']
    miles = case['input']['miles_traveled']
    receipts = case['input']['total_receipts_amount']
    
    # Run the predictor
    result = subprocess.run(['python3', 'decision_tree_predictor.py', str(days), str(miles), str(receipts)], 
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        prediction = float(result.stdout.strip())
        answers.append(prediction)
    else:
        print(f"Error on case {i+1}: {result.stderr}")
        answers.append(0.0)  # fallback
    
    if (i+1) % 100 == 0:
        print(f"Progress: {i+1}/{len(data)}")

# Write answers to file
with open('answers.txt', 'w') as f:
    for answer in answers:
        f.write(f"{answer}\n")

print(f"✅ Generated answers.txt with {len(answers)} predictions!") 