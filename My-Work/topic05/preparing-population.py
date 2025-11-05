# Preparing the population data for analysis
# The CSO data is quite clean 
# All we realy have to do is group it
# Author: Laura Donnelly

# Replace column remove string - Pandas.replace() method documentation.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html


# Pivot table - Pandas pivot_table() method documentation.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html

import pandas as pd 

FILENAME="cso-populationbyage.csv"
DATADIR= r"C:/Users/laura/Documents/GitHub/PDFA/My-Work/data/"
FULLPATH =  DATADIR + FILENAME

df = pd.read_csv(FULLPATH)


'''

drop_col_list = ["Statistic Label","CensusYear","Sex","UNIT"]
df.drop(columns=drop_col_list, inplace=True)

df  = df[df["Single Year of Age"] != "All ages"]
df["Single Year of Age"] = df["Single Year of Age"].str.replace('Under 1 year', '0')
df["Single Year of Age"] = df["Single Year of Age"].str.replace('\D', '', regex=True)
df['Single Year of Age']=df['Single Year of Age'].astype('int64')

df_anal = pd.pivot_table(df, 'VALUE',"Single Year of Age","Administrative Counties")

print (df_anal.head(10))
df_anal.to_csv("population_for_analysis.csv")
'''

'''

print (df.info())
df.to_csv("population_for_analysis.csv")

'''


drop_col_list = ["Statistic Label","CensusYear","Sex","UNIT"]
#df = df.drop(columns=drop_col_list)
df.drop(columns=drop_col_list, inplace=True)

df = df[df["Single Year of Age"] != "All ages"]
df["Single Year of Age"] = df["Single Year of Age"].str.replace('Under 1 year', '0')
df["Single Year of Age"] = df["Single Year of Age"].str.replace('\D', '', regex=True)

df['Single Year of Age']=df['Single Year of Age'].astype('int64')

#df_anal =pd.crosstab(df.loc[:, 'Administrative Counties'], df.loc[:, 'Single Year of Age'])
df_anal = pd.pivot_table(df, 'VALUE',"Single Year of Age","Administrative Counties")
print (df_anal.head(10))
df_anal.to_csv("population_for_analysis.csv")


