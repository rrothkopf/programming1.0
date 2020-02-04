'''
Chapter 11 Lab
Raven Rothkopf
'''

import pygame
pygame.init()  # vroom vroom

# Define some variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 626
SCREEN_HEIGHT = 626
done = False  # condition for game loop

# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Raven's Game")

# Loop until the user clicks the close button.

# Used to manage how fast the screen updates
clock = pygame.time.Clock()  # creates a clock object that manages updates

pygame.mouse.set_visible(False)

# Images
bg_image = pygame.image.load("sunsetlake.jpg")
bird_up = pygame.image.load("bird1.gif")
bird_down = pygame.image.load("bird2.gif")
bird_image = bird_down
cloud_image = pygame.image.load("clouds2.png")
cloud1_image = pygame.image.load("clouds.png")
cloud2_image = pygame.image.load("clouds1.png")

# Sounds
bird_sound = pygame.mixer.Sound("Birds.ogg")
bird_sound.play()

bird_flap = pygame.mixer.Sound("Bird Flap.wav")
bird_flap.set_volume(.2)

bird_call = pygame.mixer.Sound("Bird Call.wav")
bird_call.set_volume(.1)

wind = pygame.mixer.Sound("wind.ogg")
wind.set_volume(.2)
wind.play(-1)

# Controls
bird_x = 0
bird_y = 0

cloud_x = 0
change_x = .5

cloud1_x = 0
change1_x = -.5

cloud2_x = 300
change2_x = .2

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard or controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEMOTION:
            if event.rel[1] >= 0:
                bird_image = bird_up
            else:
                bird_image = bird_down
                bird_flap.play(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird_call.play(0)

    cloud_x += change_x
    if cloud_x > SCREEN_WIDTH:
        cloud_x = -300

    cloud1_x += change1_x
    if cloud1_x < -300:
        cloud1_x = 650

    cloud2_x += change2_x
    if cloud2_x > SCREEN_WIDTH:
        cloud2_x = -170

    # --- Game logic should go here
    bird_x, bird_y = pygame.mouse.get_pos()
    if bird_x > SCREEN_WIDTH - 125:
        bird_x = SCREEN_WIDTH - 125
    if bird_y > SCREEN_HEIGHT - 75:
        bird_y = SCREEN_HEIGHT - 75

    # ---- Drawing code goes here
    screen.blit(bg_image, [0, 0])
    screen.blit(bird_image, [bird_x, bird_y])
    screen.blit(cloud2_image, [cloud2_x, 0])
    screen.blit(cloud_image, [cloud_x, 0])
    screen.blit(cloud1_image, [cloud1_x, 50])


    pygame.display.flip()  # updates the screen

    # --- Limit to 60 frames per second
    clock.tick(60) # frames per second

# Close the window and quit.
pygame.quit()

