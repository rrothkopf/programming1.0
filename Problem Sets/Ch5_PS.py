'''
Chapter 5 Problem Set
Raven Rothkopf
10/7/19
'''

# Preliminaries
import pygame
pygame.init()
YELLOW = (255, 224, 71)
SKY_BLUE = (145, 187, 255)
GRASS_GREEN = (99, 191, 98)
BRICK_RED = (110, 10, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BABY_PINK = (250, 202, 242)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chapter 5 Problem Set")

clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(SKY_BLUE)
    pygame.draw.ellipse(screen, YELLOW, [599, 0, 100, 100])
    pygame.draw.rect(screen, GRASS_GREEN, [0, 250, 700, 250])
    pygame.draw.line(screen, BLACK, [0, 250], [700, 250], 3)
    pygame.draw.rect(screen, BRICK_RED, [250, 200, 200, 200])
    pygame.draw.polygon(screen, BLACK, ([250, 200], [450, 200], [350, 100]))
    pygame.draw.rect(screen, BLACK, [325, 325, 50, 75])

    # TEXT
    my_font = pygame.font.SysFont("Comic Sans", 40, True, False)
    my_text = my_font.render("Raven Rothkopf", True, BABY_PINK)
    screen.blit(my_text, [50, 25])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
