# Lab Topic 02- Representing Data.
# Author: Laura Donnelly


#1. Create a CSV file called data.csv. 
# Saved in the data directory.


#2.Write a program that reads in the data and outputs each line as list.
import csv

FILENAME="data.csv"
DATADIR= "../data/"


'''

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print (line)

'''

#3. Modify the program to deal with the header line seperately.
'''
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linenumber = 0
    for line in reader:
        if not linenumber: # first row is header row
            print (f"{line}\n----------------")
        else: # all subsequent rows
            print (line)
               
        linenumber += 1
'''

#4. Modify the prorgam to calculate the average age.
# There are a few ways to solve this;

#a. Convert the string that is read into an integer.

'''
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    total = 0
    linenumber = 0
    for line in reader:
        if not linenumber: # first row is header row
            pass
        else: # all subsequent rows
            total += int(line[1]) # why 1 ? age is the second column (which is 1 in the index)
        linenumber += 1
    print(f"Average age is {total/(linenumber-1)}") # why -1? minus 1 to not count header row
    '''

#b. Use the quote parameter to read in the numbers as floats.
'''
with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp,delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row is header row
            pass
        else: # all subsequent rows
            total += line[1] # age is the second column (which is 1 in the index)
        linecount += 1
    print(f"Average age is {total/(linecount-1)}") # why -1? minus 1 to not count header row
    '''

#5. The CVS file could of course have been read in as a Dictionary Object.
# Using DictReader from the csv module.

'''
with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    count = 0
    total = 0
    for line in reader:
        # line is now a dictionary object
        total += line['age'] # age is the second column (which is 1 in the index)
        count += 1
    print(f"Average age is {total/count}") # why is there no -1? DictReader automatically skips the header row
    '''

# Read JSON from internet

#6. Copy this URL into your brower and see the JSON it returns.
# https://www.gov.uk/bank-holidays.json

#7. Write a program tp print this JSOn to the console.

import requests

'''
url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print (data)
'''
# is this a JSON or a Dict object that is outputted? 
# It is a Dict object because JSON is converted to Dict when read into Python.

#8. Modify the program to only outputy the first holiday in northern Ireland.

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print (data['northern-ireland']['events'][0])