
# Import necessary libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# read in dataset from the CSO website.
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FY006A/CSV/1.0/en"
df = pd.read_csv(url)

# Inspect the last few rows
df.tail(3)

# Drop columns not being used.
# Using a list to store column names to be dropped.
drop_col_list = [
    'STATISTIC', 'Statistic Label', 'TLIST(A1)',
    'CensusYear', 'C02199V02655', 'C02076V03371',
    'C03789V04537', 'UNIT'
]

# implace=True to make sure changes are saved.
df.drop(columns=drop_col_list, inplace=True) 

# Remove "All ages" category
df = df[df["Single Year of Age"] != "All ages"]

# Replace text and convert "Single Year of Age" to numeric
df['Single Year of Age'] = df['Single Year of Age'].str.replace('Under 1 year', '0')
df['Single Year of Age'] = df['Single Year of Age'].str.replace(r'\D', '', regex=True)

df['Single Year of Age'] = df['Single Year of Age'].astype('int64')
df['VALUE'] = df['VALUE'].astype('int64')

print("Cleaned dataset info:")
df.info()

df_anal = pd.pivot_table(df, 'VALUE',"Single Year of Age","Sex")
print (df_anal.head(3))

# Get the column headers from the pivot table.
headers = list(df_anal.columns)
Both_sexes = headers[0]
Females = headers[1]
Males = headers[2]

# Created variables for each sex category. 
Both_sexes_data = df_anal[Both_sexes]
Females_data = df_anal[Females]
Males_data = df_anal[Males]


# using df_anal[].sum() to get total population.

number_people = df_anal[Both_sexes].sum()
number_people

# print out the dataframe to check 

df_anal

# use numpy to calculate the weighted mean.
# df_anal.index is the age

w_mean = np.average(df_anal.index, weights=df_anal[Both_sexes])
w_mean