import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns




# Load the Shannon airport dataset.

shannon = pd.read_csv("data/dly518.csv", parse_dates=["date"], index_col='date', skiprows=24,low_memory=False, date_format='%d-%b-%Y %H:%M')

# load the Dublin airport dataset.

dublin = pd.read_csv("data/dly532.csv", parse_dates=["date"], index_col='date', skiprows=25, low_memory=False, date_format='%d-%b-%Y %H:%M')

# Load the Cork airport dataset.

cork = pd.read_csv("data/dly3904.csv", parse_dates=["date"], index_col='date', skiprows=24,low_memory=False, date_format='%d-%b-%Y %H:%M')


# Load the Knock airport dataset.

knock = pd.read_csv("data/dly4935.csv", parse_dates=["date"], index_col='date', skiprows=24, low_memory=False, date_format='%d-%b-%Y %H:%M')



# Replace blank spaces with NaN values.
# See: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html

shannon.replace(to_replace=' ', value=np.nan, inplace=True)

# Check.

# shannon.head()

dublin.replace(to_replace=' ', value=np.nan, inplace=True)
# dublin.head()

cork.replace(to_replace=' ', value=np.nan, inplace=True)
# cork.head() 

knock.replace(to_replace=' ', value=np.nan, inplace=True)
# knock.head()






