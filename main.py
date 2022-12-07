import pygame
from config import *  # this contains all the global level variables across the files - its imported into all the files
from classes import *  # this imports the two classes from the classes.py
import databaseActions  # all database actions are here


# 700, 398
# main Pygame drawing loop function
def pygame_start():
    pygame.init()
    global world, vel_y, dy, dx, isJump
    # set variable locations
    mountain = Mountain(0, 0)
    user = Player(px, ply)

    world = World(world_data)  # test

    def draw_grid():
        for line in range(0, 20):
            pygame.draw.line(screen, WHITE, (0, line * tile_size), (screen_width, line * tile_size))
            pygame.draw.line(screen, WHITE, (line * tile_size, 0), (line * tile_size, screen_height))

    done = True
    while done:

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE] and isJump == False:
            vel_y = -15
            isJump = True
        if keys_pressed[pygame.K_SPACE] == False:
            isJump = False
        if keys_pressed[pygame.K_LEFT] and user.rect.x > dx:
            user.rect.x -= dx
            user.move_left = True
            user.move_right = False

        elif keys_pressed[pygame.K_RIGHT] and user.rect.x < mountainWidth - user.width - dx:
            user.rect.x += dx
            user.move_left = False
            user.move_right = True
        else:
            user.move_left = False
            user.move_right = False
            user.stepIndex = 0

        vel_y += 1
        if vel_y > 10:
            vel_y = 10

        dy += vel_y
        user.rect.y += dy
        # temp
        # if user.rect.bottom > screen_height:
        #     user.rect.bottom = screen_height
        #     dy = 0

        # for tile in world.tile_list:
        #     # check for collision in x direction
        #     if tile[1].colliderect(user.rect.x + dx, user.rect.y, user.width, user.height):
        #         dx = 0
        for tile in world.tile_list:
            # check for y collison (tile stored in 1 and image in 0)
            if tile[1].colliderect(user.rect.x, user.rect.y + dy, user.width, user.height):
                # check if below ground (jumping)
                if vel_y < 0:
                    dy = tile[1].bottom - user.rect.top
                    vel_y = 0
                elif vel_y >= 0:
                    dy = tile[1].top - user.rect.bottom
                    vel_y = 0
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()



        # draw background
        mountain.draw()
        world.draw()
        draw_grid()

        # draw player
        user.draw_game()
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
