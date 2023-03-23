import pygame
from config import *  # this contains all the global level variables across the files - its imported into all the files
from classes import *  # this imports the two classes from the classes.py
import databaseActions  # all database actions are here

# 700, 398
# main Pygame drawing loop function
def pygame_start():
    pygame.init()
    global vel_y, game_over, world, mainbullets, weapon_picked, health, enemy_health

    # set variable locations
    mountain = Mountain(0, 0)
    user = Player(px, ply)
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
            enemy_group.update()
            user.draw_game()
            platform_group.update()
        # for bul in mainbullets:
        #     if bul.rect.y - 6 < blob_group.rect.y + blob_group.height and bul.rect.y + 6 > blob_group.rect.y:  # Checks x coords
        #         if bul.rect.x + 6 > blob_group.rect.x and bul.x - 6 < blob_group.rect.x + blob_group.width: # Checks y coords
        #             health -= 1  # calls enemy hit method
        #             mainbullets.remove(bul)  # removes bullet from bullet list
        # DOESN'T WORK I HATE PYGAME SO MUCH AND THIS STUPID COLLISION DETECTION BS
        # kill enemy when hit 10 times

        for bul in mainbullets:
            if pygame.sprite.spritecollide(bul, enemy_group, False):
                print("Enemy health: " + str(enemy_health))
                enemy_health -=1
                mainbullets.remove(bul)
            if enemy_health ==0:
                pygame.sprite.spritecollide(bul, enemy_group, True)
            for tile in world.tile_list:
                # check for collision in x direction
                if tile[1].colliderect(bul.rect.x, bul.rect.y, bul.width, bul.height):
                    mainbullets.remove(bul)

        
        # draw groups
        enemy_group.draw(screen)
        platform_group.draw(screen)
        lava_group.draw(screen)
        door_group.draw(screen)
        weapon_group.draw(screen)

        game_over = user.update_player(game_over)

        if game_over == -1:
            if restart.draw():
                user.has_reset(px, ply) # if player dead draw the buttons
                game_over = 0
        
        for bul in mainbullets:
                if bul.rect.x < screen_width and bul.rect.x > 0:
                        bul.draw()
                        bul.rect.x += 10 * user.dir
                else:
                    mainbullets.remove(bul)

                
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
    while databaseActions.login() == False:  # login function is in databaseActions.py
        print("Please try again")
    pygame_start()

