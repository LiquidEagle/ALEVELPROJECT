# Simple pygame program
import pygame

# Import and initialize the pygame library

import sqlite3

#login code
#https://www.tutorialspoint.com/sqlite/sqlite_python.htm
#Useful online viewer: https://inloop.github.io/sqlite-viewer/

# establishing  a database connection
con = sqlite3.connect('alldata.db')
cursor = con.cursor()

clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


jumping = False
y_gravity = 1
jump_height = 20
y_velocity = jump_height

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

playerImgR = pygame.image.load('playerImgR.png')
playerImgL = pygame.image.load('playerImgL.png')
mountains = pygame.image.load('mountains.jpg')
jumpingImg = pygame.image.load('jumping.png')




def createDBandTable():
    con = sqlite3.connect('alldata.db')
    sql = """
  CREATE TABLE Logins(id INTEGER,
  username TEXT,
  password TEXT,
  PRIMARY KEY(id AUTOINCREMENT))
  """
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    return "database and table created"


rows = cursor.fetchall()
for row in rows:
    print(row)
    print(row[0])  # use this to print the first item
options = input(
    "\n Do you want to: \n (A) Create a new account \n (B) Login \n (C) Create Database \n Input Answer: "
).upper()

if options == "A":
    username = input("Create Username: ")
    password = input("Create Password: ")
    sql = 'INSERT INTO Logins (username,password) VALUES ("' + username + '","' + password + '");'
    print(sql)
    cursor.execute(sql)
    con.commit()

access = True

while access == False:
    if options == "B":
        username_login = input("Username: ")
        password_login = input("Password: ")
        statement = "SELECT * FROM Logins WHERE username = '" + username_login + "' AND password = '" + password_login + "'"
        cursor.execute(statement)
        if not cursor.fetchone():
            print("Login failed")
            access = False
        else:
            print("Welcome")
            access = True

if options == "C":
    createDBandTable()

class Mountain:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def draw(self):
    screen.blit(mountains, (self.x, self.y))

class Player:
  def __init__(self, x, y):
    self.dir = "right"
    self.x = x
    self.y = y
    self.size = playerImgR.get_size()
    # create a 2x bigger image than self.image
    self.smaller_imgR = pygame.transform.scale(
        playerImgR, (int(self.size[0] / 20), int(self.size[1] / 20)))
    self.smaller_imgL = pygame.transform.scale(
        playerImgL, (int(self.size[0] / 20), int(self.size[1] / 20)))
    #self.jumping_img = pygame.transform.scale(
        #jumpingImg, (int(self.size[0] / 20), int(self.size[1] / 20)))
  def drawR(self):
    #draw bigger Right image to screen at x=100 y=100 position
    screen.blit(self.smaller_imgR, (self.x, self.y))
  def drawL(self):
    #draw bigger Left image to screen at x=100 y=100 position
    screen.blit(self.smaller_imgL, (self.x, self.y))
  def jumping(self):
    #draw bigger Left image to screen at x=100 y=100 position
    screen.blit(self.jumping_img, (self.x, self.y))  
  def move(self, speed):  # input the speed
    if self.x > 500 - 30:  # if above 500 - 30 turn left
        self.dir = "left"
        self.y = self.y + 30
        return dir
    if self.x < 0:  #if below 0 turn right
        self.dir = "right"
        self.y = self.y + 30  #

    if self.dir == "right":
        self.x = self.x + speed  # changes the x value to turn right

    if self.dir == "left":
        self.x = self.x - speed  # changes the y value to turn left)

def pygame_start():
  pygame.init()
  global jumping
  #colours

    

  mountain = Mountain(0, 50)
  user = Player(0, 455)   
    #____________________ MAIN EVENTS START ___________________#

    # Run until the user asks to quit
  done = False
  while done == False:
        #----------------- CHECK FOR EVENTS START--------------------------      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
        
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:  # if right arrow pressed gun moves right
            user.dir = "right"
            user.x = user.x + 10
            print("Moving Right!")
              
        if event.key == pygame.K_LEFT:  # if left arrow pressed gun moves left
            user.x = user.x - 10
            user.dir = "left"
            print("Moving Left!")
              
        if event.key == pygame.K_SPACE:  # bullet is shot at a certain y distance where the gun is
            mainbullets.append(Bullet(spacegun.x, spacegun.y - 13))
            print("Jumping!")
    mountain.draw()        
    if user.dir=="left":
      user.drawL()
    elif user.dir=="right":
      user.drawR()       
    # Flip the display
    pygame.display.flip()

    clock.tick(17)
    screen.fill(BLACK)

# Done! Time to quit.
pygame.quit()


if access == True:
    pygame_start()
