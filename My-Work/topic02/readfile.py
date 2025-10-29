# a program that reads a file and takes
# Author: Laura Donnelly


FILENAME="numbers.txt"
DATADIR= "../data/"
FULLPATH =  DATADIR + FILENAME

#print (FULLPATH)

with open (FULLPATH, "rt") as fp:
    for line in fp:

        # use strip to remove whitespace
        # https://www.freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line/
        print (f" {line.strip()} ", end="")
        print( f"has lenght {len(line)}")
      




       