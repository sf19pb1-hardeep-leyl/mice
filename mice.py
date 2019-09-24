import sys
import csv   #Comma-separated values.  Do not name this Python script csv.py.
import datetime
import urllib.request
import io

#Database is at
#https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j
url = "https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv"

try:
    fileFromUrl = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error, file = sys.stderr)
    sys.exit(1)

sequenceOfBytes = fileFromUrl.read() #Read whole file into one big sequenceOfBytes.
fileFromUrl.close()

try:
    s = sequenceOfBytes.decode("utf-8")    #s is a string
except UnicodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

fileFromString = io.StringIO(s)
lines = csv.reader(fileFromString)   #or lines = csv.reader(s.splitlines())
miceLines = [line for line in lines if line[9] == "Evidence of mice or live mice present in facility's food and/or non-food areas. "]
fileFromString.close()
# Will continue to work on this to sort and find the restaurant(s) with the most mice violations in the city!
