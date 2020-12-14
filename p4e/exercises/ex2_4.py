"""
Exercise 5: Write a program which prompts the user for a Celsius tem-
perature, convert the temperature to Fahrenheit, and print out the
converted temperature.
"""

# prompt for celcius
celsius = int(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
print("The temperature in fahrenheit is ",fahrenheit)
