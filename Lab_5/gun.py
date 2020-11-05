import pygame as pg
import numpy as np
from random import randint

pg.init()

SCREEN_SIZE = (800, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

class Manager():
    def __init__(self):
        self.gun = Gun()
        self.score_t = Table()
        self.balls = []
        self.targets = []
        self.n_targets = 3
        
    def new_mission(self):
        for i in range(self.n_targets):
            self.targets.append(Target())
        
    def draw(self, screen):
        screen.fill(BLACK)
        for ball in self.balls:
            ball.draw(screen)
        self.gun.draw(screen)
        for target in self.targets:
            target.draw(screen)
    
    def process(self, events, screen):
        done = self.handle_events(events)
        self.move()
        self.collide()
        self.draw(screen)
        if len(self.targets) == 0 and len(self.balls) == 0:
            self.new_mission()
        return done
    
    def move(self):
        dead_balls = []
        for i, ball in enumerate(self.balls):
            ball.move()
            if not ball.is_alive:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
        self.gun.move()
    
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
                    self.gun.move()
            if pg.mouse.get_focused():
                mouse_pos = pg.mouse.get_pos()
                self.gun.set_angle(mouse_pos)
        
        self.draw(screen)
        return done
    
    def collide(self):
        collisions = []
        targets_killed = []
        for i, ball in enumerate(self.balls):
            for j, target in enumerate(self.targets):
                if target.check_collision(ball):
                    collisions.append([i, j])
                    targets_killed.append(j)
        for j in targets_killed:
            self.targets.pop(j)
    
    
class Gun():
    def __init__(self, coord = [30, SCREEN_SIZE[1]//2],
                 min_pow = 5, max_pow = 50):
        self.coord = coord
        self.angle = 0
        self.color = WHITE
        self.min_pow = min_pow
        self.max_pow = max_pow
        self.power = self.min_pow
        self.active = False
        
    def draw(self, screen):
        end_pos = [self.coord[0] + self.power*np.cos(self.angle), 
                   self.coord[1] + self.power*np.sin(self.angle)]
        pg.draw.line(screen, self.color, self.coord, end_pos, 8)
        
    def active(self):
        self.active = True
    
    def elongation(self, inc=1):
        if self.active and self.power < self.max_pow:
            self.power += inc
        
    def strike(self):
        vel = [int(self.power * np.cos(self.angle)), int(self.power * np.sin(self.angle))]
        self.active = False
        self.power = self.min_pow
        return Ball(list(self.coord), vel)
    
    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1],
                                mouse_pos[0] - self.coord[0])
    def move(self):
        self.elongation()
    
    
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
        self.coord[0] += self.vel[0]*t_step
        self.vel[1] += 2
        self.coord[1] += self.vel[1]*t_step
        self.check_walls()
        if self.vel[0]**2 + self.vel[1]**2 <= 1:
            self.is_alive = False
    
    def check_walls(self):
        n = [[1, 0], [0, 1]]
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.flip_vel(n[i])
                self.vel[0] = int(0.9*self.vel[0])
                self.vel[1] = int(0.9*self.vel[1])
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.flip_vel(n[i])
                self.vel[0] = int(0.9*self.vel[0])
                self.vel[1] = int(0.9*self.vel[1])
    
    def flip_vel(self, axis, coef_perp=1., coef_par=1.):
        vel = np.array(self.vel)
        n = np.array(axis)
        n = n / np.linalg.norm(n)
        vel_perp = vel.dot(n) * n
        vel_par = vel - vel_perp
        ans = -vel_perp * coef_perp + vel_par * coef_par
        self.vel = ans.astype(np.int).tolist()
        
class Target():
    def __init__(self, rad=30):
        coord = [randint(rad, SCREEN_SIZE[0] - rad),
                 randint(rad, SCREEN_SIZE[1] - rad)]
        self.coord = coord
        self.rad = rad
        color = rand_color()
        self.color = color
        
    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)
        
    def check_collision(self, ball):
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist
    
        
mgr = Manager()
screen = pg.display.set_mode(SCREEN_SIZE)
done = False
clock = pg.time.Clock()
while not done:
    clock.tick(15)
    done = mgr.process(pg.event.get(), screen)
    pg.display.flip()
pg.quit()
