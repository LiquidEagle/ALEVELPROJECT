import pygame
from  config import *  #this contains all the global level variables across the files - its imported into all the files
from classes import Player,Mountain #this imports the two classes from the classes.py
import databaseActions #all database actions are here

#main Pygame drawing loop function
def pygame_start():
  pygame.init()
  mountain = Mountain(0, 50)
  user = Player(0, 455)   
  done = False
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
 
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:  
            user.dir = "right"
            user.x = user.x + 10
            print("Moving Right!")   
          
        if event.key == pygame.K_LEFT: 
            user.x = user.x - 10
            user.dir = "left"
            print("Moving Left!")    
          
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
      jumping = True

    if jumping:
      y_position -= y_velocity
      y_velocity -= y_gravity
      if y_velocity < -JUMP_HEIGHT:
        jumping = False
        y_velocity = jump_height
      screen.blit(jumping_img, (self.x, self.y)) 
    else:
      user.drawL() 
      
    mountain.draw()  
    
    if user.dir=="left":
      user.drawL()
    elif user.dir=="right":
      user.drawR()       
    
    pygame.display.flip()

    clock.tick(17)
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
        






