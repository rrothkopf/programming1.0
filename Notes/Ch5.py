"""
Pygame Template
Raven Rothkopf
10/2/19
"""

import pygame
pygame.init()  # vroom vroom

# Define some variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
GRAY = (100, 100, 100)
PINK = (255, 200, 200)
ORANGE = (255, 150, 0)
MAROON = (75, 0, 0)
score = 0


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
    screen.fill(CYAN)
    pygame.draw.rect(screen, RED, [0, 0, 50, 50])

    # rect(surface, color, [top_left_x, top_left_y, width, height], optional_thickness)
    pygame.draw.rect(screen, RED, [0, 0, 100, 70])
    pygame.draw.rect(screen, BLACK, [0, 0, 100, 70], 2)
    pygame.draw.rect(screen, GREEN, [600, 50, 100, 100], 3)

    # ellipse (surface, color, [top_left_x, top_left_y, width, height)
    # ellipse is drawn inside (circumscribed) the defined rectangle
    pygame.draw.rect(screen, ORANGE, [200, 200, 100, 100])
    pygame.draw.ellipse(screen, PINK, [200, 200, 100, 100])
    pygame.draw.ellipse(screen, MAROON, [SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 100, 400, 100])

    # line(surface, color, [x1, y1], [x2, y2], thickness)
    pygame.draw.line(screen, BLACK, [0, 0], [SCREEN_WIDTH, SCREEN_HEIGHT], 3)

    # drawing with loops
    for x in range(0, SCREEN_WIDTH, 20):
        pygame.draw.line(screen, BLACK, [x, 0], [x, SCREEN_HEIGHT], 5)

    for x in range(0, SCREEN_WIDTH, 50):
        for y in range(0, SCREEN_HEIGHT, 50):
            pygame.draw.rect(screen, BLUE, [x, y, 20, 20])

    screen.fill(WHITE)
    # polygon(surface, color, ([x1, y1], [x2, y2], [x3, y3]...), optional_thickness)
    pygame.draw.polygon(screen, RED, ([0, 0], [200, 0], [100, 200]))

    # FONTS
    # SysFont(name, size, bold, italics)
    # in console pygame.font.get_fonts()
    my_font = pygame.font.SysFont("trattatellottf", 40, True, False) # step 1 of three

    # draw text
    my_text = my_font.render("Score: " + str(score), True, WHITE)  # render(string, antialias, color) (step 2 of 3)
    screen.blit(my_text, [50, 50])  # blit(rendered_text_object, [x, y])

    pygame.display.flip()  # updates the screen

    # --- Limit to 60 frames per second
    clock.tick(60) # frames per second



# Close the window and quit.
pygame.quit()

