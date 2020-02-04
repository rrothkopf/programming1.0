import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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
done = False

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chapter 5 Lab")

clock = pygame.time.Clock()

cloud_x = 0
change_x = .5

cloud1_x = 0
cloud_change_x = -.5

boat_x = 0
boat_change_x = .3



# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # move the clouds(WRAP)
    cloud_x += change_x
    if cloud_x > SCREEN_WIDTH:
        cloud_x = -250

    cloud1_x += cloud_change_x
    if cloud1_x < -600:
        cloud1_x = 200

    # move the boat(BOUNCE)
    boat_x += boat_change_x
    if boat_x > SCREEN_WIDTH - 550 or boat_x < -500:
        boat_change_x = boat_change_x * -1

    # Twinkling Stars(BLINK)


    # Sunset
    screen.fill(PINK)
    pygame.draw.rect(screen, SALMON, [0, 125, 700, 250])
    pygame.draw.rect(screen, ORANGE, [0, 250, 700, 125])
    pygame.draw.rect(screen, YELLOW, [0, 325, 700, 62.5])
    if pygame.time.get_ticks() % 120 < 100:
        for x in range(0, 700, 15):
            for y in range(0, SCREEN_HEIGHT, 50):
                pygame.draw.ellipse(screen, WHITE, [x, y, 3, 3])
    pygame.draw.ellipse(screen, BRIGHT_YELLOW, [250, 290, 200, 200])
    pygame.draw.rect(screen, BLUE, [0, 375, 700, 250])

    # Cloud 1
    pygame.draw.ellipse(screen, PURPLE, [50 + cloud_x, 100, 100, 50])
    pygame.draw.ellipse(screen, PURPLE, [80 + cloud_x, 125, 100, 50])
    pygame.draw.ellipse(screen, PURPLE, [100 + cloud_x, 80, 100, 50])
    pygame.draw.ellipse(screen, PURPLE, [125 + cloud_x, 115, 120, 50])

    # Cloud 2
    pygame.draw.ellipse(screen, PURPLE, [600 + cloud1_x, 215, 150, 50])
    pygame.draw.ellipse(screen, PURPLE, [555 + cloud1_x, 225, 100, 50])
    pygame.draw.ellipse(screen, PURPLE, [575 + cloud1_x, 180, 100, 50])
    pygame.draw.ellipse(screen, PURPLE, [515 + cloud1_x, 200, 150, 50])

    # Bird 1
    pygame.draw.ellipse(screen, DARK_PURPLE, [550, 50, 60, 20])
    pygame.draw.ellipse(screen, DARK_PURPLE, [495, 50, 60, 20])
    pygame.draw.ellipse(screen, PINK, [550, 55, 60, 20])
    pygame.draw.ellipse(screen, PINK, [495, 55, 60, 20])

    # Bird 2
    pygame.draw.ellipse(screen, DARK_PURPLE, [150, 250, 60, 20])
    pygame.draw.ellipse(screen, DARK_PURPLE, [95, 250, 60, 20])
    pygame.draw.ellipse(screen, ORANGE, [150, 255, 60, 20])
    pygame.draw.ellipse(screen, ORANGE, [95, 255, 60, 20])

    # Sun Reflection
    pygame.draw.line(screen, LIGHT_YELLOW, [230, 375], [475, 375], 3)
    pygame.draw.line(screen, LIGHT_YELLOW, [225, 385], [480, 385], 3)
    pygame.draw.line(screen, LIGHT_YELLOW, [235, 395], [470, 395], 3)
    pygame.draw.line(screen, LIGHT_YELLOW, [240, 405], [465, 405], 3)
    pygame.draw.line(screen, LIGHT_YELLOW, [249, 415], [451, 415], 3)
    pygame.draw.line(screen, LIGHT_YELLOW, [250, 425], [445, 425], 3)
    pygame.draw.line(screen, LIGHT_YELLOW, [265, 435], [435, 435], 3)
    pygame.draw.line(screen, LIGHT_YELLOW, [275, 445], [425, 445], 3)
    pygame.draw.line(screen, LIGHT_YELLOW, [285, 455], [415, 455], 3)
    pygame.draw.line(screen, LIGHT_YELLOW, [300, 465], [400, 465], 3)
    pygame.draw.line(screen, LIGHT_YELLOW, [325, 475], [375, 475], 3)

    # Boat
    pygame.draw.ellipse(screen, DARK_BLUE, [550 + boat_x, 385, 70, 20])
    pygame.draw.ellipse(screen, BROWN, [550 + boat_x, 345, 80, 50])
    pygame.draw.rect(screen, YELLOW, [550 + boat_x, 345, 700, 20])
    pygame.draw.polygon(screen, OFF_WHITE, ([588 + boat_x, 320], [560 + boat_x, 350], [620 + boat_x, 350]))
    pygame.draw.line(screen, DARK_BROWN, [588 + boat_x, 365], [588 + boat_x, 320], 3)

    # Signature
    my_font = pygame.font.SysFont("Comic Sans", 20, True, False)
    my_text = my_font.render("Raven Rothkopf", True, BABY_PINK)
    screen.blit(my_text, [8, 480])

    # Game logic goes here


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
