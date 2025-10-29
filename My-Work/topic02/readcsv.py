# A program that reads a file and takes
# Author: Laura Donnelly


# import csv to read csv files and process the data.
import csv

FILENAME="students.csv"
DATADIR= "../data/"
FULLPATH =  DATADIR + FILENAME

with open (FULLPATH, "rt") as fp:
    #for line in fp:
        #print(line, end="")

# nonnumeric will convert numeric values to floats (removes quotes) (reminder floats are numbers with decimal points)

    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0

    # for if statement remember if the integer value is 0 it is false, any other number is true
    # so if the line number is 0 it is false
    # it will only do the header row if it is 
    linenumber = 0
    for line in reader:
        if linenumber: # this is not the header (line 0)
        # print (line)
            total += int(line[1]) # the ages have quoes so are read in as strings
        else: # this is the header row
            print (line)    
        linenumber += 1

    print(total)