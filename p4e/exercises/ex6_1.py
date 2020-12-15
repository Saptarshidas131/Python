"""
Exercise 1: Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.
"""

# input
inp = input("Enter a string: ")
# set index to length - 1
index = len(inp)-1
# indexing and printing backwards
while index >= 0:
    print(inp[index],end="")
    index = index - 1
#print(inp[::-1])
    
