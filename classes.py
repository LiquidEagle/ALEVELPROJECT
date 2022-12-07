import pygame
from config import *

class Player:
	def __init__(self, x, y):
		self.stepIndex = 0
		self.imageR = right[self.stepIndex]
		self.imageL = left[self.stepIndex]
		self.rectR = self.imageR.get_rect()
		self.rectL = self.imageL.get_rect()
		self.rect = self.imageR.get_rect() # GET STANDING IMAGE RECTANGLE
		self.rect.x = x
		self.rect.y = y
		self.width = self.imageR.get_width() # GET WIDTH
		self.height = self.imageR.get_height() # GET HEIGHT
		self.move_left = False
		self.move_right = False

	def draw_game(self):
		global left, right, tile, px, ply, vel_y
		if self.stepIndex >=9:
			self.stepIndex = 0
		if self.move_left:
			screen.blit(left[self.stepIndex], (self.rect.x, self.rect.y))	
			self.stepIndex += 1
		elif self.move_right:
			screen.blit(right[self.stepIndex], (self.rect.x, self.rect.y))
			self.stepIndex += 1
		else:
			screen.blit(standing, (self.rect.x, self.rect.y))

		#create an outline around the player
		pygame.draw.rect(screen, WHITE, self.rect, 2)

		#collision detection
		
		
			
	def jump(self):
		pass
		# global isJump, jumpCount, JUMPHEIGHT
		# #start jumping
		# keys_pressed = pygame.key.get_pressed()
		# if keys_pressed[pygame.K_SPACE]:
		# 	isJump = True

		#followed this section of the tutorial here
		#https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
		# its not very OOP but it works
		# if isJump:
		# 	if jumpCount >= JUMPHEIGHT * -1:
		# 		self.rect.y -= (jumpCount * abs(jumpCount)) * 0.5
		# 		jumpCount -= 1
		# 	else: # This will execute if our jump is finished
		# 		jumpCount = JUMPHEIGHT
		# 		isJump = False
		# 		#resetting the variables


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