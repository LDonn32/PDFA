# Topic 07 lab 01

# Author: Laura Donnelly

# In this lab i want to see if there is any relation between the windspeed and the month in knock

# I am going to use the dataset

# "https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv"


# Get the data

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Look at the csv file and realise that the first 19 lines do not contain data, so we need to skip them

df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv", skiprows=19)
print(df.head(3))

# 2. Is there any correlation between the mean temperature and the month.
# The answer is no... but that is for a number of reasons (why do you think)

corrtemp = df["month"].corr(df["meant"])
print(corrtemp)

# Tidy the wind data

# 3. If you look at the data you will see that there are some windspeeds missing, we need to drop those rows
# lets make a new dataset which only has the month and the windspeed

cleandf = df[["month","wdsp"]]

# 4. Great, now lets drop the NAs

# cleandf.dropna(inplace=True)

# pandas doe not recognise the "as an NA so I am converting them to na before droping them

cleandf['wdsp']= cleandf.loc[:,('wdsp')].replace(' ', np.nan)
cleandf.dropna(inplace=True)

# 5. now we just need top convert the wind speed to floats

cleandf['wdsp'] = cleandf['wdsp'].astype(float)

# Now we can analyse

# 6. Is there a Correlation

corrwind = cleandf["month"].corr(cleandf["wdsp"])
print (f"wind correlation {corrwind}")

# 7. no there does not seem to be, that is strange let's do some regression

sns.set_style('whitegrid')
# sns.scatrterplot(x='total_bill, y='tip',data=dataset)
sns.lmplot(x='month',y='wdsp',order=3,data=cleandf)
plt.show()