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
        self.balls = []
        
    def draw(self, screen):
        screen.fill(BLACK)
        for ball in self.balls:
            ball.draw(screen)
        self.gun.draw(screen)
    
    def process(self, events, screen):
        done = self.handle_events(events)
        self.move()
        self.draw(screen)
        return done
    
    def move(self):
        for ball in self.balls:
            ball.move()
    
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.active = True
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.strike())
            if pg.mouse.get_focused():
                mouse_pos = pg.mouse.get_pos()
                self.gun.set_angle(mouse_pos)
        
        self.draw(screen)
        return done
class Gun():
    def __init__(self, coord = [30, SCREEN_SIZE[1]//2],
                 min_pow = 10, max_pow = 20):
        self.coord = coord
        self.angle = 0
        self.color = WHITE
        self.min_pow = min_pow
        self.max_pow = max_pow
        self.power = min_pow
        self.active = False
        
    def draw(self, screen):
        end_pos = [self.coord[0] + self.power*np.cos(self.angle), 
                   self.coord[1] + self.power*np.sin(self.angle)]
        pg.draw.line(screen, self.color, self.coord, end_pos, 8)
        
        
    def strike(self):
        vel = [int(self.power * np.cos(self.angle)), int(self.power * np.sin(self.angle))]
        self.active = False
        self.power = self.min_pow
        return Ball(list(self.coord), vel)
    
    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1],
                                mouse_pos[0] - self.coord[0])
    
    
class Table():
    pass
class Ball():
    def __init__(self, coord, vel, color=None, rad=15):
        if color == None:
            color = (randint(100, 255), randint(0, 255), randint(0, 255))
        self.coord = coord
        self.vel = vel
        self.color = color
        self.rad = rad
        self.is_alive = True

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)
        
    def move(self, t_step = 1):
        for i in range(2):
            self.coord[i] += self.vel[i]*t_step
        self.check_walls()
    
    def check_walls(self):
        n = [[1, 0], [0, 1]]
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.flip_vel(n[i])
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.flip_vel(n[i])
    
    def flip_vel(self, axis, coef_perp=1., coef_par=1.):
        vel = np.array(self.vel)
        n = np.array(axis)
        n = n / np.linalg.norm(n)
        vel_perp = vel.dot(n) * n
        vel_par = vel - vel_perp
        ans = -vel_perp * coef_perp + vel_par * coef_par
        self.vel = ans.astype(np.int).tolist()
        
mgr = Manager()
screen = pg.display.set_mode(SCREEN_SIZE)
done = False
clock = pg.time.Clock()
while not done:
    clock.tick(15)
    done = mgr.process(pg.event.get(), screen)
    pg.display.flip()
pg.quit()
