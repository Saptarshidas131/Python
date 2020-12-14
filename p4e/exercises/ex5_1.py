"""
Exercise 1: Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.
"""
# initialising variables
total = 0
count = 0
average = 0

# infinite loop
while True:
    # input as string
    inp = input("Enter a number, type done to end: ")
    # if input is done then print and break out of loop
    if inp == "done":
        print("\ndone")
        print("total = ",total)
        print("count = ",count)
        average = total/count
        print("average = ",average)
        break
    # otherwise convert input to number, calculate total,average and increment count
    else:
        try:
            num = int(inp)
            total = num + total
            count = count + 1
        # if input is not a number print error message and continue
        except:
            print("Invalid input, must input a number")
            continue
        
