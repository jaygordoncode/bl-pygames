import pygame
import random

# Initialize game - tells computer that the following
# code should be interpretted as a game.
pygame.init()

#step 1. Set up the display
height = 600
width = 800

# this is reusable code that represemts our game screen
screen = pygame.display.set_mode((width, height))

# this will allow us to show the title of the game when a
# user opens our game
pygame.display.set_caption("Avoid the Falling Objects")

# set frame rate
Clock = pygame.time.Clock() # games run on frames
fps = 60 # game updates 60 times per second

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

# Step 2. Creatte player object
# Object - a data type that allows us to
# pass in unique data, including
# functions and other objects.

class Player:
    def __init__(self):
        self.x = width // 2 #start in the middle
        self.y = height - 60 # Near the bottom
        self.playerWidth = 50
        self.playerHeight = 50
        self.playerSpeed = 5 # How fast the player moves

def move (self, keys):
    if keys [pygame.K_LEFT] and self.x > 0:
        self.x -= self.playerSpeed
    if keys[pygame.K_RIGHT] and self.x < width - self.playerWidth:
        self.x += self.playerSpeed

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 225),
                         
                         
        (self.x, self.y, self.playerWidth, self.playerHeight)) 
        
class FallingObject: 
    def _init_(self):
        self.x = random.randint(0,width - 50)
        self.y = -50
        self.width = 50 
        self.height = 50 
        self.speed= random.randint(3,7)
    
    def move(self):
        self.y += self.speed
    
    def draw(self):
        pygame.draw.rect(screen, (255,0,0) (self.x, self.y, self.width, self.height))
    
    def off_screen(self):
        return self.y > height
    
player = Player()
falling_objects = []
score = 0
lives = 3 

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
        