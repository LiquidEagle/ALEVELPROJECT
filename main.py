import pygame
from  config import *  #this contains all the global level variables across the files - its imported into all the files
from classes import * #this imports the two classes from the classes.py
import databaseActions #all database actions are here

#700, 398


#main Pygame drawing loop function
def pygame_start():
	pygame.init()
	mountain = Mountain(0, 0)
	user = Player(px, ply)  
	width =  standing.get_width()
	height = standing.get_height()
	isJump = False
	JUMPHEIGHT = 6
	jumpCount = JUMPHEIGHT
	global move_left, move_right, stepIndex
	
	done = True
	while done:    
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT] and user.x < mountainWidth - width - vel_x:
      print("hello")
			user.x += vel_x
			move_left = False
			move_right = True

      
		elif keys_pressed[pygame.K_LEFT] and user.x > vel_x:
			user.x -= vel_x
			move_left = True
			move_right = False 
		else:
			move_left = False
			move_right = False
			stepIndex = 0
		
		

		#start jumping
		if keys_pressed[pygame.K_SPACE]:
			isJump = True
		for event in pygame.event.get():
			#check for closing window
			if event.type == pygame.QUIT:
				pygame.quit()
			
	
		
		# draw background 
		mountain.draw()  

		#draw player
		user.draw_game()
		#if user.dir=="left":
		#	user.drawL()
		#elif user.dir=="right":
		#	user.drawR() 
		
		#followed this section of the tutorial here
		#https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
		# its not very OOP but it works
		if isJump:
			if jumpCount >= JUMPHEIGHT * -1:
				user.y -= (jumpCount * abs(jumpCount)) * 0.5
				jumpCount -= 1
			else: # This will execute if our jump is finished
				jumpCount = JUMPHEIGHT
				isJump = False
				#resetting the variables
			 
		
		pygame.display.flip()
		
		clock.tick(60)
		screen.fill(BLACK)


#--------------------------------------------------


#Start OptionMenu
options = input("Do you want to: \n (A) Create a new account \n (B) Login \n (C) Create Database \n Input Answer: ").upper()

if options == "A":
    databaseActions.register() #register  is in databaseActions.py
elif options == "C":
    databaseActions.createDBandTable() #createDBandTable  is in databaseActions.py
elif options == "B":
  while databaseActions.login() == False: #createDBandTable function is in databaseActions.py
    print("try again")
  pygame_start()
        





