import pygame
from config import *


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def is_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self):
        if self.is_mouse_over() and pygame.mouse.get_pressed()[0]:
            self.clicked = True
        else:
            self.clicked = False
        

    def draw(self):
        screen.blit(self.image, self.rect)
        return self.clicked


class Player:
    def __init__(self, x, y):
        self.has_reset(x, y)

    def draw_game(self):
        global left, right, px, ply, vel_y, is_standing
        # if self.count > 9:
        #     self.count = 0
        #     self.stepIndex +=1
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.move_left:
            screen.blit(left[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        elif self.move_right:
            screen.blit(right[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        else:
            screen.blit(standing, (self.rect.x, self.rect.y))
            is_standing = True

        # create an outline around the player
        pygame.draw.rect(screen, WHITE, self.rect, 2)

    def update_player(self, game_over):
        global standing, dead_img, weapon_picked, picR, picL, gun_playerR, gun_playerL
        dy = 0
        dx = 0

        if game_over == 0:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_a]:
                if self.move_left:
                    self.dir = -1
                else:
                    self.dir = 1
                if weapon_picked == 1:
                    if len(mainbullets) < 5:
                        mainbullets.append(Bullet(self.rect.x - 15, self.rect.y))
            if keys_pressed[pygame.K_SPACE] and self.isJump == False and self.jumping == False:
                self.vel_y = -15
                self.isJump = True
            if keys_pressed[pygame.K_SPACE] == False:
                self.isJump = False
            if keys_pressed[pygame.K_LEFT]:
                dx -= 5
                self.move_left = True
                self.move_right = False
            if keys_pressed[pygame.K_RIGHT]:
                dx += 5
                self.move_left = False
                self.move_right = True
            if keys_pressed[pygame.K_LEFT] == False and keys_pressed[pygame.K_RIGHT] == False:
                self.move_left = False
                self.move_right = False
                self.stepIndex = 0
            
            self.vel_y += 1
            if self.vel_y > 15:
                self.vel_y = 15
            dy += self.vel_y
            
            # check for collision with danger or enemies
            if pygame.sprite.spritecollide(self, enemy_group, False):
                game_over = -1
                print("you hit the enemy")
                print(game_over)
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1
                print(game_over)
            if pygame.sprite.spritecollide(self, platform_group, False):
                print("collided with platform ! ! ! !")
            if pygame.sprite.spritecollide(self, weapon_group, False):
                weapon_picked = 1
                print("collided with weapon")
                picR = gun_playerR
                picL = gun_playerL
                print(picR)
            if weapon_picked == 1:
                pygame.sprite.spritecollide(self, weapon_group, True)
            # check for collision with door to end the game and say player has won.
            if pygame.sprite.spritecollide(self, door_group, False):
                game_over = 1
                print("You have won the game!")
            
            # collision detection
            self.jumping = True
            for tile in world.tile_list: 
                tile_rect = pygame.Rect(tile[1]) #(tile stored in 1 and image in 0)
                # check collision in x direction
                if tile_rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):  
                    # if the player is moving right and there is a collision, set player's right to tile's left 
                    if dx > 0:
                        self.rect.right = tile_rect.left
                    # if the player is moving left and there is a collision, set player's left to tile's right
                    elif dx < 0:
                        self.rect.left = tile_rect.right   
                    dx = 0 # stop the player's movement in x direction
                
                # check collision in y direction
                if tile_rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # if the player is falling and there is a collision, set player's bottom to tile's top
                    if dy > 0:
                        self.rect.bottom = tile_rect.top
                        self.vel_y = 0
                        self.jumping = False
                    # if the player is jumping and there is a collision, set player's top to tile's bottom
                    elif dy < 0:
                        self.rect.top = tile_rect.bottom + 10
                        self.vel_y = 0
                    
                    # set the change in y to 0 or less if there is a collision in y direction
                    dy = min(dy, 0)



            self.rect.x += dx
            self.rect.y += dy

            for platform in platform_group:
                # check for collision in x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # check for y collison (tile stored in 1 and image in 0)
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the platform and collide with the movement of the platform
                    self.rect.x += platform.dir
                    if abs((self.rect.top + dy) - platform.rect.top) < 20:
                        dy = platform.rect.bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < 20:
                        self.rect.bottom = platform.rect.top
                        self.vel_y = 0
                        self.jumping = False
        elif game_over == -1:
            dead_img = pygame.transform.scale(dead_img, (tile_size, tile_size))
            screen.blit(dead_img, (self.rect.x + 5, self.rect.y))

            if self.rect.y >= 250:
                self.rect.y -= 5

        return game_over  # returns the value of game_over via the update_player function

    def has_reset(self, x, y):
        self.stepIndex = 0
        self.count = 0
        self.imageR = right[self.stepIndex]
        self.imageL = left[self.stepIndex]
        # self.gunR = gunR[self.stepIndex]
        self.rect = standing.get_rect()  # GET STANDING IMAGE RECTANGLE
        self.rect.x = x
        self.rect.y = y
        self.width = standing.get_width()  # GET WIDTH
        self.height = standing.get_height()  # GET HEIGHT
        self.move_left = False
        self.move_right = False
        self.vel_y = 0
        self.isJump = False  # check if player is jumping
        self.jumping = False  # check if player is in the air
        self.dir = 0


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
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    enemy = Enemy(column_count * tile_size, row_count * tile_size)
                    enemy_group.add(enemy)
                if tile == 4:
                    weapon = Weapons(column_count * tile_size, row_count * tile_size)
                    weapon_group.add(weapon)
                if tile == 6:
                    lava = Danger(column_count * tile_size, row_count * tile_size + int((tile_size / 2)))
                    lava_group.add(lava)
                if tile == 7:
                    platform = Platform(column_count * tile_size, row_count * tile_size + int((tile_size / 2)), 0, 1)
                    platform_group.add(platform)
                if tile == 8:
                    door = Door(column_count * tile_size, row_count * tile_size)
                    door_group.add(door)

                # where the instances are on the map
                column_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(self.image, (51, 47))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = -1
        self.counter = 0

    def update(self):
        self.rect.x += self.dir
        self.counter += 1
        # pygame.draw.rect(screen, WHITE, self.rect, 2)
        if abs(self.counter) > 50:
            self.dir *= -1  # turn left when counter is above 50.
            # ^ this is done by multiplying dir by -1, therefore if dir is -1 it will turn to +1 (-1 * -1 = 1)
            self.counter *= -1
            # ^ reset the counter by flipping the counter, so the enemy can move to the left of its origin.
            self.image = pygame.transform.flip(self.image, True, False)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, moveright, moveleft):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('assets/platform.png')
        self.image = pygame.transform.scale(image, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = 1
        self.count = 0
        self.mover = moveright
        self.movel = moveleft

    def update(self):
        self.rect.x += self.dir
        self.count += 1
        if abs(self.count) > 25:
            self.dir *= -1  # turn left when counter is above 25
            # ^ this is done by multiplying dir by -1, therefore if dir is -1 it will turn to +1 (-1 * -1 = 1)
            self.count *= -1
            # ^ reset the counter by flipping the counter, so the platform can move to the left of its origin.


class Danger(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('assets/lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('assets/door.png')
        self.image = pygame.transform.scale(image, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Weapons(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('assets/gun.png')
        self.image = pygame.transform.scale(image, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Bullet():
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/bulletimg.png')
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.rect.x = x
        self.rect.y = y
        self.height = self.image.get_height()
        self.width = self.image.get_width()


    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
weapon_group = pygame.sprite.Group()
world = World(world_data)
