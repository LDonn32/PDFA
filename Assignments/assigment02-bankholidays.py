# assignment02-bankholidays.py
# Author: Laura Donnelly


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
# see: https://docs.python.org/3/library/stdtypes.html#str.startswith

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
