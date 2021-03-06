import pygame
import random
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

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()  # grabs a rectangle based on the image

class Enemy(Block):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.change_y = 1
        self.change_x = random.randrange(-3, 4)
    def update(self):
        self.rect.x += self.change_x
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.change_x *= -1
        if self.rect.left <= 0:
            self.rect.left = 0
            self.change_x *= -1

        self.rect.y += self.change_y

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

player = Block()
player.image = pygame.image.load("ship.png")
player.rect = player.image.get_rect()
player.rect.bottom = SCREEN_HEIGHT  # put player at bottom

# make my groups

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

enemy_sprites = pygame.sprite.Group()

bullet_sprites = pygame.sprite.Group()

for i in range(20):
    enemy = Enemy()
    enemy.rect.x = random.randrange(0, SCREEN_WIDTH - enemy.rect.width)
    enemy.rect.y = random.randrange(-200, SCREEN_HEIGHT - 200)
    enemy.image.fill(MAGENTA)
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)

# game variables
score = 0
lives = 3
frame = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard or controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_bullet = Bullet()
            new_bullet.rect.centery = player.rect.centery
            new_bullet.rect.centerx = player.rect.centerx
            all_sprites.add(new_bullet)
            bullet_sprites.add(new_bullet)

    # --- Game logic should go here
    frame += 1

    all_sprites.update()
    player.rect.centerx = pygame.mouse.get_pos()[0]

    # bullet enemy collision
    for bullet in bullet_sprites:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_sprites, True)
        for enemy in hit_list:
            bullet.kill()

    hit_list = pygame.sprite.spritecollide(player, enemy_sprites, True)

    for enemy in hit_list:
        enemy.image.fill(CYAN)
        lives -= 1
    if lives <= 0:
        done = True
    if frame % 600 == 0:
        for enemy in enemy_sprites:
            enemy.change_y += 1

    # ---- Drawing code goes here
    screen.fill(WHITE)

    all_sprites.draw(screen)  # draws the image to the rect location

    pygame.display.flip()  # updates the screen

    # --- Limit to 60 frames per second
    clock.tick(60) # frames per second

# Close the window and quit.
pygame.quit()