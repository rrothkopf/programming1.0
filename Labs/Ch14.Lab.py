# Hangman game

# setup your game by doing the following:

# make a word list for your game
# grab a random word from your list and store it as a variable

# in a loop, do the following:

# display the hangman using the gallows
# display the used letters so the user knows what has been selected
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all correct letters, tell the user they won

# ask if they want to play again import random

import random
import pygame

gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]

word_list = ["ARTICHOKE", "AGLET", "QUORUM"]
word = word_list.pop(random.randrange(len(word_list)))

done = False
print("Welcome to Hangman! Guess the word I am thinking of correctly, or let a stick man meet his end.")
used_letters = []
fails = 0
correct = False

while not done:
    if correct:
        print("You've figured out the word, congratulations!")
        print(gallows[0])
        done = True

    print(gallows[fails])
    used_letters.sort()
    correct = True

    for letter in word:
        if letter.upper() in used_letters:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")
            correct = False
    print()
    print()
    
    print("Used Letters:", end=" ")
    for letter in used_letters:
        print(letter, end=" ")
    print()

    answer = input("Guess a letter:").upper()
    if answer in used_letters:
        print("You've already guessed that letter!")



    elif answer not in word:
        used_letters.append(answer.upper())
        fails += 1
        print("That letter isn't in the word.")

    elif answer in word:
        used_letters.append(answer.upper())
        print("You guessed correctly! Keep it up.")
        print(answer, end=" ")

    else:
        print("That's not a letter, silly!")

    if fails >= 6:
        print("You've run out of guesses! Game over :(")
        print(gallows[6])
        done = True

    if done is True:
        answer2 = input("Do you want to play again with another word?").upper()
        if answer2 == "YES" or answer2 == "Y":
            print("Welcome to Hangman (AGAIN)! Guess the word I am thinking of correctly, or let a stick man meet his end.")
            used_letters = []
            fails = 0
            word = word_list.pop(random.randrange(len(word_list)))
            done = False
        else:
            print("See you later!")


