# program showing how to read csv from a url using Pandas
# Author: Laura Donnelly

import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=wind_speed_10m,rain&past_days=3&forecast_days=1&format=csv"

# location in datafram starts at 0
df = pd.read_csv(url, header= 2)
print (df.head(3))
print (df.info())
