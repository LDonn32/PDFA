# assignment02-bankholidays.py
# Author: Laura Donnelly

# Write a program called assignment02-bankholdiays.py

# The program should print out the dates of the bank holidays that happen in 
# # Northern Ireland.

# Last few marks (ie this is more tricky)

# Modify the program to print the bank holidays that are unique to northern Ireland 
# # (i.e. do not happen elsewhere in the UK) you can choose if you want to use 
# the name or the date of the holiday to decide if it is unique.


'''
#Manual way to do it using lists and tuples by just looking up the BHs at - https://www.gov.uk/bank-holidays#northern-ireland:~:text=calendar%20(ICS%2C%2014KB)-,Past%20bank%20holidays%20in%20Northern%20Ireland,New%20Year%E2%80%99s%20Day,-Past%20bank%20holidays

# Define a function that returns a list of tuples containing the date and name of each bank holiday in Northern Ireland for 2025.
def ni_bank_holidays_2025():

# return function.

    return [
        ("2025-01-01", "New Year’s Day"),
        ("2025-03-17", "St Patrick’s Day"),
        ("2025-04-18", "Good Friday"),
        ("2025-04-21", "Easter Monday"),
        ("2025-05-05", "Early May Bank Holiday"),
        ("2025-05-26", "Spring Bank Holiday"),
        ("2025-07-14", "Battle of the Boyne / Orangemen’s Day (substitute)"),
        ("2025-08-25", "Summer Bank Holiday"),
        ("2025-12-25", "Christmas Day"),
        ("2025-12-26", "Boxing Day"),
    ]
# Main program
def main():
    holidays = ni_bank_holidays_2025()
    # Print the dates.
    print("Northern Ireland Bank Holidays in 2025:")
    # Use a for loop to print each holiday on a new line.
    for date_str, name in holidays:
        print(f"  {date_str} — {name}")

# Directly call main() so the program runs automatically
main()

'''


'''
# https://www.tutorialspoint.com/python-holidays-library
# https://pypi.org/project/holidays/

# Import date time
from datetime import date

# importing holidays module
import holidays

# getting India holidays
NI_holidays = holidays.NorthernIreland(years=2020)

# iterating over the holidays
for date, occasion in NI_holidays_holidays.items():
   
   # printing date and occasion
   print(f'{date} - {occasion}')

'''

'''
# this is following example code from lab2.0.py on reading CSV files

# Import requests module for HTTP requests.
# https://www.w3schools.com/python/module_requests.asp
import requests

# Define the URL for the UK government bank holiday JSON feed.

# retrieved the json feed by checking the network tab in developer tools on the gov.uk bank holidays page and copying the url for the json file
# https://www.gov.uk/bank-holidays.json

bank_holidays_url = "https://www.gov.uk/bank-holidays.json"

# Send a GET request to the API.
# https://www.w3schools.com/python/ref_requests_get.asp
response = requests.get(bank_holidays_url)

# Convert the response to a Python dictionary.
# https://www.w3schools.com/python/ref_requests_response.asp
data = response.json()

# Pull only the Northern Ireland holidays for 2025
northern_ireland_holidays_2025 = data["northern-ireland"]["events"]

# Print a header. 
# Format the output using f-strings to keep it nice and tidy.
print("Bank Holidays in Northern Ireland:\n")
# print colum titles with formatting to align them
print(f"{'Title':<40} {'Date'}")
print("-" * 55)

# Loop through holidays and print neatly formatted results.
for holiday in northern_ireland_holidays:
    print(f"{holiday['title']:<40} {holiday['date']}")
'''

# Cleaner code below:
# Adds filter for 2025 only


# Import requests module for HTTP requests.
import requests

# Define the URL for the UK government bank holiday JSON feed.
bank_holidays_url = "https://www.gov.uk/bank-holidays.json"

# Send a GET request to the API.
response = requests.get(bank_holidays_url)

# Convert the response to a Python dictionary.
data = response.json()

# Pull Northern Ireland holidays
northern_ireland_holidays = data["northern-ireland"]["events"]

# Filter only 2025 holidays using str.startswith method in a for loop comprehension.
# https://docs.python.org/3/library/stdtypes.html#str.startswith
northern_ireland_holidays_2025 = [
    holiday for holiday in northern_ireland_holidays if holiday["date"].startswith("2025")
]

# Print a header.
print("Bank Holidays in Northern Ireland (2025):\n")
print(f"{'Title':<40} {'Date'}")
print("-" * 55)

# Loop through holidays and print neatly formatted results.
for holiday in northern_ireland_holidays_2025:
    print(f"{holiday['title']:<40} {holiday['date']}")
