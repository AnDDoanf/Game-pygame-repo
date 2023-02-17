import pygame as pg



# wood production

class Tree:
    def __init__(self, posx, posy) -> None:
        img = pg.image.load(f'D:\Coding\pythin\cardProject\image\Villager1.png')
        self.image1 = pg.transform.scale(img, (100, 150))
        img = pg.image.load(f'D:\Coding\pythin\cardProject\image\Villager2.png')
        self.image2 = pg.transform.scale(img, (100, 150))
        self.rect = self.image1.get_rect()
        self.rect.x = posx 
        self.rect.y = posy

class Wood:
    def __init__(self) -> None:
        pass

class Stick:
    def __init__(self) -> None:
        pass

class Plank:
    def __init__(self) -> None:
        pass

# stone production

class Quarry:
    def __init_subclass__(cls) -> None:
        pass

class Rock:
    def __init__(self) -> None:
        pass

class Stone:
    def __init__(self) -> None:
        pass

class Flint: 
    def __init__(self) -> None:
        pass


