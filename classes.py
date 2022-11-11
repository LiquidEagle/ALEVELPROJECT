#This file contains the TWO classes used in the game
import pygame
from config import *


class Player:
    def __init__(self, x, y):
        self.dir = "right"
        self.x = x
        X_POSITION = x
        self.y = y
        Y_POSITION = y
        self.size = playerImgR.get_size()
        # create a 2x bigger image than self.image
        self.smaller_imgR = pygame.transform.scale(
            playerImgR, (int(self.size[0] / 20), int(self.size[1] / 20)))
        self.smaller_imgL = pygame.transform.scale(
            playerImgL, (int(self.size[0] / 20), int(self.size[1] / 20)))
        #self.jumping_img = pygame.transform.scale(
        #jumpingImg, (int(self.size[0] / 20), int(self.size[1] / 20)))
    def drawR(self):
        #draw bigger Right image to screen at x=100 y=100 position
        screen.blit(self.smaller_imgR, (self.x, self.y))

    def drawL(self):
        #draw bigger Left image to screen at x=100 y=100 position
        screen.blit(self.smaller_imgL, (self.x, self.y))

    def jumping(self):
        #draw bigger Left image to screen at x=100 y=100 position
        screen.blit(self.jumping_img, (self.x, self.y))

    def move(self, speed):  # input the speed
        if self.x > 500 - 30:  # if above 500 - 30 turn left
            self.dir = "left"
            self.y = self.y + 30
            return dir
        if self.x < 0:  #if below 0 turn right
            self.dir = "right"
            self.y = self.y + 30  #

        if self.dir == "right":
            self.x = self.x + speed  # changes the x value to turn right

        if self.dir == "left":
            self.x = self.x - speed  # changes the y value to turn left)


class Mountain:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(mountains, (self.x, self.y))
