import pygame as pg
import time

pg.init()

clock = pg.time.Clock()
fps = 60

screen_width, screen_height = pg.display.Info().current_w, pg.display.Info().current_h

screen = pg.display.set_mode((screen_width, screen_height))
screen.fill((253, 246, 227))
pg.display.set_caption("drumProject")

kick = pg.mixer.Sound('kick.mp3')
hihat_foot = pg.mixer.Sound('hihat_foot.mp3')
kick_hihat_foot = pg.mixer.Sound('kick_hihat_foot.mp3')


run = True
while run:
    screen.fill((253, 246, 227)) 
    clock.tick(fps)

    for event in pg.event.get():
        # Escape methods
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
            if event.key == pg.K_SPACE:
                kick.play()
            if event.key == pg.K_n:
                hihat_foot.play()
            if event.key == pg.K_c:
                kick_hihat_foot.play()
            if event.
    pg.display.update()

pg.quit()