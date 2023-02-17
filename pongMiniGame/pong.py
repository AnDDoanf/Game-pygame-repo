import pygame
import time
from pygame.constants import K_DOWN, K_ESCAPE, K_UP, K_r
import pymunk
import random


pygame.init()

display = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
space = pymunk.Space()
FPS = 50

veloX = 450
veloY = -300
left = 50
right = 950
top = 25
bottom = 575
middleX = 500
middleY = 300

def printText(text, x):
    font = pygame.font.SysFont("calibri", 20, True, 0)
    surface = font.render(text, True, (255, 255, 255))
    display.blit(surface, (x, 5))

class Ball():
    def __init__(self):
        self.body = pymunk.Body()
        self.reset(0,0,0)
        self.shape = pymunk.Circle(self.body, 8)
        self.shape.density = 1
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
        self.shape.collision_type = 1
        self.velocity = 600

    def draw(self):
        x, y = self.body.position
        pygame.draw.circle(display, (255,255,255),(int(x), int(y)), 8)

    def reset(self, space = 0, arbiter = 0, data = 0):
        self.body.position = middleX, middleY
        self.body.velocity = veloX*random.choice([-1,1]), veloY*random.random() 
        self.velocity = 600
        return False

    def standardize_velo(self, space = 0, arbiter = 0, data = 0):
        self.body.velocity = self.body.velocity*(self.velocity/self.body.velocity.length)
        self.velocity += 50


class Wall():
    def __init__(self,p1,p2, collision_number = None):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, p1, p2, 8)
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
        if collision_number:
            self.shape.collision_type = collision_number
    
    def draw(self):
        pygame.draw.line(display, (255,255,255), self.shape.a , self.shape.b, 10)
         
class Player():
    def __init__(self, x):
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body.position = x, middleY
        self.shape = pymunk.Segment(self.body, [0,-50], [0, 50], 10)
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
        self.shape.collision_type = 100
        self.score = 0

    def draw(self):
        p1 = self.body.local_to_world(self.shape.a)
        p2 = self.body.local_to_world(self.shape.b)
        pygame.draw.line(display, (255,255,255), p1 , p2, 12)
         
    def on_edge(self):
        if self.body.local_to_world(self.shape.a)[1] <= top:
            self.body.velocity = 0, 0
            self.body.position = self.body.position[0], top + 50
        if self.body.local_to_world(self.shape.a)[1] >= bottom -100:
            self.body.velocity = 0, 0
            self.body.position = self.body.position[0], bottom - 50

    def move(self, up = True):
        if up:
            self.body.velocity = 0, -650
        else:
            self.body.velocity = 0, 650

    def stop(self):
        self.body.velocity = 0,0

def game():
    ball = Ball()
    wall_left = Wall([left, top], [left, bottom], 102)
    wall_right = Wall([right, top], [right, bottom], 101)
    wall_top = Wall([left, top], [right, top])
    wall_bottom = Wall([left, bottom], [right, bottom])
    player1 = Player(left + 30)
    player2 = Player(right - 30)

    score1 = space.add_collision_handler(1, 101)
    score2 = space.add_collision_handler(1, 102) 
    def player1_score(space, arbiter, data):
        player1.score += 1
        ball.reset()
        return False
    score1.begin = player1_score 
    def player2_score(space, arbiter, data):
        player2.score += 1
        ball.reset()
        return False
    score2.begin = player2_score 

    score = space.add_collision_handler(1,2)
    score.begin = ball.reset
    contact_with_player = space.add_collision_handler(1,100)
    contact_with_player.post_solve = ball.standardize_velo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        keys = pygame.key.get_pressed()

        if keys[K_ESCAPE]:
            return False
        elif keys[K_r]:
            ball.reset()
        if not player2.on_edge():
            if keys[K_UP]:
                player2.move()
            elif keys[K_DOWN]:
                player2.move(False)
            else:
                player2.stop()
        else:
            player2.stop()
        
        if not player1.on_edge():
            if keys[119]:
                player1.move()
            elif keys[115]:
                player1.move(False)
            else:
                player1.stop()
        else: 
            player1.stop()

        display.fill((0,0,0))
        ball.draw()
        wall_left.draw()
        wall_right.draw()
        wall_top.draw()
        wall_bottom.draw()
        player1.draw()
        player2.draw()
        pygame.draw.line(display, (255,255,255), [middleX,top], [middleX,bottom], 4)
        printText(f"Score: {player1.score}", left)
        printText(f"Score: {player2.score}", right -100)

        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()