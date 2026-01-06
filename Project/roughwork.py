import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Maybe use these later
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from statsmodels.tsa.arima.model import ARIMA



# Load datasets.

df = pd.read_csv("dly532.csv")

# check

df.head(15)


# clean data and load again in df.
df=pd.read_csv("dly532.csv", skiprows=25, parse_dates=['date'], dayfirst=True, low_memory=False)

# check
df.head(5)


