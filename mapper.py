#!/usr/bin/env python3
import sys

def parse_line(line):
    # Strip whitespace and split by tabs
    fields = line.strip().split(',')
    # Skip header or any invalid lines
    if len(fields) == 5 and fields[0] != 'index':
        try:
            min_temp = float(fields[2])  # Min Temp is the third column (index 2)
            max_temp = float(fields[3])  # Max Temp is the fourth column (index 3)
            return min_temp, max_temp
        except ValueError:
            return None, None  # Skip if temperature values can't be converted to float
    return None, None

for line in sys.stdin:
    min_temp, max_temp = parse_line(line)
    if min_temp is not None and max_temp is not None:
        print(f"min_temp\t{min_temp}")
        print(f"max_temp\t{max_temp}")
