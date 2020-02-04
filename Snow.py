import pygame
import random
pygame.init()  # vroom vroom

# Define some variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (100, 50, 50)
GREEN = (0, 255, 0)

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

# Snow Variables
snowflakes = []

for i in range(1000):
    flake_size = random.randrange(5, 15)
    flake_speed = flake_size / 5
    flake_x = random.randrange(SCREEN_WIDTH - flake_size)
    flake_y = random.randrange(-flake_size, SCREEN_HEIGHT - flake_size)
    snowflakes.append([flake_x, flake_y, flake_size, flake_speed])

print(snowflakes)

def draw_tree(x, y):
    pygame.draw.rect(screen, BROWN, [60 + x, 170 + y, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150 + x, 400 + y], [75 + x, 250 + y], [0 + x, 400 + y]])
    pygame.draw.polygon(screen, GREEN, [[140 + x, 350 + y], [75 + x, 230 + y], [10 + x, 350 + y]])

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard or controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    for i in range(len(snowflakes)):
        snowflakes[i][1] += snowflakes[i][3]
        if snowflakes[i][1] >= SCREEN_HEIGHT:
            snowflakes[i][1] = -snowflakes[i][2]
            snowflakes[i][0] = random.randrange(SCREEN_WIDTH - snowflakes[i][2])

    # ---- Drawing code goes here
    screen.fill(BLACK)

    draw_tree(100, 200)
    for flake in snowflakes:
        pygame.draw.ellipse(screen, WHITE, [flake[0], flake[1], flake[2], flake[2]])

    pygame.display.flip()  # updates the screen

    # --- Limit to 60 frames per second
    clock.tick(60) # frames per second

# Close the window and quit.
pygame.quit()

