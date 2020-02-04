import pygame
import random
pygame.init()  # vroom vroom

# Define some variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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

# CLASSES
class Circle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.diameter = 20
        self.color = GREEN

    def draw(self):
        pygame.draw.ellipse(screen, BLACK, [self.x - 2, self.y - 2, self.diameter + 4, self.diameter + 4])
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.diameter, self.diameter])
    def update(self):
        pass

class Bouncies(Circle):
    def __init__(self):
        super().__init__()
        self.diameter = random.randrange(10, 100)
        self.color = (random.randrange(256), random.randrange(256), random.randrange(256))
        self.x = random.randrange(SCREEN_WIDTH - self.diameter)
        self.y = random.randrange(SCREEN_HEIGHT - self.diameter)
        self.change_x = random.randrange(-10, 10)
        self.change_y = random.random() * 50 - 3
        self.gravity = 0.1
        self.elasticity = .8

    def update(self):
        # move in x
        self.x += self.change_x
        if self.x > SCREEN_WIDTH - self.diameter:
            self.x = SCREEN_WIDTH - self.diameter
            self.change_x *= -1
        if self.x < 0:
            self.x = 0
            self.change_x *= -1

        # move in y
        self.change_y += self.gravity
        self.y += self.change_y
        if self.y > SCREEN_HEIGHT - self.diameter:
            self.y = SCREEN_HEIGHT - self.diameter
            self.change_y *= -self.elasticity
            self.change_x *= self.elasticity

class Bubble(Circle):
    def update(self):
        self.y -= random.random()



shape_list = []

for i in range(100):
    my_circle = Circle()
    my_circle.x = random.randrange(SCREEN_WIDTH - my_circle.diameter)
    my_circle.y = random.randrange(SCREEN_HEIGHT - my_circle.diameter)
    my_circle.diameter = random.randrange(10, 100)
    rb = random.randrange(256)
    my_circle.color = (rb, 255, rb)
    '''
    shape_list.append(my_circle)
    '''

    my_bouncy = Bouncies()
    shape_list.append(my_bouncy)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user mouse, keyboard or controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                my_bubble = Bubble()
                my_bubble.diameter = random.randrange(10, 50)
                my_bubble.x, my_bubble.y = event.pos
                my_bubble.x -= my_bubble.diameter / 2
                my_bubble.y -= my_bubble.diameter / 2
                my_bubble.color = (random.randrange(256), random.randrange(256), random.randrange(256))
                shape_list.append(my_bubble)

    # --- Game logic should go here
    for shape in shape_list:
        shape.update()

    # ---- Drawing code goes here
    screen.fill(WHITE)

    for shape in shape_list:
        shape.draw()

    pygame.display.flip()  # updates the screen

    # --- Limit to 60 frames per second
    clock.tick(60) # frames per second

# Close the window and quit.
pygame.quit()