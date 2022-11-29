#This file is for global variables etc that are needed throughout the program
import pygame
import os

clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#images

right = [None]*10
for rpic in range(1,10):
    right[rpic-1] = pygame.image.load(os.path.join('assets', 'R' + str(rpic) + '.png'))
    rpic += 1
  
left = [None]*10
for lpic in range(1,10):
    left[lpic-1] = pygame.image.load(os.path.join('assets', 'L' + str(lpic) + '.png'))
    lpic += 1

standing = pygame.image.load('assets/standing.png')
playerImgL = pygame.image.load('assets/L1.png')
mountains = pygame.image.load('assets/mountains.jpg')



mountainWidth = mountains.get_width()
mountainHeight = mountains.get_height()

# Set up the drawing window
screen = pygame.display.set_mode([mountainWidth, mountainHeight])


ply = 300
px = 250
vel_x = 10
vel_y = 10

move_left = False
move_right = False
stepIndex = 0

