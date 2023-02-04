import pygame
from config import *  # this contains all the global level variables across the files - its imported into all the files
from classes import *  # this imports the two classes from the classes.py
import databaseActions  # all database actions are here


# 700, 398
# main Pygame drawing loop function
def pygame_start():
    pygame.init()
    global vel_y, game_over, world

    # set variable locations
    mountain = Mountain(0, 0)
    user = Player(px, ply)
    #world = World(world_data)
    restart = Buttons(screen_width // 2 - 60, screen_height // 2, restart_img)

    def draw_grid():
        for line in range(0, 20):
            pygame.draw.line(screen, WHITE, (0, line * tile_size), (screen_width, line * tile_size))
            pygame.draw.line(screen, WHITE, (line * tile_size, 0), (line * tile_size, screen_height))

    done = True
    while done:
        for event in pygame.event.get():
            # check for closing window 
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
        screen.fill(0)
        clock.tick(60)
        # draw background
        mountain.draw()
        world.draw()

        #draw grid (temp)
        #draw_grid()

        if game_over == 0:
            blob_group.update()
            user.draw_game()
        platform_group.update()
        

        
        # draw groups
        blob_group.draw(screen)
        platform_group.draw(screen)
        lava_group.draw(screen)
        door_group.draw(screen)
        weapon_group.draw(screen)

        game_over = user.update_player(game_over)

        if game_over == -1:
            if restart.draw():
                user.has_reset(px, ply) # if player dead draw the buttons
                game_over = 0
                
        # flip the pygame display
        pygame.display.flip()
        # frames per second
        
        #screen.fill(BLACK)


# --------------------------------------------------


# Start OptionMenu
options = input(
    "Do you want to: \n (A) Create a new account \n (B) Login \n (C) Create Database \n Input Answer: ").upper()

if options == "A":
    databaseActions.register()  # register  is in databaseActions.py
elif options == "C":
    databaseActions.createDBandTable()  # createDBandTable  is in databaseActions.py
elif options == "B":
    while databaseActions.login() == False:  # createDBandTable function is in databaseActions.py
        print("Please try again")
    pygame_start()

