# Chapter 12 Problem Set (21pts)

# 1 Write code to create an INSTANCE of the class below.
#  Use DOT NOTATION to change its three attributes to those of your own pet or one you know and love: (2pts)

class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

my_dog = Dog()
my_dog.age = 2
my_dog.name = "Stella"
my_dog.weight = 60


# 2 Write code to create an INSTANCE of this class
#  Set the name and email attribute by passing the values to the constructor method
#  (that means adding additional parameters to the init method): (2pts)

class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email

person1 = Person("Raven", "rrothkopf@fwparker.org")


# 3 For the code below, create a CLASS with attributes for color, name, and breed.
#  The instance code below will use that class to create a green parrot named Sunny. (2pts)

class Bird():
    def __init__(self, color, name, breed):
        self.color = color
        self.name = name
        self.breed = breed

my_bird = Bird("green", "Sunny", "Parrot")


# 4 The following code has three common errors.  Fix the code. (3pts)

class Person():
    def __init__(self, name):
        self.name = name
        self.money = 0


desmond = Person("Desmond")
desmond.money = 100  # set the money for Desmond to 100 dollars


# 5. This problem has several parts that are all contained in a single program. Make sure that the program satisfies the requirements for each part.

# part A. Write code that defines a class named Animal: (3pts)

class Animal():
    def __init__(self, name):
        print("An animal has been born.")
        self.name = name
    def eat(self):
        print("Munch munch")
    def make_noise(self):
        print("Grr says", self.name)

'''
* Add an attribute for the animal name.
* Add a constructor for the Animal class that prints ''An animal has been born.''
* Add an eat() method for Animal that simply prints ''Munch munch.''
* Add a make_noise() method for Animal that prints ''Grrr says [animal name].''
'''

# part B. Create a class named Cat: (3pts)
'''
* Make Animal the parent class.
* A make_noise() method for Cat that prints ``Meow says [animal name].''
* A constructor for Cat that prints ``A cat has been born.'' and it also calls the parent constructor.
'''

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A cat has been born")
    def make_noise(self):
        print("Meow says", self.name)


# part C.  Create a class named Dog: (3pts)
'''
* Make Animal the parent class.
* A makeNoise() method for Dog that prints ``Bark says [animal name].''
* A constructor for Dog that prints ``A dog has been born.'' and it also calls the parent constructor.
'''

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A dog has been born")
    def make_noise(self):
        print("Bark says", self.name)

# part D.  Make a single program with the following: (3pts)
''' 
* Code that creates instances of a cat, two dogs, and an animal.
* Set the name for each.
* Call the eat() and make_noise() methods for each animal. (Don't forget this part.)
'''

animal = Animal("Bob")
cat = Cat("Leo")
dog1 = Dog("Sparky")
dog2 = Dog("Pup")

dog1.eat()
dog1.make_noise()

dog2.eat()
dog2.make_noise()

cat.eat()
cat.make_noise()

animal.eat()
animal.make_noise()


