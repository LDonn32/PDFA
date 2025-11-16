# Log Files

# Author: Laura Donnelly

# The next series of tasks is to create a 
# regresasion plot for the amount of data
# that was transferred for each hour of the day
# Using the data from the access.logs file

# 1. Write a function to read in the strings
# It should strip off the firsts and last characters

def parse_str(x):
    return x[1:-1]

# 2. Write a function to read in the date in the 
# format it is in the log file
# it will also need to strip the first
# and last characters (ie the [])

import datetime

def parse_datetime(x):

    dt= datetime.strptime(x[1:-1], '%d/%d/%Y:%H:%M:%S')
    return dt

# 3. Read in the log file into a dataframe,
# remember the columns in the log file are.
['ip', 'time', 'request', 'status', 'size', 'referer', 'user_agent']

# We will not need columns 10r2(they are blank), and remember to assign the parsing 
# functions for each column.
# The delimiator in this code looks
# like a scary regular expression.

import pandas as pd

df= pd.read_csv('data/access.log',sep=r'\s(?=(?:[^"]*"[^"]*")*$)(?![^\[]*\])',engine='python',
                na_values='-',
                header=None,
                usecols=[0, 3, 4, 5, 6, 7, 8],
                names=['ip', 'time', 'request', 'status', 'size', 'referer', 'user_agent'],
                converters={'time': parse_datetime,
                            'request': parse_str,
                            'status': int,
                            'size':int,
                            'referer': parse_str,
                            'user_agent': parse_str})

# 4. You can check that it was all read in correctly by either 
# printing out the head () of the data frame
# or by storing the dataframe into an excel and looking at it.

excelFilename = './data/log.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')

# 5. NOTE you can manipulate the columns to get extract data
# from them e.g. you could get more info about the URI and URL
# (But this is not needed for this excerise)

request = df.pop('request').str.split()
df['resource'] = request.str[1]
df['method'] = request.str[0]

# yes i could have used regex for this 
# from the request get the string before the ?

df['url'] = request.str[1].str.split('?').str[0]

# 6. Ok now lets make another dataframe that store the sums
# of all the data transferred for each hour(H)

dfbyhour=df.resample('H', on='time').sum()

# 7. you should inspect this dataframe, you will see the 
# index has time periods 

df.info
