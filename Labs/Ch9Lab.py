'''
Chapter 9 Lab - Yahtzee
Raven Rothkopf
'''

import random
done = False
yahtzees = 0

def yahtzee_roll():
    roll_list = []
    for i in range(5):
        roll_list.append(random.randrange(1, 7))
    return roll_list

print(yahtzee_roll())

def create_list(size):
    roll_list = []
    for i in range(100000):
        roll_list.append(yahtzee_roll())
    return roll_list

def is_yahtzee(roll_list):
    if roll_list[0:5] == [6, 6, 6, 6, 6]:
        print("You got a Yahtzee!")
        return True
    if roll_list[0:5] == [5, 5, 5, 5, 5]:
        print("You got a Yahtzee!")
        return True
    if roll_list[0:5] == [4, 4, 4, 4, 4]:
        print("You got a Yahtzee!")
        return True
    if roll_list[0:5] == [3, 3, 3, 3, 3]:
        print("You got a Yahtzee!")
        return True
    if roll_list[0:5] == [2, 2, 2, 2, 2]:
        print("You got a Yahtzee!")
        return True
    if roll_list[0:5] == [1, 1, 1, 1, 1]:
        print("You got a Yahtzee!")
        return True
    else:
        return False

roll_list = create_list(100000)
for roll in roll_list:
    if is_yahtzee(roll) == True:
        yahtzees += 1

print()
print("There are", yahtzees, "yahtzees.")
print("Out of 100,000 rolls,", str(float((yahtzees / len(roll_list)) * 100)) + "% of them are Yahtzees!")













