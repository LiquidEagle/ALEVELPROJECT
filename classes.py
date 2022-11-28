#This file contains the TWO classes used in the game
import pygame
from config import *

class Player:
	def __init__(self, x, y):
		self.dir = "right"
		self.x = x
		self.y = y
		self.size = playerImgR.get_size()
		# create a 2x bigger image than self.image
		self.smaller_imgR = pygame.transform.scale(playerImgR, (int(self.size[0] / 20), int(self.size[1] / 20)))
		self.smaller_imgL = pygame.transform.scale(playerImgL, (int(self.size[0] / 20), int(self.size[1] / 20)))
		#self.jumping_img = pygame.transform.scale(
		#jumpingImg, (int(self.size[0] / 20), int(self.size[1] / 20)))
	def drawR(self):
		#draw bigger Right image to screen at x=100 y=100 position
		screen.blit(self.smaller_imgR, (self.x, self.y))
		
	def drawL(self):
		#draw bigger Left image to screen at x=100 y=100 position
		screen.blit(self.smaller_imgL, (self.x, self.y))
	
	#def move(self, speed):  # input the speed
		
	def jumpOLD(self):
			global vel_y, vel_x
			print(self.y)
			self.y -= vel_y
			vel_y -=1 
			if vel_y < -10:
				vel_y = 10

	def jump(self):
			#not used - jumping is done in main.py
			pass

class Mountain:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(mountains, (self.x, self.y))
