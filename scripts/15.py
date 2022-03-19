#use of date format
from datetime import date

current_date = date.today()

print("Today is : %d-%d-%d" % (current_date.day, current_date.month, current_date.year))

custom_date = date(2022, 1, 28)
print("The Date is: ",custom_date)