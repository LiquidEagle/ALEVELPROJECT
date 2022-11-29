#This file contains the TWO classes used in the game
import pygame
from config import *
  
class Player:
	def __init__(self, x, y):
		self.dir = "right"
		self.x = x
		self.y = y
		#self.size = playerImgR.get_size()
	def draw_game(self):
		global stepIndex
		global move_left, move_right, left, right
		if stepIndex >=9:
			stepIndex = 0
		if move_left == True:
			screen.blit(left[stepIndex], (self.x, self.y))	
			print(left[stepIndex])
			stepIndex += 1
		elif move_right == True:
			screen.blit(right[stepIndex], (self.x, self.y))
			stepIndex += 1
		else:
			screen.blit(standing, (self.x, self.y))

	def drawR(self):
		#draw bigger Right image to screen at x=100 y=100 position
		#screen.blit(playerImgR, (self.x, self.y))
		pass
		
	def drawL(self):
		#draw bigger Left image to screen at x=100 y=100 position
		#screen.blit(playerImgL, (self.x, self.y))
		pass
	
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
