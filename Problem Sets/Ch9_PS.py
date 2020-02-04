# Chapter 09 Problem Set - FUNCTIONS are FUN! (17pts)
'''
Section 1 of 3...
For the code below, GIVE A PREDICTION for what it will output. Then run
the code and state if your prediction was accurate or not. If your prediction
is incorrect, make a quick note of the difference.  More importantly, make sure you understand how and why it differed.
'''

# This section is worth 3 points.

print("Problem # 1")
'''
I think this will print...
Problem # 1
3

It actually printed...
Problem # 1
3 
'''
y = 3

def f1(x):
    print(y)


f1(5)

print("Problem # 2")
'''
I think this will print...
Problem # 2
4

It actually printed...
Problem # 2
3 
'''


def f2(x):
    x = x + 1

x = 3
f2(x)
print(x)


print("Problem # 3")
'''
I think this will print... 
Problem # 3
4

It actually printed...
Problem # 3
4
'''

def f3(x):
    x = x + 1
    print(x)


x = 3
f3(x)


print("Problem # 4")
'''
I think this will print...
Problem # 4
4

It actually printed...
Problem # 4
4
None
'''

def f4(x):
    z = x + 1
    print(z)


x = 3
x = f4(x)
print(x)

print("Problem # 5")
'''
WARNING.  COMMENT OUT THIS ONE AFTER YOU ANSWER AND TRY IT
I think this will print...
Problem # 5
f start
g start
f end
g end

It actually printed...
an on going loop of 
f start
g start


def f():
    print("f start")
    g()
    print("f end")


def g():
    print("g start")
    f()
    print("g end")


f()
'''

print("Problem # 6")
'''
I think this will print...
Problem # 6
2 4

It actually printed...
Problem # 6
4
'''


def spam(x):
    y = x - 1
    x = x + 1
    return y, x


answer = spam(3)
print(answer[1])



#############################################################################################
# Section 2 of 3                                                                            #
# This next section involves finding the mistakes in the code.                              #
# Videos at the end of the chapter can help with these problems if you need an explanation. #
# This section is worth 6 points.                                                           #
#############################################################################################


# Problem 7 (1pt)
# Correct the following code: (Don't let it print out the word `None')
# Only change the function.  Do not change the call to the function.


def find_sum(a, b, c):
    x = a + b + c
    return x

print(find_sum(10, 11, 12))



# Problem 8 (1pt)
# Correct the following code: (x should increase by one, but it doesn't.)
# The correct solution involves capturing and use the returned value from the function.

def increase(x):
    return x + 1


x = 10
print("x is", x, " I will now increase x.")
increase(x)
print("x is now", increase(x))



# Problem 9
# Correct the following code (1pt)

def print_hello():
    print("Hello")


print_hello()

# Problem 10
# Correct the following code (1pt)
print("Problem #10")

def count_to_ten():
    for i in range(1, 11):
        print(i)


count_to_ten()



# Problem 11
# There are two things wrong with this one
# Correct the following code (1pt)

def sum_list(my_list):
    for i in my_list:
        return sum(my_list)


favorite_numbers = [45, 2, 10, -5, 100]
print(sum_list(favorite_numbers))



# Problem #12 (1pts)
# Correct the following code: (This almost reverses the string. What is wrong?)
# Think about how reverse indices work.

def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(1, text_length + 1):
        result = result + text[i * -1]
    return result


text = "Programming is the coolest thing ever."
print(reverse(text))




############################################################################
#  Section 3 of 3                                                          #
#  (8 pts) For this section, write code that satisfies each description    #
#  Make sure that you both write AND call the function you create.         #
############################################################################


# Problem # 13 (2pts)
# WRITE AND CALL a function that takes in two parameters.
# The first parameter will be a string named phrase.
# The second parameter will be a number named count.
# Print phrase to the screen count times.
# (e.g., the function takes in "Hello" and 5, then prints "Hello" five times.)
def f3():
    phrase = input("Enter phrase: ")
    count = int(input("Enter count: "))
    for i in range(count):
        print(phrase)

f3()


# Problem # 14 (2pts)
# WRITE AND CALL a function that takes in a number, and returns the square of that number.
# Note, this function should RETURN the answer, not print it out.
def f4(number):
    answer = number ** 2
    return answer

print(f4(5))


# Problem # 15 (2pts)
# WRITE AND CALL a function that will take two numbers as parameters
# and RETURN their product AND sum as a tuple.
def f5(x, y):
    product = x * y
    sum = x + y
    return product, sum

print(f5(10, 20))

# Problem # 16 (2pts)
# WRITE AND CALL  a function that takes three numbers as parameters,
# and returns the centrifugal force.
# The formula for centrifugal force is: F=mv^2/r
# (F is centrifugal force, m is mass, r is radius, and v is angular velocity.)

def f6():
    m = float(input("Enter Mass: "))
    r = float(input("Enter Radius: "))
    v = float(input('Enter Angular Velocity: '))
    return m * (v ** 2) / r

print("The centrifugal force is" , f6(), "newtons")



