# This is code anonymise the sub domains of ip addresses 
# Author: Laura Donnelly

import re

#regex = "\d{1,3}\.\d{1,3} " # this will find other numbers apart from ips
regex =  "(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}"  # we make a group at the beginning to keep
replacementText="\\1XXX.XXX " # note the space at the end to match above


regex = "\[.*\]"
filename = "smaller-access.log.txt"
datadir = r"C:\Users\laura\Documents\Github\PDFA\My-Work\topic04\data\\"

fullpath = datadir + filename


outputFileName = "anonymisedIPs.txt"

with open(fullpath) as inputFile:
    with open(outputFileName, 'w') as outputFile:
        for line in inputFile:
            # for debugging
            #foundText = re.search(regex, line).group()
            #print(foundText)
            newLine = re.sub(regex, replacementText, line)
            outputFile.write(newLine)