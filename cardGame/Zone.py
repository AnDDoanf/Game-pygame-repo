import pygame as pg

class InformationZone():
    def __init__(self, width, height):
        self.rect = pg.Rect((20, 20), (int(width/6), height - 40))

    def draw(self, screen):
        pg.draw.rect(screen, color="#000000", rect=self.rect, width=5, border_radius=3)
    
    def zonePos(self):
        return [self.rect.topright, self.rect.bottomright]
        
class houseZone():
    def __init__(self) -> None:
        pass

class PlayZone():
    def __init__(self, width, height):
        self.rect = pg.Rect((int(width/6)+40, 20), (int(width*5/6) - 80, height - 40))

    def draw(self, screen):
        pg.draw.rect(screen, color="#000000", rect=self.rect, width=5, border_radius=3)
    
    def zonePos(self):
        return [self.rect.bottom, self.rect.top, self.rect.left, self.rect.right]
