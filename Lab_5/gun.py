import pygame as pg
import numpy as np
from random import randint

pg.init()

SCREEN_SIZE = (800, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Manager():
    def __init__(self):
        self.gun = Gun()
        self.score_t = Table()
        
    def draw(self, screen):
        screen.fill(BLACK)
        self.gun.draw(screen)
    
    def process(self, events, screen):
        done = self.handle_events(events)
        self.move()
        self.draw(screen)
        return done
    
    def draw(self, screen):
        screen.fill(BLACK)
        self.gun.draw(screen)
    
    def move(self):
        pass
    
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            if pg.mouse.get_focused():
                mouse_pos = pg.mouse.get_pos()
                self.gun.set_angle(mouse_pos)
        
        self.draw(screen)
        return done
class Gun():
    def __init__(self, coord = [30, SCREEN_SIZE[1]//2]):
        self.coord = coord
        self.angle = 0
        self.color = WHITE
        
    def draw(self, screen):
        gun_shape = [[self.coord[0]+int(20*np.cos(self.angle)-8*np.sin(self.angle)), 
                     self.coord[1]+int(20*np.sin(self.angle)+8*np.cos(self.angle))],
                     [self.coord[0]+int(20*np.cos(self.angle)+8*np.sin(self.angle)), 
                     self.coord[1]+int(20*np.sin(self.angle)-8*np.cos(self.angle))],
                     [self.coord[0]+int(-10*np.cos(self.angle)+8*np.sin(self.angle)), 
                     self.coord[1]+int(-10*np.sin(self.angle)-8*np.cos(self.angle))],
                     [self.coord[0]+int(-10*np.cos(self.angle)-8*np.sin(self.angle)), 
                     self.coord[1]+int(-10*np.sin(self.angle)+8*np.cos(self.angle))]]
        pg.draw.polygon(screen, self.color, gun_shape)
        
        
    def strike(self):
        pass
    
    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1],
                                mouse_pos[0] - self.coord[0])
    
    
class Table():
    pass
class Ball():
    pass
        
mgr = Manager()
screen = pg.display.set_mode(SCREEN_SIZE)
done = False
clock = pg.time.Clock()
while not done:
    clock.tick(15)
    done = mgr.process(pg.event.get(), screen)
    pg.display.flip()
pg.quit()
