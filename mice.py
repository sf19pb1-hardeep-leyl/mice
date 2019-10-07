"""
List the CAMIS number, name, and number of mouse violations
of the 10 restaurants with the largest number of mouse violations.
"""

import sys
import csv  #Comma-Separated Values
import urllib.request
import collections

#Database is at
#https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j
url = "https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv"

try:
    fileFromUrl = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

sequenceOfBytes = fileFromUrl.read() #Slurp whole file into one big sequenceOfBytes.
fileFromUrl.close()

try:
    s = sequenceOfBytes.decode("utf-8")    #s is a string
except UnicodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

lines = csv.reader(s.splitlines())   #lines is a list of lists

#Two dictionaries that let you look up a CAMIS number and find the corresponding ...
dba = {}                                   #name of the restaurant
numberOfViolations = collections.Counter() #number of mice violations for that restaurant

for line in lines:                     #line is a list of 26 strings
    if "Evidence of mice or live mice present in facility's food and/or non-food areas." in line[11]:
        camis = int(line[0])           #the id number of the restaurant
        dba[camis] = line[1]           #Record the name of this restaurant.
        numberOfViolations[camis] += 1 #Tally an additional violation.  Automatically starts at 0.

for camis, n in numberOfViolations.most_common(10): #the 10 worst offenders, starting with the worst
    print(f"{camis:8} {n:2} {dba[camis]}")

sys.exit(0)
