'''
Computer Programming 1 - Final
Raven Rothkopf

My game is a Super Mario Bros. themed Pac-man game. Move around the map using the arrow keys to collect all of the coins
with 4 goombas chasing you. The mushrooms act as 1-ups. After you collect all of the coins,
you level up and the goombas increase their speed. If you run into the goombas after the second level,
they take damage and decrease their speed. You can level up infinitely, but if you die once, you go back to level one.
There is an option to replay the game. The game resets each time you level up.

Music by Shade Rothkopf
'''

import pygame
import random

pygame.init()  # vroom vroom

# Define some variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 189, 71)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
GRAY = (100, 100, 100)
PINK = (255, 200, 200)
ORANGE = (255, 150, 0)
MAROON = (75, 0, 0)
DARK_BLUE = (17, 11, 66)
DARK_PURPLE = (37, 23, 82)

score = 0
lives = 3
one_ups = 2
level = 1

done = False  # condition for game loop

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 725

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Super Mario Pac-Man")

# CLASSES
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image1 = pygame.image.load("mario.png")
        self.image2 = pygame.image.load("mario1.png")
        self.image = self.image1

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):

        # move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = wall.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = wall.rect.right

        # move up/down
        self.rect.y += self.change_y
        hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        for wall in hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        # Call the parent's constructor
        super().__init__()

        # Make a green wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Goomba(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.speed = 2
        self.change_x = 2
        self.change_y = 0
        self.walls = None

    def update(self):
        self.rect.x += self.change_x
        hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in hit_list:
            if self.change_x > 0:
                self.rect.right = wall.rect.left
                self.change_x = 0
                if random.randrange(2) == 0:
                    self.change_y = self.speed
                else:
                    self.change_y = -self.speed
            if self.change_x < 0:
                self.rect.left = wall.rect.right
                self.change_x = 0
                if random.randrange(2) == 0:
                    self.change_y = self.speed
                else:
                    self.change_y = -self.speed

        self.rect.y += self.change_y
        hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in hit_list:
            if self.change_y > 0:
                self.rect.bottom = wall.rect.top
                self.change_y = 0
                if random.randrange(2) == 0:
                    self.change_x = self.speed
                else:
                    self.change_x = -self.speed
            if self.change_y < 0:
                self.rect.top = wall.rect.bottom
                self.change_y = 0
                if random.randrange(2) == 0:
                    self.change_x = self.speed
                else:
                    self.change_x = -self.speed


class Mushroom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([x, y])
        self.rect = self.image.get_rect()

all_sprites_list = pygame.sprite.Group()
coin_list = pygame.sprite.Group()
mushroom_list = pygame.sprite.Group()


# IMAGES:

# game images
pipe_image = pygame.image.load("pipe.png")
toad_image = pygame.image.load("toad.png")
coin_image = pygame.image.load("coin.png")
peach_right = pygame.image.load("peach.png")
peach_left = pygame.image.load("peach2.png")
peach_image = peach_right
red_goomba = pygame.image.load("redgoomba.png")
brown_goomba = pygame.image.load("browngoomba.png")
blue_goomba = pygame.image.load("blue.png")
orange_goomba = pygame.image.load("orange.png")
mushroom_image = pygame.image.load("mushroom.png")
gameover = pygame.image.load("gameover.jpg")

# intro screen images
mario_bg = pygame.image.load("1.png")
pacman_bg = pygame.image.load("2.jpg")
mario_logo = pygame.image.load("mario.jpg")
pacman_logo = pygame.image.load("pacman.png")
box = pygame.image.load("box.jpg")

# instructions screen images
mario_1 = pygame.image.load("marioman.png")
pacman_1 = pygame.image.load("pacman1.png")

# game over screen images

# SOUNDS
background_music = pygame.mixer.Sound("background music.wav")
background_music.play(-1)
background_music.set_volume(.1)
level_clear = pygame.mixer.Sound("levelclear.wav")
level_clear.set_volume(.1)
game_over_sound = pygame.mixer.Sound("gameover.wav")
game_over_sound.set_volume(.1)
goomba_hit = pygame.mixer.Sound("hit.wav")
goomba_hit.set_volume(.1)
mushroom_sound = pygame.mixer.Sound("1up.wav")
mushroom_sound.set_volume(.1)

