"""
Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
   Score    Grade
>= 0.9       A
>= 0.8       B
>= 0.7       C
>= 0.6       D
< 0.6        F
"""

# function to calculate grade based on score given as parameter
def computegrade(score):
    if score > 1.0 or score < 0.0:
        print("Score out of range")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")

# prompt for score input and call function computegrade
try:
    score = float(input("Enter a score between 0.0 and 1.0: "))
    computegrade(score)
except:
    print("Bad score")
