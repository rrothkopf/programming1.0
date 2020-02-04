'''
Chapter 13 Lab - Sprites
Raven Rothkopf
12/10/19
'''

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (207, 239, 255)
DARK_BLUE = (43, 130, 173)

score = 0
level = 1


class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # set boundaries here
        if self.rect.x > screen_width - 15:
            self.rect.x = screen_width - 15
        if self.rect.y > screen_height - 15:
            self.rect.y = screen_height - 15

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0


# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# good blocks
for i in range(50):
    block = Block(RED, 20, 15)
    block.image = pygame.image.load("Bubble2.png")
    block.rect = block.image.get_rect()

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    good_block_list.add(block)
    all_sprites_list.add(block)

# bad blocks
for i in range(50):
    block = Block(RED, 20, 15)
    block.image = pygame.image.load("Dirty_Bubble_Vector.png")
    block.rect = block.image.get_rect()

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    bad_block_list.add(block)
    all_sprites_list.add(block)

# Create a RED player block
player = Player(20, 20)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def intro_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(RED)
        pygame.display.flip()
        clock.tick(60)

intro_screen()

score = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
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

    # Clear the screen
    screen.fill(BLUE)

    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)

    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)

    # Check the list of collisions.
    for block in good_blocks_hit_list:
        score += 1
        print(score)

    for block in bad_blocks_hit_list:
        score -= 1
        print(score)

    if len(good_blocks_hit_list) == 0:
        level += 1
        print("level up")
        for i in range(50):
            block = Block(RED, 20, 15)
            block.image = pygame.image.load("Bubble2.png")
            block.rect = block.image.get_rect()

            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(screen_height)
            good_block_list.add(block)
            all_sprites_list.add(block)


    # Draw all the spites
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    my_font = pygame.font.SysFont("Comic Sans", 25, True, False)
    my_text = my_font.render("Score:" + str(score), True, DARK_BLUE)
    screen.blit(my_text, [8, 8])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
