import pygame as pg
from Name import *
from random import randint

class Villager():
    def __init__(self, gender, name, posx, posy):
        img = pg.image.load(f'D:\Coding\pythin\cardProject\image\Villager1.png')
        self.image1 = pg.transform.scale(img, (100, 150))
        img = pg.image.load(f'D:\Coding\pythin\cardProject\image\Villager2.png')
        self.image2 = pg.transform.scale(img, (100, 150))
        self.rect = self.image1.get_rect()
        self.rect.x = posx 
        self.rect.y = posy

        self.attack = 2
        self.hp = 12
        self.age = 5
        self.gender = gender
        self.name  = name
        self.job = "Villager"
        self.equipment = []

        
        self.velocity = 5
        self.velx = 0
        self.vely = 0
        self.desx = posx
        self.desy = posy

        self.countdown = 0
        self.isWorking = False
        self.isMove = False
        self.partner = None


        if self.gender == "Male":
            self.displayImage = self.image1
        else: self.displayImage = self.image2
        
    def move(self):
        if self.desx != self.rect.x:
            if self.desx > self.rect.x + self.velx:
                self.rect.x += self.velx
            elif self.desx < self.rect.x - self.velx:
                self.rect.x -= self.velx
            else: self.rect.x += self.desx - self.rect.x

        if self.desy != self.rect.y:    
            if self.desy > self.rect.y + self.vely:
                self.rect.y += self.vely
            elif self.desy < self.rect.y - self.vely:
                self.rect.y -= self.vely
            else: self.rect.y += self.desy - self.rect.y
        
        if [self.rect.x, self.rect.y] == [self.desx, self.desy]: 
            self.isMove = False
    
    def showInfo(self ,screen, size):
        font = pg.font.SysFont("calibri", size, True, 0)
        surface1 = pg.image.load(f'D:\Coding\pythin\cardProject\image\Info.png')
        screen.blit(surface1, (48, 80))
        infos = [self.name, str(self.age), str(self.hp), self.gender]
        for i in range (len(infos)):
            surface2 = font.render(info[i]+infos[i], True, (0, 0, 0))
            screen.blit(surface2, (45, 80+(i)*30))
        

    def update(self, screen):
        if self.isWorking == True :
            self.countdown -= 1
        
        screen.blit(self.displayImage, self.rect)

        self.move()
    



        
class Corpse():
    def __init__(self) -> None:
        pass