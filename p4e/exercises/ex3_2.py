"""
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program
"""

# prompt for hours and rate per hour
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    # check for overtime, if hours more than 40 add extra 1.5 times the hours
    if hours > 40:
        pay = (hours * rate) + (hours - 40)*1.5
    # otherwise regular pay
    else:
        pay = hours * rate
        
    print("Pay: " + str(pay))
    
except:
    print("Error, please enter numeric input")
    


