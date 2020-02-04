import pygame
pygame.init()  # vroom vroom

# Define some variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (206, 191, 219)
BRIGHT_YELLOW = (255, 225, 0)
YELLOW = (255, 227, 133)
ORANGE = (255, 184, 133)
SALMON = (255, 157, 133)
PINK = (255, 133, 133)
BLUE = (128, 158, 224)
DARK_BLUE = (96, 142, 214)
DARK_PURPLE = (82, 64, 99)
BROWN = (110, 79, 61)
DARK_BROWN = (64, 50, 40)
OFF_WHITE = (255, 244, 235)
LIGHT_YELLOW = (255, 249, 207)
BABY_PINK = (250, 202, 242)

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

pygame.mouse.set_visible(False)

# Images
bg_image = pygame.image.load("bgCave.bmp")
dragon_right = pygame.image.load("dragon2.png")
dragon_left = pygame.image.load("dragon3.png")
dragon_image = dragon_right

# Sounds
bg_music = pygame.mixer.Sound("bgMusic.wav")
bg_music.play(-1)  # play(number of times to play) (-1, loop forever)
bg_music.set_volume(.5)  # float between 0 and 1

fireball_sound = pygame.mixer.Sound("fireball.wav")
fireball_sound.play()


# Control variables
dragon_x = 0
dragon_y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard or controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            fireball_sound.play()
        if event.type == pygame.MOUSEMOTION:
            if event.rel[0] >= 0:
                dragon_image = dragon_right
            else:
                dragon_image = dragon_left

    # --- Game logic should go here
    dragon_x, dragon_y = pygame.mouse.get_pos()

    # ---- Drawing code goes here
    screen.blit(bg_image, [0, 0])
    screen.blit(dragon_image, [dragon_x, dragon_y])

    pygame.display.flip()  # updates the screen

    # --- Limit to 60 frames per second
    clock.tick(60) # frames per second

# Close the window and quit.
pygame.quit()

