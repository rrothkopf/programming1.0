'''
Chapter 1 Problem Set (18pts)

Instructions:  For each of the following, enter your answer below the numbered problem.  
Ensure the code runs properly without errors, and make sure your file executes before you submit it!

If a single problem is not working properly, please comment it out of your code. 
If a question is commented out, it will receive partial credit.  
Non working or broken code will not receive any credit for that problem.

This code currently is broken in many places.  It will not run until you fix it.
If you want to work on an individual problem, copy and paste it into another tab, or just copy and paste it into the python shell to see if it works.
'''

######################################

# Problem 1 (1pt)
# Write a line of code that will print the name of the creator of Python. (look it up)
import math

print("Guido van Rossum")

######################################

# Problem 2 (1pt)
# Print the result of 2 divided by 3
print(2 / 3)
# Then print the result of 2 floor 3
print(2 // 3)

######################################

# Problem 3 (1pt)
# Calculate the average of 4.6, 8.2, and 2.1.  Print the result.
x = 4.6 + 8.2 + 2.1
y = x / 3
print(y)

######################################

# Problem 4 (1pt)
# Correct the following code (make it work).

A = 22
print(A)

######################################

# Problem 5 (3pt)
# Comment out all of the variable names below which ARE NOT ALLOWED in Python?
# Use a double hashtag ## to comment out variable names that are NOT allowed.
# Some variable names are ALLOWED, but are IMPROPER.  For those names, comment them out with single hashtag #.
# If a name is proper, leave it uncommented.

apple = 1
#Apple = 2
APPLE = 3
#Apple2 = 4
##1Apple = 5
##account number = 6
account_number = 7
##account.number = 8
# accountNumber = 9
##account# = 10
pi = 11
PI = 12
fred = 13
#Fred = 14   # Can't be capitalized
# GreatBigVariable = 15
# greatBigVariable = 16
great_big_variable = 17
##great.big.variable = 18
##2x = 19
x2x = 20
##total% = 21

######################################

# Problem 6 (1pt)
# Fix the following code:

x = 45
print(x)

######################################

# Problem 7 (1pt)
# This program should calculate the area of a circle
# Something is preventing it from working.  Check the error and fix the code.
import math
radius = float(input("Radius:"))
area = math.pi * (radius ** 2)
print(area)
######################################

# Problem 8 (1pt)
# The code below works, but is improper.
# Correct the THIRD line of code below to show the BETTER way to write it.  (Ch1 - 1.7.1 Operator Spacing)

x = 4
y = 5
a = (x * 2) * (y + 3)  # fix me!
print(a)

######################################

# Problem 9 (1pt)
# Fix the following code:

x = 4
y = 5
a = 3 * (x + y)
print(a)

######################################

# Problem 10 (1pt)
# Fix the mistake in the following line of code.
# It should ask the user for input, and assign it to the variable age as an integer.

age = int(input("Enter your age:"))

######################################

# Problem 11 (1pt)
# Write a SINGLE LINE of Python code that will use escape codes to print one double-quote followed by your name on a new line.
'''
Example run:
"
Bob
'''

print("\"" "\nraven")

######################################

# Problem 12 (1pt)
# The code below will print the number 3.
# Change the denominator to make the modulo operation print the number 4 instead.

print(13 % 9)

######################################

# Problem 13 (1pt)
# The following floor operator will give the result of 2.
# Change ONLY the denominator of this floor division so it prints 4.
print(13 // 3)

######################################

# Problem 14 (1pt)
# Change ONLY the second line of the code below so that one is added to the variable x.  The number 4 should be printed.

x = 3
x = x + 1  # change this line only
print(x)

######################################

# Problem 15 (1pt)
# Correct the following code:

user_name = input("Enter your name: ")
print("Hello", user_name)

######################################

# Problem 16 (1pt)
# Correct the following code:
value = int(input("Enter your year of birth:"))
print("You turn", 2019 - value, "this year!")

# WHEN YOU COMPLETE THIS PROBLEM SET, DO NOT FORGET TO COMMIT AND PUSH
# YOUR FILE BACK TO THE REPOSITORY.
