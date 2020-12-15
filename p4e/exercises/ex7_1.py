"""
Exercise 1: Write a program to read through a file and print the contents
of the file (line by line) all in upper case. Executing the program will
look as follows:
"""

filename = input("Enter filename: ")
# try opening file
try:
    fileh = open(filename)
except:
    print("Invalid filename ",filename)
    exit()
# reading filedata
#data = fileh.read()
# reading data line by line and printing in uppercase
for line in fileh:
    print(line.strip().upper())
    
