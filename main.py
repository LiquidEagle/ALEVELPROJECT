import pygame
from config import *  # this contains all the global level variables across the files - its imported into all the files
from classes import *  # this imports the two classes from the classes.py
import databaseActions  # all database actions are here


# 700, 398
# main Pygame drawing loop function
def pygame_start():
    pygame.init()
    global world, vel_y, dy, game_over, restart_img

    # set variable locations
    mountain = Mountain(0, 0)
    user = Player(px, ply)
    world = World(world_data)
    restart = Buttons(screen_width // 2 - 60, screen_height // 2, restart_img)

    def draw_grid():
        for line in range(0, 20):
            pygame.draw.line(screen, WHITE, (0, line * tile_size), (screen_width, line * tile_size))
            pygame.draw.line(screen, WHITE, (line * tile_size, 0), (line * tile_size, screen_height))

    done = True
    while done:
        # temp
        if user.rect.bottom > screen_height:
            user.rect.bottom = screen_height
            dy = 0

        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()

        # draw background
        mountain.draw()
        world.draw()

        #draw grid (temp)
        draw_grid()

        if game_over == 0:
            world.blob_group.update()
            user.draw_game()
            
        #draw blob
        world.blob_group.draw(screen)
        
        # draw player
        
        game_over = user.update_player(game_over)

        if game_over == -1:
            if restart.draw():
                user.has_reset(px, ply) # if player dead draw the buttons
                game_over = 0

        #draw danger areas
        world.lava_group.draw(screen)

        # jump if space is pressed
        # user.jump()
        # flip the pygame display
        pygame.display.flip()

        # frames per second
        clock.tick(30)
        screen.fill(BLACK)


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
