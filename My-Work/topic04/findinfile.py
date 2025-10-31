# This code will find some text in an access file
# Author: Laura Donnelly


from os import replace
import re

regex = "\[.*\]"
filename = "smaller-access.log.txt"
datadir = r"C:\Users\laura\Documents\Github\PDFA\My-Work\topic04\data\\"

fullpath = datadir + filename

with open(fullpath) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        if (len(foundTextList)!= 0):
            #print(foundTextList)

            foundText = foundTextList[0]
            # print(foundText)

            # if I did not want the [] at the beginning and end
            # print(foundText[1:-1])

            # could also try slicing to remove first and last character
            # print(foundText[1:len(foundText)-1])

            # or could use strip
            # print(foundText.strip("[0-9:/]"))

            # could also use replace to replace unwanted characters with the character X
            # print(foundText.replace("[0-9:/]", "X"))

            # seems to be putting them in brackets, want them replaced with X
            # try this again later





