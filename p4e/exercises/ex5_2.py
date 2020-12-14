"""
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
"""
# initialising variables to None
maximum = None
minimum = None

# infinite loop
while True:
    # input
    inp = input("Enter a number, type done to end:")
    # if input is done then take print maximum and minimum and break out of loop 
    if inp == "done":
        print("\ndone")
        print("maximum = ",maximum)
        print("minimum = ",minimum)
        break
    # otherwise calculate maximum and minimum
    else:
        try:
            num = int(inp)
            if minimum == None:
                minimum = num
            elif num<minimum:
                minimum = num
            if maximum == None:
                maximum = num
            elif num>maximum:
                maximum = num
        # if input is not a number
        except:
            print("Invalid input, enter number")
            continue
