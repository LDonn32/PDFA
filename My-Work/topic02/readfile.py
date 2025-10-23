# a program that reads a file and takes
# Author: Laura Donnelly


FILENAME="numbers.txt"
DATADIR= "../../data/"
FULLPATH =  DATADIR + FILENAME

#print (FULLPATH)

with open (FULLPATH, "rt") as fp:
    total = 0
    for line in fp:
        #print (f" {line.strip()} ", end="")
        #print( f"has lenght {len(line)}")
        total += int(line)
    print (total)






       