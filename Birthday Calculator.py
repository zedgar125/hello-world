# Edgar Zuniga 1861071
from math import floor   # imported date due to years showing decimals after calculations
from datetime import date

current_month = int(input("Enter the current month: "))
current_day = int(input("Enter the current day: "))
current_year = int(input("Enter the current year: "))
birth_month = int(input("Enter the month of birth: "))
birth_day = int(input("Enter the day of birth: "))
birth_year = int(input("Enter the year of birth: "))

c_dm = current_month, current_day  # puts current month and day together to compare with birth month and day
b_dm = birth_month, birth_day
c_date = date(current_year, current_month, current_day)  # formats to a yyyy - mm - dd
b_date = date(birth_year, birth_month, birth_day)

age_time = c_date - b_date  # calculates time and days between dates
age_year = floor(age_time.days / 365)  # calculates the number of years and rounds down the decimal

print()
print('Birthday Calculator')
print()
print('Current day')
print('Day:', current_day, "\nMonth:", current_month, "\nYear:", current_year)
print()
print('Birthday')
print('Day:', birth_day, "\nMonth:", birth_month, "\nYear:", birth_year)
if c_dm == b_dm:                 # if month and day are equal, Happy Birthday will print
    print("Happy Birthday!")
print("You are", age_year,  "years old.")
print("hello world")
