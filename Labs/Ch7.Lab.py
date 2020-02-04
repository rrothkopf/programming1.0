'''
Chapter 7 Lab - Lights Out
Raven Rothkopf
10/22/19
'''

import random
print("Welcome to Lights Out! Your goal is to flip the switches to try to turn all of the lights off,\nBUT every time you turn off a light, the surrounding two turn on!\n Good luck!")

lights = []
for j in range(10):
    num = random.randrange(2)
    if num == 0:
        lights.append("X")
    if num == 1:
        lights.append("O")
done = False

while not done:
    for i in range(10):
        print(i, end=" ")
    print()
    for x in range(len(lights)):
        print(lights[x], end=" ")

    flip = int(input("\nFlip a switch (0 to 9): "))
    if flip == 0:
        if lights[0] == "X":
            lights[0] = "O"
        elif lights[0] == "O":
            lights[0] = "X"
        if lights[1] == "X":
            lights[1] = "O"
        elif lights[1] == "O":
            lights[1] = "X"

    if flip == 9:
        if lights[9] == "X":
            lights[9] = "O"
        elif lights[9] == "O":
            lights[9] = "X"
        if lights[8] == "X":
            lights[8] = "O"
        elif lights[8] == "O":
            lights[8] = "X"

    if flip > 0 and flip < 9:
        if lights[flip] == "X":
            lights[flip] = "O"
        elif lights[flip] == "O":
            lights[flip] = "X"

        if lights[flip + 1] == "X":
            lights[flip + 1] = "O"
        elif lights[flip + 1] == "O":
            lights[flip + 1] = "X"

        if lights[flip - 1] == "X":
            lights[flip - 1] = "O"
        elif lights[flip - 1] == "O":
            lights[flip - 1] = "X"

    if lights[0:10] == ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]:
        print()
        for i in range(10):
            print(i, end=" ")
        print()
        for x in range(len(lights)):
            print(lights[x], end=" ")
        print("\nCongratulations, you shut all of the lights off! \nThanks for playing Lights Out!")
        done = True


