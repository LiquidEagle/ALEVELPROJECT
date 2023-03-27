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
normal_playerR = 'R'
gun_playerR = 'RG'
normal_playerL = 'L'
gun_playerL = 'LG'

picR = normal_playerR
picL = normal_playerL

right = [None]*10
for rpic in range(1,10):
    right[rpic-1] = pygame.image.load(os.path.join('assets', picR + str(rpic) + '.png'))
    rpic += 1

left = [None]*10
for lpic in range(1,10):
    left[lpic-1] = pygame.image.load(os.path.join('assets', picL + str(lpic) + '.png'))
    lpic += 1


#load all images
Rimg = pygame.image.load('assets/R1.png')
Limg = pygame.image.load('assets/L1.png')
standing = pygame.image.load('assets/standing.png')

mountains = pygame.image.load('assets/snow.png')
mountains = pygame.transform.scale(mountains, (1000,1000))
dirt_img = pygame.image.load('assets/dirt2.png')
grass_img = pygame.image.load('assets/grass2.png')
dead_img = pygame.image.load('assets/dead.png')
restart_img = pygame.image.load('assets/restart.png')
restart_img = pygame.transform.scale(restart_img, (120,50))
won_img = pygame.image.load('assets/won.png')
won_img = pygame.transform.scale(won_img, (120,200))

mountainWidth = mountains.get_width()
mountainHeight = mountains.get_height()
screen_width = 1000
screen_height = 1000

# Set up the drawing window
screen = pygame.display.set_mode([mountainWidth, mountainHeight])
pygame.display.set_caption("Platformer Game")

#enemy attributes
enemy_health = 10

#player attributes
ply = screen_width -800
px = 100
mainbullets = []
JUMPHEIGHT = 5
jumpCount = JUMPHEIGHT
health = 10

#tile attributes
tile_size = 50
weapon_picked = 0

#game attributes
game_over = 0

world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 2, 0, 7, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 7, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 2, 0, 7, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 7, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 1, 1],
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


