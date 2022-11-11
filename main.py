import pygame
from  config import *  #this contains all the global level variables across the files - its imported into all the files
from classes import * #this imports the two classes from the classes.py
import databaseActions #all database actions are here

#700, 398

#main Pygame drawing loop function
def pygame_start():
  pygame.init()
  mountain = Mountain(0, 0)
  user = Player(0, 355)  
  done = False
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT]:  
      user.dir = "right"
      user.x = user.x + 10
          
    if keys_pressed[pygame.K_LEFT]:
      user.x = user.x - 10
      user.dir = "left"   

    if keys_pressed[pygame.K_SPACE]:
      jumping = True
      
    jumping = False
    if jumping:
      Player.y -= y_velocity
      y_velocity -= y_gravity
      if y_velocity < -jump_height:
        jumping = False
        y_velocity = jump_height
        user.jumping()       
        
  
      
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
        






