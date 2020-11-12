import pygame

Class Star:
    """Класс, описывающий звезду. Содержит её массу, координаты, скорость,
    радиус, цвет.
    """
    def __init__(self):
        self.m = 0
        self.x = 0
        self.y = 0
        self.vel = 0
        self.rad = 0
        self.color = (0, 0, 0)
        self.coords = [0, 0]
    
    def __draw__(self, screen):
        pygame.draw.circle(screen, self.color, self.coords, self.rad)



Class Planet:
    """Класс, описывающий планету. Содержит её массу, координаты, скорость,
    радиус, цвет.
    """
    def __init__(self):
        self.m = 0
        self.x = 0
        self.y = 0
        self.vel = 0
        self.rad = 0
        self.color = (0, 0, 0)
        self.coords = [0, 0]

    def __draw__(self, screen):
        pygame.draw.circle(screen, self.color, self.coords, self.rad)
