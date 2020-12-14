"""
Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
"""

# prompt for hours and rate per hour
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# check for overtime, if hours more than 40 add extra 1.5 times the hours
if hours > 40:
    pay = (hours * rate) + (hours - 40)*1.5
# otherwise regular pay
else:
    pay = hours * rate
    
print("Pay: " + str(pay))

