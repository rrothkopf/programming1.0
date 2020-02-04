'''
Chapter 12 Lab - Classes
Raven Rothkopf
12/5/19

This code creates rectangles and ellipses at random locations, with random colors and dimensions that bounce off the screen,
'''

import pygame
import random
pygame.init()  # vroom vroom

# Define some variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# CLASSES
class Rectangle():
    def __init__(self):
        self.x = random.randrange(701)
        self.y = random.randrange(501)
        self.color = (random.randrange(256), random.randrange(256), random.randrange(256))
        self.height = random.randrange(21, 71)
        self.width = random.randrange(21, 71)
        self.change_x = random.randrange(-2, 4)
        self.change_y = random.randrange(-2, 4)
    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])
    def update(self):

        # shapes bounce off in the x
        self.x += self.change_x
        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
            self.change_x *= -1
        if self.x < 0:
            self.x = 0
            self.change_x *= -1

        # shapes bounce off in the y
        self.y += self.change_y
        if self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.change_y *= -1
        if self.y < 0:
            self.y = 0
            self.change_y *= -1

# Defines Rectangle() as the parent class, creates an ellipse as the child class
class Ellipse(Rectangle):
    def draw(self):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.width, self.height])

# duplicates shapes
my_list = []
for i in range(500):
    my_object = Rectangle()
    my_list.append(my_object)

    my_object2 = Ellipse()
    my_list.append(my_object2)


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # condition for game loop

# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Raven's Game")

# Loop until the user clicks the close button.

# Used to manage how fast the screen updates
clock = pygame.time.Clock()  # creates a clock object that manages updates

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard or controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # ---- Drawing code goes here
    screen.fill(WHITE)

    for my_object in my_list:
        my_object.draw()

    for my_object in my_list:
        my_object.update()

    pygame.display.flip()  # updates the screen

    # --- Limit to 60 frames per second
    clock.tick(60) # frames per second

# Close the window and quit.
pygame.quit()