#Chapter 07 Problem Set (19pts)


# Problem 1
# Create  a list with six values in it.
# Each value will be a different data type: integer, float, string, boolean, list, and tuple
# Set each item in the list to any appropriate value of that type.  (2pts)
my_int = -378
my_float = 4.348
my_str = "Hello World"
my_bool = False
my_list = [0, 0, 200, 100]
my_tuple = (255, 255, 255)

my_list1 = [my_int, my_float, my_str, my_bool, my_list, my_tuple]
print(my_list1)

# Problem 2.
# Using an index for my_list2, print the names Idle and Jones. (1pts)
my_list2 = ["Cleese", "Gilliam", "Idle", "Chapman", "Palin", "Jones"]
print(my_list2[2])
print(my_list2[5])

# Problem 3
# Use a for loop to print each item in my_list3 below. (2pts)
my_list3 = [5, 2, 6, 8, 101]
for i in range(len(my_list3)):
    print(my_list3[i])

# Problem 4
# Use a FOR loop and the append method to generate and add the numbers 1 to 100 to my_list4.
# Then print out the list. (2pts)
my_list4 = []
for i in range(101):
    my_list4.append(i)
print(my_list4)

# Problem 5
# Print the number 1, 2 and 3 using indices for my_list5 below (3pts)
my_list5 = [[38, 11, 66], 2, [5, [43, 3], 7], [1, 90, 7], [4, 10, 33, [30, 77]]]
print(my_list5[3][0])
print(my_list5[1])
print(my_list5[2][1][1])

# Problem 6
# Using the string called "my_text6" below, do the following using string indices: (4pts)

# a. Print the length of my_text6.
# b. Print the letter "z" from my_text6.
# c. Print "The q" from my_text6
# d. Print the text "ox jump" from my_text6.

my_text6 = "The quick brown fox jumped over the lazy dogs."
print(len(my_text6))
print(my_text6[-8])
print(my_text6[:5])
print(my_text6[17:24])

# Problem 7
# Write a loop that will generate ten random integers from 1 to 10 and append them to list7
# Then print the list. (2pts)
import random
my_list7 = []

for i in range(10):
    num = random.randrange(1, 11)
    my_list7.append(num)
print(my_list7)

# Problem 8
# Write a program that counts the number of threes in an array like my_list8.
# Print the number of threes after counting them in the loop. (3pts)


my_list8 = [3, 12, 3, 5, 3, 4, 6, 8, 5, 3, 5]

three = 0
for num in my_list8:
    if num == 3:
        three += 1

print("There are", three, "threes in this array")
