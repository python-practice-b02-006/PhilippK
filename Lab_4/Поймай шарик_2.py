# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:30:19 2020

@author: Филипп
"""

import pygame
import numpy as np
from pygame.draw import *
from random import randint, random
pygame.init()
pygame.font.init()

FPS = 40
screen = pygame.display.set_mode((1200, 600))
font = pygame.font.SysFont("Times New Roman", 30)


BLUE = (0, 0, 255)
WHITE = (250, 250, 250)

def new_ball(x, y):
    '''рисует новый шарик '''
    global r
    r = 30
    color = BLUE
    circle(screen, color, (x, y), r)
def draw_score(score):
    '''рисует количество очков '''
    text = str(score)
    surface = font.render(text, False, (0, 0, 0))
    screen.blit(surface, (100, 60))
        

clock = pygame.time.Clock()
finished = False
screen.fill(WHITE)
score = 0
draw_score(score)
global x, y
x = randint(100, 1100)
y = randint(100, 500)
a = random() * (randint(0, 1) - 0.5) # скорость по x
b = np.sqrt(1 - a**2) * (randint(0, 1) - 0.5) # скорость по y
a = int(5*a)
b = int(5*b)
l = 1 # задает шаг передвижения шарика
new_ball(x, y)
pygame.display.update()


while not finished:
    clock.tick(FPS)
    if l == 100:
        x = randint(100, 1100)
        y = randint(100, 500)
        a = random() * (randint(0, 1) - 0.5)
        b = np.sqrt(1 - a**2) * (randint(0, 1) - 0.5)
        a = int(5*a)
        b = int(5*b)
        l = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - x)**2 + (event.pos[1] - y)**2 <= r**2:
                score += 1
                x = -1000
                x = randint(100, 1100)
                y = randint(100, 500)
                a = random() * (randint(0, 1) - 0.5)
                b = np.sqrt(1 - a**2) * (randint(0, 1) - 0.5)
                a = int(5*a)
                b = int(5*b)
                l = 1
                screen.fill(WHITE)
                draw_score(score)
                new_ball(x, y)
    x = x + a
    y = y + b
    if (x >= 1170) & (a > 0):
        a *= -1
    if (x <= 30) & (a < 0):
        a *= -1
    if (y >= 570) & (b > 0):
        b *= -1
    if (y <= 30) & (b < 0):
        b *= -1
    screen.fill(WHITE)
    draw_score(score)
    new_ball(x, y)
    pygame.display.update()
    l += 1

pygame.quit()