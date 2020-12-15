"""
Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print out
the average spam confidence.
"""
def findconfidence(string):
    find_colon = string.find(':')
    num = float(string[find_colon+1:])
    return num

def calc_confidence():
    count = 0
    total = 0
    filename = input("Enter a filename: ")
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
