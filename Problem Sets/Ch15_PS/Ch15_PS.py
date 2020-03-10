'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

'''file = open("../Searching/Dictionary.txt")
word_list = []

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        word_list.append(word)

length_number = []
length_list = []

for word in word_list:
    length = len(word)
    length_number.append(length)
    length_number.sort()
    if length == length_number[0]:
        length_list.append(word)
print("The longest word in the dictionary is:", length_list[0]) '''

# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"

# TOTAL WORD COUNT
aliceinwonderland = open("../Ch15_PS/AliceInWonderland.py")
a_word_list = []

for line in aliceinwonderland:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        a_word_list.append(word)

print("There are", len(a_word_list), "words in the book Alice In Wonderland!")

# AVERAGE WORD LENGTH
word_length = [len(word) for word in a_word_list]

print("The average length of a word in the book Alice in Wonderland is", (sum(word_length))/len(a_word_list))

# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
alice_list = []
for word in a_word_list:
    if word.upper() == "ALICE":
        alice_list.append(word)

print("The name Alice appears", len(alice_list), "times.")

# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
seven_letter_word = []
for word in a_word_list:
    if len(word) == 7:
        seven_letter_word.append(word)

repeated_words = []
frequency_list = []

for word in seven_letter_word:
    frequency = seven_letter_word.count(word)
    repeated_words.append(frequency)
    repeated_words.sort()
    if frequency == repeated_words[-1]:
        frequency_list.append(word)

print("The most frequently occurring seven letter word in Alice In Wonderland is:", frequency_list[-1].upper())


# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
