# This is a pygame template- skeleton for a new pygame project
import pygame, sys
import random
from pygame.locals import *
from settings import *
import time

WIDTH = 1280
HEIGHT = 660

# Frames per second
FPS = 30

# Create Sound Object
pygame.mixer.init(44100, -16,2,2048)
soundObj1 = pygame.mixer.Sound('fart-1.wav')
soundObj2 = pygame.mixer.Sound('fart-2.wav')
soundObj3 = pygame.mixer.Sound('fart-3.wav')
soundObj4 = pygame.mixer.Sound('fart-4.wav')

#Create Sprite group to make updating quicker and easier
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

class Player(pygame.sprite.Sprite):
    # Sprite for the Player
    # start of any object to initialize
    def __init__(self):
        # now initialize Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# Useful colors defined (red, green, blue from 0 -255). Fourth value is alpha value for transparancy 0- 255.
WHITE =(255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
GRAY = (128, 128, 128)
SILVER = (192, 192, 192)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Fire up pygame and create winow
pygame.init()
pygame.mixer.init()

# imports the sprite. Sprite may be PNG, JPG, GIF, and BMP. Sprite MUST be in same folder as .py file
catImg = pygame.image.load(r'C:\Users\...\Documents\Python Scripts from Workstation\Pygame\catAnimation\cat.png')

# Set sprite's initial x and y
catx = 10
caty = 10
direction = 'right'


# Name the window the game is played in
pygame.display.set_caption(TITLE)

# starts the clock to count for time lapsed as related to FPS
clock = pygame.time.Clock()

# Text objects.  1)Font type 2)Text to display (font color, text box color) 3)create text box 4)size of text box
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Welcome to Cat Kingdom', True, AQUA, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (500, 150)

# start Background music
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1, 0.0)

# Game Loop
running = True
while running:
    # keep loop running at right speed
    clock.tick(FPS)
    
    # Process input (events)
    for event in pygame.event.get():
        #Check for closing window
        if event.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
    
    
    # Update Stage
    all_sprites.update()

    
    # Draw/ render Stage
    screen.fill((BLACK))
    all_sprites.draw(screen)

    if direction == 'right':
        catx += 5
        if catx == 1190:
            soundObj1.play()
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 600:
            soundObj2.play()
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            soundObj3.play()
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            soundObj4.play()
            direction = 'right'

    # Copies sprite into display
    screen.blit(catImg, (catx, caty))

    screen.blit(textSurfaceObj, textRectObj)
    
   

    
    


    
    # ONLY *AFTER* drawing everything, flip the display to show what has been drawn
    pygame.display.flip()
