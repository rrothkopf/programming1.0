'''
Chapter 4 Lab
Raven Rothkopf
9/30/19
'''

print("Welcome to Voyage! You are a sailor out on the sea in search of adventure. \nNot long ago, you saw a storm brewing far behind you and knew your boat was too small to survive it! \nChoose your actions wisely to get back to dry land, who knows what you might discover along the way?")
# variables
done = False  # condition for game loop
player_position = 0
thirst = 0
boat_damage = 0
storm_position = -20
drinks = 3
import random

# Answer options /
while not done:
    print("\nRemember, choose carefully!")
    print("A. Sail ahead at full speed.")
    print("B. Sail ahead at moderate speed.")
    print("C. Quench your thirst.")
    print("D. Drop your anchor for the night and repair your boat.")
    print("E. Status check.")
    print("Q. Quit.")
    print()
    answer = input("Enter your choice: ")

    if answer.upper() == "Q":
        done = True
        print("Thanks for playing!")
    elif answer.upper() == "A":
        print("You sailed ahead at full speed.")

        position_1 = random.randrange(8, 11)
        player_position += position_1
        print("You traveled", position_1, "knots.")

        boat_damage += random.randrange(2, 4)
        storm_position += random.randrange(4, 8)
        thirst += 1
    elif answer.upper() == "B":
        print("You sailed ahead at moderate speed.")

        position_2 = random.randrange(5, 7)
        player_position += position_2
        print("You traveled", position_2, "knots.")

        boat_damage += random.randrange(1, 2)
        storm_position += random.randrange(7, 10)
        thirst += 1
    elif answer.upper() == "C":
        if drinks > 0:
            print("You quenched your thirst.")
            thirst = 0
            drinks -= 1
        elif drinks <= 0:
            print("Your bottle is empty!")
    elif answer.upper() == "D":
        print("You dropped your anchor for the night. You also repaired the damages to your boat, looking good as new!")
        storm_position += random.randrange(9, 11)
        boat_damage = 0
    elif answer.upper() == "E":
        print("Status Update:")
        print("Total knots traveled: ", player_position)
        print("Drinks left in your bottle: ", drinks)
        print("Storm is", player_position - storm_position, "knots behind you!")

    if thirst >= 5 and done == False:
        print("\nYou died of thirst!")
        print("Game over :(")
        done = True
    elif thirst == 3 or thirst == 4 and done == False:
        print("You are getting thirsty!")

    if boat_damage >= 9 and done == False:
        print("\nYour boat is too damaged to continue! You capsize and sink.")
        print("Game over :(")
        done = True
    if boat_damage == 6 or boat_damage == 7 or boat_damage == 8 and done == False:
        print("Your boat is pretty beat up! You might want to stop and repair it.")

    if storm_position >= player_position and done == False:
        print("\nThe storm caught you!")
        print("Game over :(")
        done = True
    elif player_position - storm_position <= 7 and done == False:
        print("\nThe storm is close!")

# secret island story line
    if random.randrange(20) == 4 and done == False and (answer == "A" or answer == "B" or answer == "C"):
        print("\nYou stumble upon a secret island! You quench your thirst, refill your bottle and repair your boat.")
        thirst = 0
        drinks = 3
        boat_damage = 0

    if random.randrange(75) == 6 and done == False and (answer == "A" or answer == "B" or answer == "C"):
        print("\nOh no! A water vortex opened up and swallowed you and your boat, you died.")
        print("Game over :(")
        done = False

    if player_position >= 100 and done == False:
        print("\nYou made it on to dry land safe and sound! Can't say the same for your boat.")
        print("Congratulations! Thank you for playing.")
        answer1 = input("Would you like to play again?")
        if answer1.upper() == "YES" or answer1.upper() == "Y":
            done = False
            player_position = 0
            thirst = 0
            boat_damage = 0
            storm_position = -20
            drinks = 3
            print("\n\nWelcome to Voyage! You are a sailor out on the sea in search of adventure. \nNot long ago, you saw a storm brewing far behind you and knew your boat was too small to survive it! \nChoose your actions wisely to get back to dry land, who knows what you might discover along the way?")
        if answer1.upper() == "NO" or answer1.upper() == "N":
            done = True