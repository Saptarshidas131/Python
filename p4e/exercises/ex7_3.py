"""
Exercise 3: Sometimes when programmers get bored or want to have a
bit of fun, they add a harmless Easter Egg to their program. Modify
the program that prompts the user for the file name so that it prints a
funny message when the user types in the exact file name “na na boo
boo”. The program should behave normally for all other files which
exist and don’t exist. Here is a sample execution of the program:
"""

def findconfidence(string):
    find_colon = string.find(':')
    num = float(string[find_colon+1:])
    return num

def calc_confidence():
    count = 0
    total = 0
    filename = input("Enter a filename: ")
    if filename == "na na boo boo":
        print("NA NA BOO BOO - You have been punk'd")
        exit()
    # try opening a file
    try:
        fh = open(filename)
    # if file not found print error message and exit
    except:
        print("Invalid file ",filename)
        exit()
    text = 'X-DSPAM-Confidence:'
    for line in fh:
        if line.startswith(text):
            confidence = findconfidence(line)
            total = confidence + total
            count = count+1
    average = total/count
    print("Average spam confidence is ",average)
calc_confidence()
