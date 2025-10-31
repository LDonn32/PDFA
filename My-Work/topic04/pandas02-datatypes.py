# code snippets for lectures
# Author: Andrew Beatty

import pandas as pd


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

print(df.info())

df['Date of birth'] = pd.to_datetime(df['Date of birth'])
#df['numeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')

print (df.info())

#standardise data
df['Email'] = df['Email'].str.lower().str.strip()
print (df.head(5))

# drop unesasary columns
df.drop(columns=['User Id'], inplace=True)

# lastly deal with outliers

#Q1 = df['value'].quantile(0.25)
#Q3 = df['value'].quantile(0.75)
#IQR = Q3 - Q1
#df = df[(df['value'] >= Q1 - 1.5 * IQR) & (df['value'] <= Q3 + 1.5 * IQR)]

df.to_csv( "temp_file.csv")