#This file is for global variables etc that are needed throughout the program
import pygame

clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# Set up the drawing window
screen = pygame.display.set_mode([700, 398])
#images
playerImgR = pygame.image.load('playerImgR.png')
playerImgL = pygame.image.load('playerImgL.png')
jumpingImg = pygame.image.load('jumping.png')
mountains = pygame.image.load('mountains.jpg')

y_gravity = 1
jump_height = 20
y_velocity = jump_height
