# code snippets for lectures
# Author: Laura Donnelly


import pandas as pd
# up two levels past topic04 and then down into data

# was having issues with relative paths, so added this to check current working directory.

'''
import os
print("Current working directory:", os.getcwd())

# this was code from lecture, but it wasn't working for me (despite same file path working in other files), so I hard coded the path below.
FILENAME= "people-100-dirty.csv"
DATADIR= "../Data/"

'''

FILENAME= "people-100-dirty.csv"
DATADIR = r"C:\Users\laura\Documents\Github\PDFA\My-Work\Data\\"


df= pd.read_csv(DATADIR + FILENAME)

# Detect missing values
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Fill missing values
df.fillna(value='default_value', inplace=True)

# drop duplicate rows
# df.drop_duplicates(inplace=True)
df.to_csv( "temp_file.csv")
