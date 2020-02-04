# Chapter 3 Lab - Make Your Own Quiz
score = 0
print("\nHow well do YOU know Python? Take this very official quiz to find out.")


print("\nQuestion 1: ")
print("When was Python created?\n\tA. The 1970s \n\tB. The 1980s \n\tC. The 1990s \n\tD. The 2000s")
answer_1 = input("Your answer: ")
if answer_1.upper() == "B" or answer_1.upper() == "THE 1980S":
    print("\nCorrect, keep it up!")
    score += 1
else:
    print("\nSorry, the answer was B!")


print("\nQuestion 2: ")
print("What did Guido Van Rossum name Python after?\n\tA. The reptile \n\tB. His favorite childhood toy \n\tC. Monty Python \n\tD. The Greedy Python by Eric Carle")
answer_2 = input("Your answer: ")
if answer_2.upper() == "C" or answer_2.upper() == "MONTY PYTHON":
    print("\nCorrect, you are good at this!")
    score += 1
else:
    print("\nSorry, the answer was C!")


print("\nQuestion 3: ")
print("What nationality is Python's creator?\n\tA. Swiss \n\tB. French \n\tC. German \n\tD. Dutch")
answer_3 = input("Your answer: ")
if answer_3.upper() == "D" or answer_3.upper() == "DUTCH":
    print("\nCorrect, you are on a roll!")
    score += 1
else:
    print("\nSorry, the answer was D!")


print("\nQuestion 4: ")
print("True or False: Python is the most popular language taught in British primary schools, surpassing French!")
answer_4 = input("Your answer: ")
if answer_4.upper() == "TRUE" or answer_4.upper() == "T":
    print("\nCorrect, you're almost done!")
    score += 1
else:
    print("\nSorry, it's a true statement!")


print("\nQuestion 5: ")
print("What is the world's biggest python? \n\tA. The Reticulated Python \n\tB. The Royal Python \n\tC. The Burmese Python \n\tD. The Anthill Python")
answer_5 = input("Your answer: ")
if answer_5.upper() == "A" or answer_5.upper() == "THE RETICULATED PYTHON" or answer_5.upper() == "RETICULATED PYTHON":
    print("\nCorrect! This python can stretch to a record breaking 30 FEET fully grown. Can you believe it?")
    score += 1
elif answer_5.upper() == "D":
    print("\nIncorrect! The Anthill Python is actually the world's smallest python, measuring a mere 20 inches. The name gives it away, don't you think?")
else:
    print("\nSorry, the answer was A!")


final_score = (score / 5) * 100
print("\nYou got", score , "out of 5 correct and scored a", str(score / 5 * 100) + "%")
if 80 <= final_score <= 100:
    print("Congratulations, you are a certified Python expert!")
elif 0 <= final_score <= 60:
    print("You should really study up on your Python knowledge!")
else:
    print("You passed, but your Python knowledge could use some extra practice!")

