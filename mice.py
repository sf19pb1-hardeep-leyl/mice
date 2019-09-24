"""
restaurant.py
Find restaurants with mice violations. Will work on this some more to find the resturant(s) with the most mice violations
"""

import sys
import csv   #Comma-separated values.  Do not name this Python script csv.py.

filename = "/Users/student/Documents/DOHMH_New_York_City_Restaurant_Inspection_Results.csv"

try:
    csvfile = open(filename)
except FileNotFoundError:
    print(f'Sorry, could not find file "{filename}".', file = sys.stderr)
    sys.exit(1)
except PermissionError:
    print(f'Sorry, no permission to open file "{filename}".', file = sys.stderr)
    sys.exit(1)

lines = csv.reader(csvfile)

for line in lines:              #During each iteration, line is a list of strings.
    if line[11] == "Evidence of mice or live mice present in facility's food and/or non-food areas.":   
        print(line[1], line[8]) #name and inspection date
        print(line[11])         #violation description
        print()

csvfile.close()
sys.exit(0)
