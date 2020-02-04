'''
Chapter 10 Lab - Controls
Raven Rothkopf
11/14/2019
'''

import pygame
pygame.init()

# Define some variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (128, 158, 224)

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
done = False  # condition for game loop

# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Raven's Game")
pygame.mouse.set_visible(False)

# Loop until the user clicks the close button.

# Used to manage how fast the screen updates
clock = pygame.time.Clock()  # creates a clock object that manages updates

car_x = 0
car_y = 0

player_x = 0
player_y = 0

change_x = 0
change_y = 0

car_color = RED

def draw_car(x, y, car_color):
    pygame.draw.rect(screen, BLACK, [x + 10, y, 10, 5], 1)  # windows
    pygame.draw.rect(screen, car_color, [x + 5, y, 6, 5])  # windows
    pygame.draw.ellipse(screen, BLACK, [x + 2, y + 6, 9, 9], 3)  # wheel
    pygame.draw.ellipse(screen, BLACK, [x + 18, y + 6, 9, 9], 3)  # wheel
    pygame.draw.rect(screen, car_color, [x, y + 4, 30, 5])  # body

def draw_player(x, y, color):
    x -= 7
    y -= 15
    pygame.draw.ellipse(screen, BLACK, [10 + x, 15 + y, 5, 5])  # player's head
    pygame.draw.line(screen, BLACK, [12 + x, 15 + y], [12 + x, 25 + y])  # player's body
    pygame.draw.line(screen, BLACK, [12 + x, 25 + y], [15 + x, 35 + y])  # right leg
    pygame.draw.line(screen, BLACK, [12 + x, 25 + y], [9 + x, 35 + y])  # left leg
    pygame.draw.line(screen, BLACK, [12 + x, 18 + y], [17 + x, 26 + y])  # right arm
    pygame.draw.line(screen, BLACK, [12 + x, 18 + y], [7 + x, 26 + y])  # left arm

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard or controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_x = 3
            elif event.key == pygame.K_LEFT:
                change_x = -3
            elif event.key == pygame.K_DOWN:
                change_y = 3
            elif event.key == pygame.K_UP:
                change_y = -3
            elif event.key == pygame.K_r:
                car_color = RED
            elif event.key == pygame.K_b:
                car_color = BLUE
        elif event.type == pygame.KEYUP:  # lift finger off key
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                change_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                change_y = 0



    # --- Game logic should go here

    # PLAYER CONTROLS
    player_x, player_y = pygame.mouse.get_pos()
    if player_x > SCREEN_WIDTH - 11:
        player_x = SCREEN_WIDTH - 11
    if player_y > SCREEN_HEIGHT - 21:
        player_y = SCREEN_HEIGHT - 21

    # CAR CONTROLS
    car_x += change_x
    car_y += change_y

    if car_x > SCREEN_WIDTH - 30:
        car_x = SCREEN_WIDTH - 30
    if car_y > SCREEN_HEIGHT - 15:
        car_y = SCREEN_HEIGHT - 15
    if car_y < 0:
        car_y = 0
    if car_x < 0:
        car_x = 0

    # ---- Drawing code goes here
    screen.fill(WHITE)
    draw_car(car_x, car_y, car_color)
    draw_player(player_x, player_y, 0)

    pygame.display.flip()  # updates the screen

    # --- Limit to 60 frames per second
    clock.tick(60) # frames per second

# Close the window and quit.
pygame.quit()