import pygame
from pygame.constants import *
from pygame.event import event_name
import pymunk
import math
from pymunk import contact_point_set
from pymunk.shapes import Segment
import random

pygame.init()

display = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()
space = pymunk.Space()
Xcenter = 500
Ycenter = 400
A = 300
B = 250
accelarate = 50
FPS = 80

class Ball():
    def __init__(self, p1, p2, collision_number = None):
        self.body = pymunk.Body()
        self.body.position = p1, p2
        self.shape = pymunk.Circle(self.body, 8)
        self.shape.density = 10
        self.body.velocity = 200*random.random(),200*random.random()
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
    
    def moverightleft(self, right = True):
        self.body.veloX, self.body.veloY = self.body._get_velocity()
        if right:
            self.body.velocity = 300, 0
        else:
            self.body.velocity = -300, 0

    def moveupdown(self, up = True):
        self.body.veloX, self.body.veloY = self.body._get_velocity()
        if up:
            self.body.velocity = 0, -300
        else:
            self.body.velocity = 0, 300
    
    def standardize_velo(self):
        self.body.velocity = self.body.velocity*(self.velocity/self.body.velocity.length)

    def draw(self, color):
        x, y = self.body.position
        pygame.draw.circle(display, color,(int(x), int(y)), 8)


class Wall():
    def __init__(self, p1, p2, collision_number = None):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body,p1, p2, 8)
        self.shape.elasticity = 1
        space.add(self.body, self.shape)

    def draw(self):
        pygame.draw.line(display, (255,255,255), self.shape.a , self.shape.b, 20)

def game():
    ball1 = Ball(500, 200, 1)
    ball2 = Ball(600, 200 ,1)
    ball3 = Ball(610, 200 ,1)
    ball4 = Ball(620, 200 ,1)
    ball5 = Ball(630, 200 ,1)
    ball6 = Ball(640, 200 ,1)
    ball7 = Ball(650, 200 ,1)
    ball8 = Ball(660, 200 ,1)
    ball9 = Ball(670, 200 ,1)

    i = 30
    colis = space.add_collision_handler(1,2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        keys = pygame.key.get_pressed()

        if keys[K_ESCAPE]:
            return False
        if keys[K_d]:
            ball1.moverightleft()
        elif keys[K_a]:
            ball1.moverightleft(False)
        if keys[K_w]:
            ball1.moveupdown()
        elif keys[K_s]:
            ball1.moveupdown(False)

        display.fill("black")
        

        ball1.draw((255,0,0))
        ball2.draw((0,255,0))
        ball3.draw((0,255,0))
        ball4.draw((0,255,0))
        ball5.draw((0,255,0))
        ball6.draw((0,255,0))
        ball7.draw((0,255,0))
        ball8.draw((0,255,0))
        ball9.draw((0,255,0))
        rotate = i*math.pi/180
        Xtopright = Xcenter + A*math.cos(rotate) - B*math.sin(rotate)
        Ytopright = Ycenter - A*math.sin(rotate) - B*math.cos(rotate)
        Xbotright = Xcenter + A*math.cos(rotate) + B*math.sin(rotate)
        Ybotright = Ycenter - A*math.sin(rotate) + B*math.cos(rotate)
        Xtopleft = 2*Xcenter - Xbotright
        Ytopleft = 2*Ycenter - Ybotright
        Xbotleft = 2*Xcenter - Xtopright
        Ybotleft = 2*Ycenter - Ytopright
        wall_bot = Wall([Xbotleft, Ybotleft], [Xbotright,Ybotright],3)
        wall_top = Wall([Xtopleft, Ytopleft], [Xtopright, Ytopright],3)
        wall_left = Wall([Xtopleft, Ytopleft], [Xbotleft, Ybotleft],3)
        wall_right = Wall([Xtopright, Ytopright], [Xbotright, Ybotright],3)
        wall_top.draw()
        wall_left.draw()
        wall_right.draw()
        wall_bot.draw()
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)
    

game()
pygame.quit()