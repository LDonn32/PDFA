# In this lab we are going to use Python to make some regression graphs

# Getting started

# 1. write a program that loads the seaborn tips data
# and prints out the top 5 rows (ie the head)

import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
dataset = sns.load_dataset('tips')

print (dataset.head)

# 2. Modify the script produce a regression plot for the tips against the total bill

import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
dataset = sns.load_dataset('tips')

# the for debugging
# print(dataset.head())
sns.set_style('whitegrid')
sns.lmplot(x='total_bill', y='tip', order=1, data=dataset)

# plt.show()

# 3. Mess around with this to produce a different plot

sns.set_style('whitegrid')
sns.regplot(x='total_bill', y='tip', order=1, data=dataset)

# plt.show()

sns.set_style('whitegrid')
sns.residplot(x='total_bill', y='tip', order=1, color= 'blue', data=dataset)

# plt.show()

# A bit more on regression.

# 4. Make plot using discrete values for example tips against size

sns.lmplot(x="size",y="tip", data=dataset)

# 5. Put in a jitter to make it easier to see

sns.lmplot(x="size", y="tip", data=dataset, x_jitter=.05)

# 6. Instead of dots use an estimator to estimate the mean for each size

import numpy as np
sns.set_style('whitegrid')
sns.lmplot(x="size", y="tip", data=dataset, x_estimator=np.mean)
# plt.show()