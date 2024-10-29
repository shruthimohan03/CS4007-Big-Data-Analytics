#!/usr/bin/env python3
import sys

min_temp = float('inf')
max_temp = float('-inf')

for line in sys.stdin:
    try:
        key, value = line.strip().split('\t')
        temperature = float(value)
        if key == 'min_temp':
            if temperature < min_temp:
                min_temp = temperature
        elif key == 'max_temp':
            if temperature > max_temp:
                max_temp = temperature
    except ValueError:
        continue  # Skip lines with invalid data

if min_temp != float('inf') and max_temp != float('-inf'):
    print(f"Minimum Temperature: {min_temp}")
    print(f"Maximum Temperature: {max_temp}")
else:
    print("No valid temperature data found.")
