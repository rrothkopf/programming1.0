import pygame
pygame.init()  # vroom vroom

# Define some variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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
RED = (255, 0, 0)


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
rect_x = 0
rect_y = 0
rect_color = PINK

ellipse_x = 0
ellipse_y = 0
change_x = 0
change_y = 0

def draw_stickman(x, y):
    x -= 95
    y -= 83
    # Head
    pygame.draw.ellipse(screen, BLACK, [96 + x, 83 + y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [100 + x, 100 + y], [105 + x, 110 + y], 2)
    pygame.draw.line(screen, BLACK, [100 + x, 100 + y], [95 + x, 110 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [100 + x, 100 + y], [100 + x, 90 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [100 + x, 90 + y], [104 + x, 100 + y], 2)
    pygame.draw.line(screen, RED, [100 + x, 90 + y], [96 + x, 100 + y], 2)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard or controller)
    #  You can only have one event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos, event.button)
            rect_color = YELLOW
        elif event.type == pygame.MOUSEBUTTONUP:
            rect_color = PINK
        elif event.type == pygame.MOUSEMOTION:
            # rect_color = BLUE
            print(event.pos, event.rel, event.buttons)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_x = 3
            elif event.key == pygame.K_LEFT:
                change_x = -3
            elif event.key == pygame.K_DOWN:
                change_y = 3
            elif event.key == pygame.K_UP:
                change_y = -3
        elif event.type == pygame.KEYUP:  # lift finger off key
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                change_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                change_y = 0


    # --- Game logic should go here
    ellipse_x += change_x
    ellipse_y += change_y

    if ellipse_x > SCREEN_WIDTH - 30:
        ellipse_x = SCREEN_WIDTH - 30
    if ellipse_y > SCREEN_HEIGHT - 30:
        ellipse_y = SCREEN_HEIGHT - 30
    if ellipse_y < 0:
        ellipse_y = 0
    if ellipse_x < 0:
        ellipse_x = 0

    rect_x, rect_y = pygame.mouse.get_pos()

    if rect_x > SCREEN_WIDTH - 30:
        rect_x = SCREEN_WIDTH - 30
    if rect_y > SCREEN_HEIGHT - 30:
        rect_y = SCREEN_HEIGHT - 30

    # ---- Drawing code goes here
    screen.fill(WHITE)

    pygame.draw.rect(screen, rect_color, [rect_x, rect_y, 30, 30])

    pygame.draw.ellipse(screen, ORANGE, [ellipse_x, ellipse_y, 30, 30])

    draw_stickman(0, 0)
    pygame.display.flip()  # updates the screen

    # --- Limit to 60 frames per second
    clock.tick(60) # frames per second

# Close the window and quit.
pygame.quit()