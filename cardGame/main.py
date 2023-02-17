from random import randint
import pygame as pg
from pygame.locals import *
import time
from Human import *
from Zone import *
from Infrastructure import *
import Name
import math

pg.init()

clock = pg.time.Clock()
fps = 60

screen_width, screen_height = pg.display.Info().current_w, pg.display.Info().current_h

screen = pg.display.set_mode((screen_width, screen_height))
screen.fill((253, 246, 227))
pg.display.set_caption("Lover")

clickSound = pg.mixer.Sound('D:\Coding\pythin\cardProject\sound\Click.mp3')
releaseSound = pg.mixer.Sound('D:\Coding\pythin\cardProject\sound\ReleaseClick.mp3')

def quitting():
    text = "Ending"
    screen.fill((253, 246, 227)) 
    printText( text , screen_width/2 - int(screen_width/15) ,screen_height/2 - int(screen_height/40), 50)
    pg.display.update()
    time.sleep(0.2)

    for i in range(5):
        screen.fill((253, 246, 227))
        text += "."  
        printText( text , screen_width/2 - int(screen_width/15) ,screen_height/2 - int(screen_height/40), 50)
        pg.display.update()
        time.sleep(0.2)

    pg.quit()

def printText(text, x ,y, size):
    font = pg.font.SysFont("calibri", size, True, 0)
    surface2 = font.render(text, True, (0, 0, 0))
    screen.blit(surface2, (x, y))


run = True

informationZone = InformationZone(screen_width, screen_height)
playZone = PlayZone(screen_width, screen_height)


yearDuration = 60 #seconds
year = 1
countdown = yearDuration*fps

# cards size: 100*150
human = []
nature = []
infrac = []

text_occupied = False



selected = None
human.append(Villager("Male", "Adam", 600, 400))
human.append(Villager("Female", "Eve", 400, 400))
infrac.append(House(600, 600))


while run:
    clock.tick(fps)
    screen.fill((253, 246, 227))   
    informationZone.draw(screen)
    playZone.draw(screen)
    mousex, mousey = pg.mouse.get_pos()

    countdown -= 1
    printText("YEAR "+str(year) + " ("+str(int(countdown/36)) + "% )" , 45 , 40, 20)
    if countdown == 0:
        countdown = yearDuration*fps
        year += 1


    for i in (human):
        i.update(screen)

    for i in (infrac):
        i.update(screen, human)
        
        #Show infracsrtructure infos
        if i.rect.collidepoint((mousex, mousey)):
            i.showInfo(screen, 20)

    for r in (human):
        #Check if human go into infracstructure
        for i in infrac:
            if i.rect.collidepoint((r.desx + 50, r.desy + 75)) and i.rect.colliderect(r):
                i.stay(r, human)
                
        #Show human infos
        if r.rect.collidepoint((mousex, mousey)):
            r.showInfo(screen, 20)   

    for event in pg.event.get():
        # Escape methods
        if event.type == pg.QUIT:
            run = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            #Take selected human
            for r in (human):
                if event.button == 1: 
                    if r.rect.collidepoint(event.pos):
                        clickSound.play()
                        selected = human.index(r)
                        if selected != None:
                            temp = human[selected]
                            human.pop(selected)
                            human.append(temp)

            #Interact with infracstructure
            for r in infrac:
                if event.button == 3:
                    if r.rect.collidepoint(event.pos):
                        if len(r.interior) != 0:
                            r.forceGetOut(human)
                            r.producting = -1

        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
               
                #Move human Cards, set the limit area
                if selected != None:
                    releaseSound.play()
                    human[selected].isMove = True
                    if mousex + 50 > playZone.zonePos()[3]:
                        mousex = playZone.zonePos()[3] - 53
                    elif mousex - 50 < playZone.zonePos()[2]:
                        mousex = playZone.zonePos()[2] +53
                    if mousey + 75 > playZone.zonePos()[0]:
                        mousey = playZone.zonePos()[0] -78
                    elif mousey - 75 < playZone.zonePos()[1]:
                        mousey = playZone.zonePos()[1] + 78
                    
                    #Calculate the velocity in x, y bases on the absolute velocity
                    human[selected].desx = mousex - 50
                    human[selected].desy = mousey - 75
                    dx = abs(human[selected].desx - human[selected].rect.x)
                    dy = abs(human[selected].desy - human[selected].rect.y)
                    t = math.sqrt(pow(dx, 2) + pow(dy, 2))/human[selected].velocity
                    if t != 0:
                        human[selected].velx = dx/t
                        human[selected].vely = dy/t
                
                selected = None

        
    pg.display.update()

quitting()