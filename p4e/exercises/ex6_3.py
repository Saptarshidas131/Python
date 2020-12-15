"""
Exercise 3: Encapsulate this code in a function named count, and gen-
eralize it so that it accepts the string and the letter as arguments.
"""

def count(string,letter):
    count = 0
    for l in string:
        if l == letter:
            count = count + 1
    print(count)

string_input = input("Enter a string: ")
letter_input = input("Enter a letter: ")
count(string_input,letter_input)
