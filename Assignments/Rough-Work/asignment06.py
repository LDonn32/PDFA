# assignment_6_Weather.ipynb
# rough work 
# Author: Laura Donnelly

# Imports libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates # maybe not use this will see

sns.set(style="whitegrid") # causing error go back to plt plot maybe



#  Load data 
url = "https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv"
# skip the metadata at the top
df = pd.read_csv(url, skiprows=23)

# Quick inspect
print('Columns:', df.columns.tolist())
print('\nFirst 5 rows:')
print(df.head())

# pParse datetime and set index
# The file usually has a 'date' column like 'DD-MMM-YYYY HH:MM'. Use dayfirst and coerce errors to catch parsing issues.
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
# drop rows where date failed to parse
df = df.dropna(subset=['date']).copy()
# set index
df = df.set_index('date').sort_index()

print('\nDate range:', df.index.min(), 'to', df.index.max())

# Temperature: hourly time series (full range)
if 'temp' not in df.columns:
    raise ValueError("No 'temp' column found in the data. Check column names printed above.")

plt.figure(figsize=(14,5))
ax = sns.lineplot(data=df, x=df.index, y='temp')
ax.set_title('Hourly Temperature (Full Date Range)')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (°C)')
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(mdates.AutoDateLocator()))
plt.tight_layout()
plt.show()




'''
#  Daily mean temperature
daily_mean = df['temp'].resample('D').mean()
print('\nDaily mean sample:')
print(daily_mean.head())

plt.figure(figsize=(14,5))
ax = sns.lineplot(x=daily_mean.index, y=daily_mean.values, marker='o')
ax.set_title('Daily Mean Temperature (Full Date Range)')
ax.set_xlabel('Date')
ax.set_ylabel('Mean Temperature (°C)')
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(mdates.AutoDateLocator()))
plt.tight_layout()
plt.show()

'''

# Plot the daily mean.

plt.figure(figsize=(18,6))

# daily_mean is a DataFrame with 'date' and 'temp' columns
sns.lineplot(data=daily_mean, x='date', y='temp',)
plt.title('Daily Mean Temperature')
plt.xlabel("Date")
plt.ylabel("Mean Temperature (°C)")
plt.show()


'''

#  Monthly mean temperature
monthly_mean = df['temp'].resample('M').mean()
print('\nMonthly mean sample:')
print(monthly_mean.head())

plt.figure(figsize=(12,5))
ax = sns.lineplot(x=monthly_mean.index, y=monthly_mean.values, marker='o')
ax.set_title('Monthly Mean Temperature')
ax.set_xlabel('Month')
ax.set_ylabel('Monthly Mean Temperature (°C)')
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(mdates.AutoDateLocator()))
plt.tight_layout()
plt.show()
'''

# Compute monthly mean temperature.

monthly_mean = (df.set_index('date').resample('M')['temp'].mean().reset_index())

# Take a look at the monthly mean before plotting.
print(monthly_mean)


# Plot the monthly mean. 
plt.figure(figsize=(14,5))
sns.lineplot(x=monthly_mean['date'], y=monthly_mean['temp'], marker='o')
plt.title('Monthly Mean Temperature')
plt.xlabel("Month")
plt.ylabel("Monthly Mean Temperature (°C)")
plt.tight_layout()
plt.show()




# Second Part on Windspeed the last 40%

# Print all column names to find which one reflects windspeed
print("Columns in the dataset:")
print(df.columns)

# After checking the columns outputted, manually set the windspeed column name.
wcol = 'wdsp'   

print("Using windspeed column:", wcol)

# Convert windspeed column to numeric.
# see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html 
df[wcol] = pd.to_numeric(
    df[wcol].astype(str).str.replace(',', '.', regex=False), # replace commas with dots
    errors='coerce'
)


# Plot raw windspeed 

# code not working hewre need to trouble shoot .... too messy on the plots find way to make labels neater.


# Rolling windspeed (24-hour rolling average)
# If data are hourly, use window=24. If not exactly hourly, this still gives a rolling window of 24 samples.
rolling_window = 24
rolling_wind = df[wcol].rolling(window=rolling_window, min_periods=1).mean()

plt.figure(figsize=(14,5))
ax = sns.lineplot(x=rolling_wind.index, y=rolling_wind.values)
ax.set_title(f'{rolling_window}-Sample Rolling Mean of {wcol}')
ax.set_xlabel('Date')
ax.set_ylabel(f'Rolling mean {wcol}')
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(mdates.AutoDateLocator()))
plt.tight_layout()
plt.show()

#  Daily max windspeed
daily_max_wind = df[wcol].resample('D').max()
print('\nDaily max wind sample:')
print(daily_max_wind.head())

plt.figure(figsize=(14,5))
ax = sns.lineplot(x=daily_max_wind.index, y=daily_max_wind.values, marker='o')
ax.set_title('Daily Maximum Windspeed')
ax.set_xlabel('Date')
ax.set_ylabel(f'Daily max {wcol}')
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(mdates.AutoDateLocator()))
plt.tight_layout()
plt.show()

# Monthly mean of daily max windspeeds
monthly_mean_daily_max = daily_max_wind.resample('M').mean()
print('\nMonthly mean of daily max windspeeds:')
print(monthly_mean_daily_max.head())

plt.figure(figsize=(12,5))
ax = sns.lineplot(x=monthly_mean_daily_max.index, y=monthly_mean_daily_max.values, marker='o')
ax.set_title('Monthly Mean of Daily Maximum Windspeeds')
ax.set_xlabel('Month')
ax.set_ylabel(f'Monthly mean of daily max {wcol}')
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(mdates.AutoDateLocator()))
plt.tight_layout()
plt.show()

