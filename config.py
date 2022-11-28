#This file is for global variables etc that are needed throughout the program
import pygame

clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#images
playerImgR = pygame.image.load('playerImgR.png')
playerImgL = pygame.image.load('playerImgL.png')
jumpingImg = pygame.image.load('jumping.png')
mountains = pygame.image.load('mountains.jpg')



mountainWidth = mountains.get_width()
mountainHeight = mountains.get_height()

# Set up the drawing window
screen = pygame.display.set_mode([mountainWidth, mountainHeight])


ply = 355
px = 1
vel_x = 10
vel_y = 10


