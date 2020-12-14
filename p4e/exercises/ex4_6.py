"""
Exercise 6: Rewrite your pay computation with time-and-a-half for over-
time and create a function called computepay which takes two parameters
(hours and rate).
"""
# function to calculate pay given hours and rate as parameters
def computepay(hours,rate):
    
    # check for overtime, if hours more than 40 add extra 1.5 times the hours
    if hours > 40:
        pay = (hours * rate) + (hours - 40)*1.5
    # otherwise regular pay
    else:
        pay = hours * rate
        
    print("Pay: " + str(pay))
    

# prompt and function calling
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    computepay(hours,rate)
        
except:
    print("Error, please enter numeric input")
