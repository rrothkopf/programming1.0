'''
Chapter 04 Problem Set (21pts))

Instructions:  For each of the following, enter your answer below the numbered problem.
Ensure the code runs properly without errors. Make sure your file executes before you submit it!

If a single problem is not working properly, please comment it out of your code.
If a question is commented out, it will receive partial credit.
Non working or broken code will not receive any credit for that problem.
'''

#################################
# Problem 1 (2pts)
# Write a Python program that will use a for loop to print your name 6 times on separate lines,
# and then the word "Done" on the last line.
i = 1
while i <= 6:
    print("Francis")
    i += 1
print("Done!")

'''
Sample Run:

Francis
Francis
Francis
Francis
Francis
Francis
Done
'''

#################################
#  Problem 2 (2pts)
# Write a Python program that will use a for loops to print your first name 3 times and then your last name 3 times.
# Repeat this pattern (3 first followed by 3 lasts) 10 times using nested for loops.
n = 1
while n <= 10:
    for i in range(3):
        print("Raven")
    for j in range(3):
        print("Rothkopf")
    n += 1

'''
Sample Run

Francis
Francis 
Francis
Parker 
Parker
Parker
(Above is repeated 10 times)
'''

#################################
#  Problem 3 (Multiples of seven - 2pts)
#  Write a Python program that will use a for loop to print multiples of seven from 21 to 63. (63 must be included)
for i in range(21, 64, 7):
    print(i)

#################################
#  Problem 4 (Countdown - 2pts)
#  Write a Python program that will use a WHILE LOOP to count from 10 down to 1.
#  Then print the words "Blast off!" Remember, this time we will use a WHILE LOOP, don't use a FOR loop.
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Blast off!")

#################################
#  Problem 5 (Random ints - 2pts)
#  Write a program that prints a random integer from 1 to 20.
#  Put it in a loop so that it prints a random integer 20 times
import random
i = 1
while i <= 20:
    print(random.randrange(1, 21))
    i += 1

'''
Sample Run
4
12
15
9
10
1
18
4
13
3
'''

###########################
#  Problem 6 (Random floats - 2pts)
#  Write a program that prints a random floating point number somewhere between 1 and 5 (inclusive).
#  Do not make the mistake of generating a random number from 0 to 5 instead of 1 to 5.
#  Put it in a loop to print a different random float 10 times.
i = 1
while i <= 10:
    print(random.random() * 4 + 1)
    i += 1

'''
Sample Run
2.987862719820445
1.870129734673759
4.434092587298322
4.929302003474453
2.0609415060503515
3.428599151662887
1.715550409049674
1.083673547723635
3.917120042736795
2.982349679748726
'''

#################################
#  Problem 7 (Coin Flipper - 4pts)
'''  
Make a Coin flipper: 
    * Start by creating a program that will print a random 0 or 1.
    * Then, instead of 0 or 1, print heads or tails (use an IF statement to check the random number)
    * Add a loop so that the program does this 100 times.
    * Print the total number of heads flipped, and the number of tails. (make variables to track each)

If done properly, you will likely have around half heads and half tails.
'''
heads = 1
tails = 0
i = 1
while i <= 99:
    answer = (random.randrange(0, 2))
    if answer == 1:
        print("heads")
        heads += 1
    else:
        print("tails")
        tails += 1
    i += 1
print("\nnumber of heads: ", heads, "\nnumber of tails: ", tails)

#################################
#  Problem 8 (Rock Paper Scissors - 5pts)
'''
Write a program that plays rock, paper, scissors:

    * Start by creating a program that randomly prints 0, 1, or 2.
    * Improve the program so it randomly prints rock, paper, or scissors using if statements.
    Don't select from a list, as shown in the chapter.  This random selection will be the computer's choice.
    * Add to the program so it first asks the user their choice.(It might be easier if you have them enter a number instead of rock, paper, or scissors. See sample run)
    * Add conditional statement to figure out who wins and print back the result to the user.
    * Make your game behave like the sample run.  
'''

'''
Sample run:

Welcome to rock paper scissors:

Enter your choice (0 for rock, 1 for paper, or 2 for scissors): 1

Player chooses paper.
Computer chooses rock.

Congratulations, you win!
'''
# Foundation
done = False
import random

computer = random.randrange(0, 3)
print("Let's play rock paper scissors!")

while not done:

    # Player choice
    player = int(input("Choose your player: \n(type 0 for rock, 1 for paper, or 2 for scissors)"))
    if player == 0:
        print("\n\tPlayer chooses rock")
    elif player == 1:
        print("\n\tPlayer chooses paper")
    elif player == 2:
        print("\n\tPlayer chooses scissors")

    # Computer choice
    if computer == 0:
        print("\tComputer chooses rock")
    elif computer == 1:
        print("\tComputer chooses paper")
    elif computer == 2:
        print("\tComputer chooses scissors")

    # Results
    if computer == player:
        print("\nWe tied!")
    elif computer == 0 and player == 1:
        print("\nCongratulations, you won!")
    elif computer == 0 and player == 2:
        print("\nI beat you this time!")
    elif computer == 1 and player == 0:
        print("\nI beat you this time!")
    elif computer == 1 and player == 2:
        print("\nCongratulations, you won!")
    elif computer == 2 and player == 0:
        print("\nCongratulations, you won!")
    elif computer == 2 and player == 1:
        print("\nI beat you this time!")

    # Loop
    answer = input("\nRematch?")
    if answer.upper() == "NO" or answer.upper() == "N":
        done = True
        print("Thanks for playing!")

# Before submissiion, check your variable names, spacing, and make sure your full code runs.
