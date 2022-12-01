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
		self.imageR = right[self.stepIndex]
		self.rectR = self.imageR.get_rect()
		self.imageL = left[self.stepIndex]
		self.rectL = self.imageL.get_rect()
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
	
class Platform:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Mountain:
	global tile_size
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw(self):
		screen.blit(mountains, (self.x, self.y))

class World:
	def __init__(self, data):
		self.tile_list = []

		row_count = 0
		for row in data:
			column_count = 0
			for tile in row:
				if tile ==1:
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = column_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile ==2:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = column_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				column_count += 1
			row_count += 1
	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])