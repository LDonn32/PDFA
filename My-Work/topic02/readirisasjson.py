# Reads in the iris data set as json
# Author: Laura Donnelly

import json

FILENAME="iris.json"
DATADIR= "../data/"
FULLPATH =  DATADIR + FILENAME

with open (FULLPATH, "rt") as fp:
    irisdataset = json.load(fp)
    print (irisdataset[0])