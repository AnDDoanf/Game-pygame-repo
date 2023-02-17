import pygame
from pygame import surface
from pygame import rect
from pygame import draw
from pygame.constants import K_ESCAPE, MOUSEBUTTONDOWN
from pygame.event import pump
from pynput.mouse import Button, Controller
import random

pygame.init()
display = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

mouse = Controller()

class Rec():
    def reset(self, parent_screen, x, y):
        display.fill((100,0,0)) 
        self.body = pygame.draw.rect(parent_screen, "white", [x,y,50,50])

def game():
    score = 0
    rectX, rectY = random.randint(10, 700), random.randint(10, 700)
    rec1 = Rec()
    rec1.reset(display, rectX, rectY)
    while True: 
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif (event.type == MOUSEBUTTONDOWN):
                if (rectX <= mx <= rectX + 50) and (rectY <= my <= rectY + 50):
                    score += 1
                    rectX, rectY = random.randint(10, 700), random.randint(10, 700)
                    rec1.reset(display, rectX, rectY)
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            print(score)
            return False
        
        pygame.display.flip()
        clock.tick(30)

    

game()
pygame.quit()