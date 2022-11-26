import pygame
from  config import *  #this contains all the global level variables across the files - its imported into all the files
from classes import * #this imports the two classes from the classes.py
import databaseActions #all database actions are here

#700, 398

#main Pygame drawing loop function
def pygame_start():
  pygame.init()
  mountain = Mountain(0, 0)
  global ply
  global px
  global vel_y
  global vel_x
  global height
  global width
  user = Player(px, ply)  
  width =  user.smaller_imgR.get_width()
  height = user.smaller_imgR.get_height()
  done = False
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT] and user.x < mountainWidth - width - vel_x:  
      user.dir = "right"
      user.x = user.x + vel_x
          
    if keys_pressed[pygame.K_LEFT] and user.x > vel_x:
      user.x = user.x - vel_x
      user.dir = "left"  

    jump = False
    
    if keys_pressed[pygame.K_SPACE]:
      jump = True

    if jump is True:
      user.y -= vel_y
      vel_y -=1 
      if vel_y < -10:
        jump = False 
        vel_y = 10  

#    if jumping:
#      Player.y -= y_velocity
#      y_velocity -= y_gravity
#      if y_velocity < -jump_height:
#        jumping = False
#        y_velocity = jump_height
#        user.jumping()       
        
  
      
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
        





