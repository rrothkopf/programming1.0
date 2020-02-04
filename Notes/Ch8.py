import pygame
import math
pygame.init()  # vroom vroom

# Define some variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (206, 191, 219)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
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

rect_x = 0
change_x = 5
rect_y = 0
change_y = 3
accel_y = 0.1

bg_color = [0, 0, 0]
color_list = [RED, ORANGE, YELLOW, GREEN, BLUE]
color_index = 0

angle = 0
angle_speed = .01
length = 200

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard or controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    print(pygame.time.get_ticks())  # time in millis

    angle += angle_speed
    dx = math.cos(angle) * length
    dy = math.sin(angle) * length
    # color shift
    '''
    if bg_color[1] < 255:
        bg_color[1] += 1  # must be int from 0 to 255
    if bg_color[0] < 255:
        bg_color[0] += 1
    '''

    # cycle through colors
    color_index += 1

    # move our rectangle
    change_y += accel_y
    rect_x += change_x
    rect_y += change_y

    if rect_x > SCREEN_WIDTH - 50 or rect_x < 0:
        change_x = change_x * -1

    if rect_y > SCREEN_HEIGHT - 50:
        change_y *= -1
        color_index += 1
    if rect_y < 0:
        change_y *= -1
        color_index += 1

    # Wrap
    '''
    if rect_x > SCREEN_WIDTH:
        rect_x = -50 
    '''
    # ---- Drawing code goes here
    screen.fill(bg_color)

    pygame.draw.rect(screen, PURPLE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, color_list[color_index % len(color_list)], [rect_x, rect_y, 50, 50])

    if pygame.time.get_ticks() > 5000:
       pygame.draw.rect(screen, BLUE, [100, 200, 50, 50])

    if pygame.time.get_ticks() % 1000 < 500:
        pygame.draw.rect(screen, WHITE, [100, 300, 50, 50])
    else:
        pygame.draw.rect(screen, ORANGE, [100, 300, 50, 50])

    pygame.draw.line(screen, WHITE, [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], [SCREEN_WIDTH // 2 + dx, SCREEN_HEIGHT // 2 + dy], 3)

    pygame.display.flip()  # updates the screen

    # --- Limit to 60 frames per second
    clock.tick(60) # frames per second

# Close the window and quit.
pygame.quit()
