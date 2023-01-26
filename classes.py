import pygame
from config import *


class Buttons():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.has_clicked = False

    def draw(self):
        is_clicked = False
        # get mouse pos
        pos = pygame.mouse.get_pos()

        # check if mouse is over button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.has_clicked == False:  # 0 = LMB
                is_clicked = True
                self.has_clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.has_clicked = False
        screen.blit(self.image, self.rect)
        return is_clicked


class Player:
    def __init__(self, x, y):
        self.has_reset(x, y)

    def draw_game(self):
        global left, right, px, ply, vel_y
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

        # create an outline around the player
        pygame.draw.rect(screen, WHITE, self.rect, 2)

    def update_player(self, game_over):
        global standing, dead_img
        dy = 0
        dx = 0

        if game_over == 0:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE] and self.isJump == False and self.jumping == False:
                self.vel_y = -15
                self.isJump = True
            if keys_pressed[pygame.K_SPACE] == False:
                self.isJump = False
            if keys_pressed[pygame.K_LEFT]:
                dx -= 5
                self.move_left = True
                self.move_right = False

            elif keys_pressed[pygame.K_RIGHT]:
                dx += 5
                self.move_left = False
                self.move_right = True
            else:
                self.move_left = False
                self.move_right = False
                self.stepIndex = 0

            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # collision detection
            world = World(world_data)
            self.jumping = True
            for tile in world.tile_list:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # check for y collison (tile stored in 1 and image in 0)
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below ground (jumping)
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground (falling)
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.jumping = False

            # check for collision with danger or enemies
            if pygame.sprite.spritecollide(self, World.blob_group, False):
                game_over = -1
                print(game_over)
            if pygame.sprite.spritecollide(self, world.lava_group, False):
                game_over = -1
                print(game_over)

            self.rect.x += dx
            self.rect.y += dy
        elif game_over == -1:
            dead_img = pygame.transform.scale(dead_img, (tile_size, tile_size))
            screen.blit(dead_img, (self.rect.x + 5, self.rect.y))

            if self.rect.y >= 250:
                self.rect.y -= 5

        return game_over  # cant make game_over simply 'global' as it must return value at the time of action

    def jump(self):

        # global isJump, jumpCount, JUMPHEIGHT
        # #start jumping
        # keys_pressed = pygame.key.get_pressed()
        # if keys_pressed[pygame.K_SPACE]:
        # 	isJump = True

        # followed this section of the tutorial here
        # https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
        # its not very OOP but it works
        # if isJump:
        # 	if jumpCount >= JUMPHEIGHT * -1:
        # 		self.rect.y -= (jumpCount * abs(jumpCount)) * 0.5
        # 		jumpCount -= 1
        # 	else: # This will execute if our jump is finished
        # 		jumpCount = JUMPHEIGHT
        # 		isJump = False
        # 		#resetting the variables
        pass

    def has_reset(self, x, y):
        self.stepIndex = 0
        self.imageR = right[self.stepIndex]
        self.imageL = left[self.stepIndex]
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


class Mountain:
    global tile_size

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(mountains, (self.x, self.y))


class World:
    blob_group = pygame.sprite.Group()
    def __init__(self, data):
        self.tile_list = []
        row_count = 0

        self.lava_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
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
                    blob = Enemy(column_count * tile_size, row_count * tile_size)
                    self.blob_group.add(blob)
                if tile == 6:
                    lava = Danger(column_count * tile_size, row_count * tile_size + int((tile_size / 2)))
                    self.lava_group.add(lava)
                if tile == 7:
                    platform = Platform(column_count * tile_size, row_count * tile_size + int((tile_size / 2)),0,1)
                    self.platform_group.add(platform)

                # where the instances are on the map
                column_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/blob.png')
        self.image = pygame.transform.scale(self.image, (51, 47))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = 1
        self.counter = 0

    def update(self):
        self.rect.x += self.dir
        self.counter += 1
        pygame.draw.rect(screen, WHITE, self.rect, 2)
        if abs(self.counter) > 50:
            # checks for absolute value, so even if the counter is negative it will return a positive value
            self.dir *= -1  # turn left when couter is above 50
            self.counter *= -1  # reset the counter

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,moveright,moveleft):
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
        self.rect.x +=self.dir
        self.count += 1
        if abs(self.count) > 50:
            # checks for absolute value, so even if the counter is negative it will return a positive value
            self.dir *= -1  # turn left when couter is above 50
            self.count *= -1  # reset the counter

class Danger(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('assets/lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Weapons():
    pass
# def __init__(self, x,y):
# 	self.image = pygame.image.load('assets/')
# 	self.rect = self.image.get_rect()
