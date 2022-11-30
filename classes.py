#This file contains the TWO classes used in the game
import pygame
from config import *
  
class Player:
	def __init__(self, x, y):
		self.dir = "right"
		self.x = x
		self.y = y
		self.move_left = False
		self.move_right = False
		self.stepIndex = 0
		
	def draw_game(self):
		global left, right
		if self.stepIndex >=9:
			self.stepIndex = 0
		if self.move_left:
			screen.blit(left[self.stepIndex], (self.x, self.y))	
			self.stepIndex += 1
		elif self.move_right:
			screen.blit(right[self.stepIndex], (self.x, self.y))
			self.stepIndex += 1
		else:
			screen.blit(standing, (self.x, self.y))

	def jump(self):
			#not used - jumping is done in main.py
			pass

class Platform:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def draw(self):
		pygame.draw.rect(screen,GREEN,pygame.Rect(self.x, self.y, 60, 60))


class Mountain:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(mountains, (self.x, self.y))
