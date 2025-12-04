'''
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

'''

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
drop_col_list = [
    'STATISTIC', 'Statistic Label', 'TLIST(A1)',
    'CensusYear', 'C02199V02655', 'C02076V03371',
    'C03789V04537', 'UNIT'
]
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

# Pivot into age x sex table (rows=age, cols=Sex, values=VALUE)
df_anal = pd.pivot_table(df, 'VALUE', "Single Year of Age", "Sex")
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

# use numpy to calculate the weighted mean of both sexes.
weighted_mean_Both_sexes = np.average(df_anal.index, weights=df_anal[Both_sexes])
weighted_mean_Both_sexes

# df_anal.index.astype(int) to convert index to integer for ages. 
ages = df_anal.index.astype(int)

# use numpy.average() to calculate the weighted mean for males and females, separately.
weighted_mean_male = np.average(ages, weights=df_anal[Males])
weighted_mean_female = np.average(ages, weights=df_anal[Females])

print(f"Weighted mean age (Males): {weighted_mean_male:.2f}")
print(f"Weighted mean age (Females): {weighted_mean_female:.2f}")

# Calculate the difference between Females and Males by age.
df_anal['Difference'] = df_anal[Females] - df_anal[Males]

# Take a look at the first 3 rows to check. 
df_anal['Difference'].head(3)

# Print the difference in male and female population.
df_male_total = df_anal[Males].sum()
df_female_total = df_anal[Females].sum()   

# abs() to get absolute value of difference.
df_difference = abs(df_female_total - df_male_total)

print(f"Absolute difference between female and male population: {df_difference:,.0f}")

# Get the average age for females
weighted_mean_female = np.average(df_anal.index, weights=df_anal['Female'])

weighted_mean_female

# get the average age for males
weighted_mean_male = np.average(df_anal.index, weights=df_anal['Male'])
weighted_mean_male  

# Visualize the difference between male and female population using a bar chart.
bar_width = 0.50
ages_numeric = df_anal.index.astype(int)
plt.figure(figsize=(14, 6))
plt.bar(ages_numeric, df_anal['Difference']) 
plt.axhline(0, color='black', linewidth=0.8)
plt.xlabel('Age')
plt.ylabel('Female - Male')
plt.title('Population difference by single year of age (Female minus Male)')
plt.show()


# look at part 2
# looking at 35 age group


target_age = 35
lower_bound = target_age - 5
upper_bound = target_age + 5
print(f"Age group: {lower_bound} to {upper_bound}")

# Filter the pivot table df_anal for this age range
age_group_df = df_anal.loc[(df_anal.index >= lower_bound) & (df_anal.index <= upper_bound)]
age_group_df

# Totals in the age band
total_males_ageband = age_group_df[Males].sum()
total_females_ageband = age_group_df[Females].sum()
sex_difference_ageband = total_females_ageband - total_males_ageband

print(f"Total males (age {lower_bound}-{upper_bound}): {total_males_ageband:,}")
print(f"Total females (age {lower_bound}-{upper_bound}): {total_females_ageband:,}")
print(f"Population difference (F - M): {sex_difference_ageband:,}")


# look at part 3
# region with largest sex difference in that age band


# Filter original df for the age band
df_ageband = df[(df["Single Year of Age"] >= lower_bound) &
                (df["Single Year of Age"] <= upper_bound)]

# Group by Region and Sex, sum population for each
region_sex_group = df_ageband.groupby(["Region", "Sex"])["VALUE"].sum().unstack()

# Calculate difference by region (Female - Male)
region_sex_group["Difference"] = region_sex_group["Female"] - region_sex_group["Male"]

# Region with the largest absolute difference
max_diff_region = region_sex_group["Difference"].abs().idxmax()
max_diff_value = region_sex_group.loc[max_diff_region, "Difference"]

print(f"Region with largest sex difference (age {lower_bound}-{upper_bound}): {max_diff_region}")
print(f"Difference (F - M): {max_diff_value:,}")

region_sex_group
