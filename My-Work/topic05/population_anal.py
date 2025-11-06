# analysisng population wrong
# Author: Laura Donnelly

import pandas as pd 

FILENAME="population_for_analysis.csv"
DATADIR= "C:/Users/laura/Documents/GitHub/PDFA/My-Work/topic05/"
FULLPATH =  DATADIR + FILENAME

df = pd.read_csv(FULLPATH)

# print (df.head(3))
headers = df.columns[1:] # gets rid of the first column.
print (headers)
district =headers[0]
print (df[district].describe()) # gives basic descriptive statistics
print(df[district]) # print all the values in the district column