# peach variables
peach_x = 360
peach_change_x = .8

# make walls
wall_list = pygame.sprite.Group()

# BOUNDARIES
wall = Wall(0, 0, 30, 725, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(0, 0, 700, 50, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(0, 700, 700, 30, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(670, 0, 50, 725, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(550, 570, 125, 50, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(20, 570, 125, 50, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(20, 240, 85, 30, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(20, 470, 125, 25, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(580, 240, 95, 30, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(330, 675, 40, 30, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(595, 345, 80, 142, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(330, 30, 40, 127, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(30, 170, 75, 40, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(273, 170, 27, 50, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(273, 188, 40, 37, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(400, 90, 230, 60, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(75, 300, 125, 125, DARK_PURPLE)
wall_list.add(wall)
all_sprites_list.add(wall)

# PIPES

# lower half
wall = Wall(60, 650, 240, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(400, 650, 240, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(185, 575, 15, 75, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(500, 575, 15, 75, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(250, 575, 200, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(345, 575, 15, 70, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(200, 475, 300, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(345, 475, 15, 70, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(415, 525, 200, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(85, 525, 200, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(240, 430, 15, 50, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(450, 430, 15, 50, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

# upper half
wall = Wall(200, 255, 300, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(345, 195, 15, 70, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(550, 300, 15, 195, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(550, 300, 90, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(240, 255, 15, 65, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(450, 255, 15, 65, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(60, 80, 240, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(180, 80, 15, 60, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(60, 125, 90, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(135, 125, 15, 150, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(225, 125, 75, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(225, 125, 15, 100, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(180, 175, 15, 50, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(495, 255, 10, 20, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

# TOAD BOX
wall = Wall(60, 425, 150, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(60, 300, 15, 125, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(195, 300, 15, 125, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(60, 300, 150, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

# PEACH BOX
wall = Wall(400, 140, 240, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(400, 80, 240, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(400, 80, 15, 70, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(625, 80, 15, 70, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(400, 188, 240, 15, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(535, 188, 15, 82.5, GREEN)
wall_list.add(wall)
all_sprites_list.add(wall)

# GOOMBAS
goomba_list = pygame.sprite.Group()

redgoomba = Goomba(650, 650)
redgoomba.image = red_goomba
redgoomba.rect = redgoomba.image.get_rect()
redgoomba.rect.center = (650, 650)
redgoomba.walls = wall_list
redgoomba.change_x = 2
redgoomba.change_y = 0
all_sprites_list.add(redgoomba)
goomba_list.add(redgoomba)

browngoomba = Goomba(650, 100)
browngoomba.image = brown_goomba
browngoomba.rect = browngoomba.image.get_rect()
browngoomba.rect.center = (650, 100)
browngoomba.walls = wall_list
browngoomba.change_x = 2
browngoomba.change_y = 0
all_sprites_list.add(browngoomba)
goomba_list.add(browngoomba)

bluegoomba = Goomba(100, 650)
bluegoomba.image = blue_goomba
bluegoomba.rect = bluegoomba.image.get_rect()
bluegoomba.rect.center = (100, 650)
bluegoomba.walls = wall_list
bluegoomba.change_x = 2
bluegoomba.change_y = 0
all_sprites_list.add(bluegoomba)
goomba_list.add(bluegoomba)

orangegoomba = Goomba(100, 100)
orangegoomba.image = orange_goomba
orangegoomba.rect = orangegoomba.image.get_rect()
orangegoomba.rect.center = (100, 100)
orangegoomba.walls = wall_list
orangegoomba.change_x = 2
orangegoomba.change_y = 0
all_sprites_list.add(orangegoomba)
goomba_list.add(orangegoomba)

# PLAYER
player = Player(350, 360)
player.walls = wall_list
all_sprites_list.add(player)

# COINS
for x in range(10, 700, 20):
    for y in range(5, 750, 20):
        coin = Coin(x, y)
        all_sprites_list.add(coin)
        coin_list.add(coin)

# MUSHROOMS
mushroom_1 = Mushroom(48, 65)
mushroom_1.image = mushroom_image
mushroom_1.rect = mushroom_1.image.get_rect()
mushroom_1.rect.center = (48, 65)
all_sprites_list.add(mushroom_1)
mushroom_list.add(mushroom_1)

mushroom_2 = Mushroom(650, 685)
mushroom_2.image = mushroom_image
mushroom_2.rect = mushroom_1.image.get_rect()
mushroom_2.rect.center = (650, 685)
all_sprites_list.add(mushroom_2)
mushroom_list.add(mushroom_2)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()  # creates a clock object that manages updates

# INTRO SCREEN
def intro_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True

                else:
                    done = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3, 0)
                    player.image = player.image2
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                    player.image = player.image1
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 3)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)

        screen.fill(WHITE)
        screen.blit(mario_bg, [0 , 0])
        screen.blit(pacman_bg, [350, 0])
        screen.blit(mario_logo, [80, 60])
        screen.blit(pacman_logo, [380, 60])
        screen.blit(box, [180, 200])

        text = my_font.render("Welcome to Super Mario Bros.", True, BLACK)
        text_1 = my_font.render("x Pacman!", True, BLACK)
        text_2 = my_font.render("Press the space bar", True, BLACK)
        text_3 = my_font.render("for instructions.", True, BLACK)

        screen.blit(text, [187, 210])
        screen.blit(text_1, [300, 240])
        screen.blit(text_2, [260, 295])
        screen.blit(text_3, [270, 325])

        pygame.display.flip()
        clock.tick(60)
intro_screen()

# LEVEL CLEARED SCREEN
def clear():
    for i in range(300):
        background_music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True

                else:
                    done = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3, 0)
                    player.image = player.image2
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                    player.image = player.image1
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 3)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)

        pygame.draw.rect(screen, BLACK, [200, 300, 300, 100])

        text = my_font.render("LEVEL CLEARED!", True, WHITE)

        screen.blit(text, [250, 345])

        pygame.display.flip()
        clock.tick(60)

# INSTRUCTIONS SCREEN

def instructions_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
                else:
                    done = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3, 0)
                    player.image = player.image2
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                    player.image = player.image1
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 3)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)

        screen.fill(DARK_PURPLE)
        screen.blit(mario_1, [200, 100])
        screen.blit(pacman_1, [400, 100])

        text = my_font.render("INSTRUCTIONS:", True, WHITE)
        text_1 = my_font.render("Travel around the map using the arrow keys", True, WHITE)
        text_7 = my_font.render("to collect coins.", True, WHITE)
        text_2 = my_font.render("Avoid the Goombas at all costs!", True, WHITE)
        text_8 = my_font.render("If they catch you 3 times its game over.", True, WHITE)
        text_3 = my_font.render("The mushrooms give you an extra life.", True, WHITE)
        text_4 = my_font.render("Collect all of the coins without running out of lives to win!", True, WHITE)
        text_5 = my_font.render("GOOD LUCK :)", True, WHITE)
        text_6 = my_font.render("(press the space bar to play!)", True, WHITE)

        screen.blit(text, [260, 270])
        screen.blit(text_1, [100, 340])
        screen.blit(text_7, [260, 370])
        screen.blit(text_2, [170, 400])
        screen.blit(text_8, [120, 430])
        screen.blit(text_3, [140, 460])
        screen.blit(text_4, [5, 490])
        screen.blit(text_5, [280, 560])
        screen.blit(text_6, [170, 650])

        pygame.display.flip()
        clock.tick(60)
instructions_screen()

# GAME OVER SCREEN
def game_over():
    done = False
    background_music.stop()
    my_font = pygame.font.SysFont("Calibri", 40, True, False)
    game_over_sound.play(0)
    end_game = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                end_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
                    background_music.play(-1)
                    intro_screen()
                    instructions_screen()
                    end_game = False
                else:
                    done = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3, 0)
                    player.image = player.image2
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                    player.image = player.image1
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 3)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)

        screen.fill(BLACK)
        screen.blit(gameover, [250, 260])

        text = my_font.render("Want to play again?", True, WHITE)
        text_1 = my_font.render("Press the space bar to start over.", True, WHITE)
        screen.blit(text, [200, 450])
        screen.blit(text_1, [100, 480])

        pygame.display.flip()
        clock.tick(60)

    return end_game

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard or controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
                player.image = player.image2
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
                player.image = player.image1
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # --- Game logic should go here
    # move Peach (BOUNCE)
    peach_x += peach_change_x
    if peach_x > 545:
        peach_change_x = peach_change_x * -1
        peach_image = peach_left

    if peach_x < 345:
        peach_change_x = peach_change_x * -1
        peach_image = peach_right

    # ---- Drawing code goes here
    screen.fill(DARK_BLUE)

    # draw all sprites
    all_sprites_list.update()
    coin_list.draw(screen)
    wall_list.draw(screen)
    mushroom_list.draw(screen)
    goomba_list.draw(screen)
    screen.blit(player.image, player.rect.topleft)

    screen.blit(pipe_image, [80, 375])
    screen.blit(toad_image, [150, 385])
    screen.blit(peach_image, [peach_x, 44])

    if pygame.time.get_ticks() % 120 < 100:
        screen.blit(coin_image, [95, 340])

    # COLLISIONS:

    # coin collisions
    coin_hit_list = pygame.sprite.spritecollide(player, coin_list, True)
    for coin in coin_hit_list:
        score += 1

    for wall in wall_list:
        pygame.sprite.spritecollide(wall, coin_list, True)

    # player/mushroom collision
    mushroom_hit_list = pygame.sprite.spritecollide(player, mushroom_list, True)
    for mushroom in mushroom_hit_list:
        lives += 1
        one_ups -= 1
        mushroom_sound.play()

    # player/goomba collision
    goomba_hit_list = pygame.sprite.spritecollide(player, goomba_list, True)
    for goomba in goomba_hit_list:
        lives -= 1
        goomba_hit.play(0)

        if goomba == redgoomba:
            redgoomba = Goomba(650, 650)
            redgoomba.image = red_goomba
            redgoomba.rect = redgoomba.image.get_rect()
            redgoomba.rect.center = (650, 650)
            redgoomba.walls = wall_list
            redgoomba.change_x = 2
            redgoomba.change_y = 0
            all_sprites_list.add(redgoomba)
            goomba_list.add(redgoomba)

        if goomba == orangegoomba:
            orangegoomba = Goomba(100, 100)
            orangegoomba.image = orange_goomba
            orangegoomba.rect = orangegoomba.image.get_rect()
            orangegoomba.rect.center = (100, 100)
            orangegoomba.walls = wall_list
            orangegoomba.change_x = 2
            orangegoomba.change_y = 0
            all_sprites_list.add(orangegoomba)
            goomba_list.add(orangegoomba)

        if goomba == browngoomba:
            browngoomba = Goomba(650, 100)
            browngoomba.image = brown_goomba
            browngoomba.rect = browngoomba.image.get_rect()
            browngoomba.rect.center = (650, 100)
            browngoomba.walls = wall_list
            browngoomba.change_x = 2
            browngoomba.change_y = 0
            all_sprites_list.add(browngoomba)
            goomba_list.add(browngoomba)

        if goomba == bluegoomba:
            bluegoomba = Goomba(100, 650)
            bluegoomba.image = blue_goomba
            bluegoomba.rect = bluegoomba.image.get_rect()
            bluegoomba.rect.center = (100, 650)
            bluegoomba.walls = wall_list
            bluegoomba.change_x = 2
            bluegoomba.change_y = 0
            all_sprites_list.add(bluegoomba)
            goomba_list.add(bluegoomba)

    # CONDITIONS FOR LOSING/BEATING A LEVEL
    if lives <= 0 or lives == 0:
            done = game_over()

            score = 0
            lives = 3
            one_ups = 2
            level = 1

            # reset player
            player.rect.center = (350, 360)

            # create coins
            for coin in coin_list:
                coin.kill()
            for x in range(10, 700, 20):
                for y in range(5, 750, 20):
                    coin = Coin(x, y)
                    all_sprites_list.add(coin)
                    coin_list.add(coin)

            coin_hit_list = pygame.sprite.spritecollide(player, coin_list, True)
            for coin in coin_hit_list:
                score += 1

            # reset goombas
            redgoomba.rect.center = (650, 650)

            orangegoomba.rect.center = (100, 100)

            bluegoomba.rect.center = (100, 650)

            browngoomba.rect.center = (650, 100)

            # create mushrooms
            for mushroom in mushroom_list:
                mushroom.kill()

            mushroom_1 = Mushroom(48, 65)
            mushroom_1.image = mushroom_image
            mushroom_1.rect = mushroom_1.image.get_rect()
            mushroom_1.rect.center = (48, 65)
            all_sprites_list.add(mushroom_1)
            mushroom_list.add(mushroom_1)

            mushroom_2 = Mushroom(650, 685)
            mushroom_2.image = mushroom_image
            mushroom_2.rect = mushroom_1.image.get_rect()
            mushroom_2.rect.center = (650, 685)
            all_sprites_list.add(mushroom_2)
            mushroom_list.add(mushroom_2)

            mushroom_hit_list = pygame.sprite.spritecollide(player, mushroom_list, True)
            for mushroom in mushroom_hit_list:
                lives += 1
                one_ups -= 1
                mushroom_sound.play()

    if score == 548 or score == 1096 or score == 1644 or score == 2192 or score == 2740 or score == 3288 or score == 3836 or score == 4384 or score == 4932 or score == 5480 or score == 6028 or score == 6576 or score == 7124 or score == 7672 or score == 8220:

        # reset player

        level_clear.play(0)
        lives = 3
        one_ups = 2
        level += 1

        player.rect.center = (350, 360)

        # LEVEL CLEAR
        clear()
        background_music.play(-1)

        for x in range(10, 700, 20):
            for y in range(5, 750, 20):
                coin = Coin(x, y)
                all_sprites_list.add(coin)
                coin_list.add(coin)

        coin_hit_list = pygame.sprite.spritecollide(player, coin_list, True)
        for coin in coin_hit_list:
            score += 1

        # reset goombas
        redgoomba.speed += 1
        orangegoomba.speed += 1
        bluegoomba.speed += 1
        browngoomba.speed += 1

        redgoomba.rect.center = (650, 650)

        orangegoomba.rect.center = (100, 100)

        bluegoomba.rect.center = (100, 650)

        browngoomba.rect.center = (650, 100)

        # create mushrooms
        for mushroom in mushroom_list:
            mushroom.kill()

        mushroom_1 = Mushroom(48, 65)
        mushroom_1.image = mushroom_image
        mushroom_1.rect = mushroom_1.image.get_rect()
        mushroom_1.rect.center = (48, 65)
        all_sprites_list.add(mushroom_1)
        mushroom_list.add(mushroom_1)

        mushroom_2 = Mushroom(650, 685)
        mushroom_2.image = mushroom_image
        mushroom_2.rect = mushroom_1.image.get_rect()
        mushroom_2.rect.center = (650, 685)
        all_sprites_list.add(mushroom_2)
        mushroom_list.add(mushroom_2)

        mushroom_hit_list = pygame.sprite.spritecollide(player, mushroom_list, True)
        for mushroom in mushroom_hit_list:
            lives += 1
            one_ups -= 1
            mushroom_sound.play()

    # SCORE
    my_font = pygame.font.SysFont("Comic Sans", 30, True, False)
    my_text = my_font.render("Score:" + str(score), True, WHITE)
    screen.blit(my_text, [40, 20])

    # LIVES
    my_font = pygame.font.SysFont("Comic Sans", 30, True, False)
    my_text = my_font.render("Lives:" + str(lives), True, WHITE)
    screen.blit(my_text, [200, 20])

    # ONE-UPS
    my_font = pygame.font.SysFont("Comic Sans", 30, True, False)
    my_text = my_font.render("1-UPS:" + str(one_ups), True, WHITE)
    screen.blit(my_text, [450, 20])

    # LEVELS
    my_font = pygame.font.SysFont("Comic Sans", 30, True, False)
    my_text = my_font.render("Level:" + str(level), True, WHITE)
    screen.blit(my_text, [570, 20])

    pygame.display.flip()  # updates the screen

    # --- Limit to 60 frames per second
    clock.tick(60)  # frames per second

# Close the window and quit.
pygame.quit()
