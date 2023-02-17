from random import randint
import pygame as pg
from turtle import delay
from pygame.locals import *
import time

pg.init()

clock = pg.time.Clock()
fps = 60

screen_width, screen_height = pg.display.Info().current_w, pg.display.Info().current_h

screen = pg.display.set_mode((screen_width, screen_height))
screen.fill((253, 246, 227))
pg.display.set_caption("Lover")

tileSize = 40

def drawGrid():
    for line in range(0,28):
        pg.draw.line(screen, (209,203,184), (0, line*tileSize), (screen_width, line*tileSize))
    for line in range(0,48):
        pg.draw.line(screen, (209,203,184), (line*tileSize, 0), (line*tileSize, screen_height))

class Protector():
    def __init__(self, x, y):
        img = pg.image.load('D:\Coding\pythin\loverProject\image\char1.png')
        self.image1 = pg.transform.scale(img, (50, 80))
        img = pg.image.load('D:\Coding\pythin\loverProject\image\char2.png')
        self.image2 = pg.transform.scale(img, (50, 80))
        self.rect = self.image1.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.displayImage = self.image1

    def update(self):
        mousex, mousey = pg.mouse.get_pos()
        
        ay = (mousey - 35 - self.rect.y)/20

        if self.rect.x < mousex-20:
            self.displayImage = self.image1
            ax = (mousex - 10 - self.rect.x)/20
        else:
            ax = (mousex - 20 - self.rect.x)/20
            self.displayImage = self.image2


        self.rect.x += ax
        self.rect.y += ay

        if self.rect.colliderect(object.rect.topleft, (1,80)):
            self.rect.right = object.rect.left
        elif self.rect.colliderect(object.rect.topright, (1,80)):
            self.rect.left = object.rect.right
        elif self.rect.colliderect(object.rect.topleft, (50,1)):
            self.rect.bottom = object.rect.top
        elif self.rect.colliderect(object.rect.bottomleft, (50,1)):
            self.rect.top = object.rect.bottom

        screen.blit(self.displayImage, self.rect)


class Object():
    def __init__(self):
        img = pg.image.load('D:\Coding\pythin\loverProject\image\char3.png')
        self.image3 = pg.transform.scale(img, (50, 80))
        img = pg.image.load('D:\Coding\pythin\loverProject\image\char4.png')
        self.image4 = pg.transform.scale(img, (50, 80))
        self.rect = self.image3.get_rect()
        self.rect = self.image4.get_rect()
        self.rect.x = screen_width/2 - 25
        self.rect.y = screen_height/2 - 40
        self.displayImage = self.image3

        
    def update(self,x,y):
        if self.rect.x < x:
            self.displayImage = self.image3
        else: 
            self.displayImage = self.image4
        
        screen.blit(self.displayImage, self.rect)

class Attacker():
    def __init__(self):
        self.img = pg.image.load('D:\Coding\pythin\loverProject\image\heart.jpg')
        self.rect = self.img.get_rect()
        self.reset()
    
    def reset(self):
        rand = randint(1, 4)
        if rand == 1: 
            self.rect.x = 0
            self.rect.y = randint(0, screen_height)
        if rand == 2: 
            self.rect.x = screen_width
            self.rect.y = randint(0, screen_height)
        if rand == 3: 
            self.rect.y = 0
            self.rect.x = randint(0, screen_width)
        if rand == 4: 
            self.rect.y = screen_height
            self.rect.x = randint(0, screen_width)
            
        self.vx = (object.rect.x - self.rect.x + 25)/90
        self.vy = (object.rect.y - self.rect.y + 40)/90
        

    def update(self):
        global defend_point
        global miss_point
        if self.rect.colliderect(protector.rect):
            self.reset()
            defend_point += 1

        if self.rect.colliderect(object.rect):
            self.reset()    
            miss_point += 1

        self.rect.x += self.vx
        self.rect.y += self.vy

        screen.blit(self.img, self.rect)

def printText(text, x ,y, size):
    font = pg.font.SysFont("calibri", size, True, 0)
    surface = font.render(text, True, (0, 0, 0))
    screen.blit(surface, (x, y))

defend_point = 0
miss_point = 0

mousex, mousey = pg.mouse.get_pos()
protector = Protector(mousex, mousey) 
object = Object()
pg.mouse.set_visible(False)
attacker1 = Attacker()
attacker2 = Attacker()
run = True
while run:
    clock.tick(fps)
    screen.fill((253, 246, 227))
    printText(f"Defended: {defend_point}", 50   , 20, 20)
    printText(f"Missed: {miss_point}", 50, 60, 20)
    object.update(protector.rect.x, protector.rect.y)
    protector.update()
    attacker1.update()
    attacker2.update()
    turnOff = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

    pg.display.update()

screen.fill((253, 246, 227))
printText("Game Over", screen_width/2-screen_width/25, screen_height/2, 50)
pg.display.update()
time.sleep(1)

pg.quit()