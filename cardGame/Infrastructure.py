import pygame as pg
import Name
from Human import *

class House():
    def __init__(self, posx, posy):
        img = pg.image.load(f'D:\Coding\pythin\cardProject\image\House.png')
        self.image = pg.transform.scale(img, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.x = posx 
        self.rect.y = posy
        self.interior = []
        self.producting = -1

    def stay(self, person, human):
        if len(self.interior) < 2:
            person.rect.x = self.rect.x + 105*(len(self.interior)+1)
            person.rect.y = self.rect.y
            person.desx = person.rect.x
            person.desy = person.rect.y
            self.interior.append(person)
            human.remove(person)
        if len(self.interior) == 2:
            self.producting = 600
        else: self.producting = -1
        

    def update(self, screen, human):      
        screen.blit(self.image, self.rect)
        if len(self.interior) == 2 and self.interior[0].gender != self.interior[1].gender:
            self.producting -= 1
            if self.producting == 0:
                temp = randint(1, 2)
                newGender = "Male" if temp == 1 else "Female"
                newName = girl_name[randint(0,len(girl_name)-1)] if newGender == "Female" else boy_name[randint(0,len(boy_name)-1)]
                new = Villager(newGender, newName, self.rect.x - 105, self.rect.top)
                human.append(new)
                human.extend(self.interior)
                self.interior.clear()
                self.producting = -1

    def forceGetOut(self, human):
        human.extend(self.interior)
        self.interior.clear()

    def showInfo(self, screen, size):
        font = pg.font.SysFont("calibri", size, True, 0)
        surface = font.render("People in house: "+str(len(self.interior)), True, (0, 0, 0))
        screen.blit(surface, (45, 80))
        for j in range (len(self.interior)):
            surface = font.render(self.interior[j].name, True, (0, 0, 0))
            screen.blit(surface, (60, 80 + (j+1)*30))
        if self.producting != -1:
            surface = font.render("Producing "+str(int(self.producting/6))+"%", True, (0, 0, 0))
            screen.blit(surface, (45, 80 + 3*30))
            
