# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:22:26 2020

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

RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)


def ball_1_define():
    '''определяет синий шарик '''
    global x1, y1, a1, b1, color1
    x1 = randint(100, 1100)
    y1 = randint(100, 500)
    a1 = random() * (randint(0, 1) - 0.5) # скорость по x
    b1 = np.sqrt(1 - a1**2) * (randint(0, 1) - 0.5) # скорость по y
    a1 = int(5*a1)
    b1 = int(5*b1)
    color1 = BLUE
def ball_2_define():
    '''определяет красный шарик '''
    global x2, y2, a2, b2, color2
    x2 = randint(100, 1100)
    y2 = randint(100, 500)
    a2 = random() * (randint(0, 1) - 0.5) # скорость по x
    b2 = np.sqrt(1 - a2**2) * (randint(0, 1) - 0.5) # скорость по y
    a2 = int(5*a2)
    b2 = int(5*b2)
    color2 = RED
def ball_3_define():
    '''определяет розовый шарик '''
    global x3, y3, a3, b3, color3
    x3 = randint(100, 1100)
    y3 = randint(100, 500)
    a3 = random() * (randint(0, 1) - 0.5) # скорость по x
    b3 = np.sqrt(1 - a3**2) * (randint(0, 1) - 0.5) # скорость по y
    a3 = int(5*a3)
    b3 = int(5*b3)
    color3 = MAGENTA
def new_ball(x, y, color):
    '''рисует новый шарик '''
    global r
    r = 30
    circle(screen, color, (x, y), r)
def draw_score(score):
    text = str(score)
    surface = font.render(text, False, (0, 0, 0))
    screen.blit(surface, (100, 60))   
        

clock = pygame.time.Clock()
finished = False
screen.fill(WHITE)
score = 0
draw_score(score)
ball_1_define()
ball_2_define()
ball_3_define()
l1, l2, l3 = 1, 1, 1 # задает шаг передвижения шарика
new_ball(x1, y1, color1)
new_ball(x2, y2, color2)
new_ball(x3, y3, color3)
pygame.display.update()


while not finished:
    clock.tick(FPS)
    if l1 == 100:
        ball_1_define()
        l1 = 1
    if l2 == 100:
        ball_2_define()
        l2 = 1
    if l3 == 100:
        ball_3_define()
        l3 = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - x1)**2 + (event.pos[1] - y1)**2 <= r**2:
                score += 1
                x1 = -1000
                ball_1_define()
                l1 = 1
                screen.fill(WHITE)
                draw_score(score)
                new_ball(x1, y1, color1)
            if (event.pos[0] - x2)**2 + (event.pos[1] - y2)**2 <= r**2:
                score += 1
                x2 = -1000
                ball_2_define()
                l2 = 1
                screen.fill(WHITE)
                draw_score(score)
                new_ball(x2, y2, color2)
            if (event.pos[0] - x3)**2 + (event.pos[1] - y3)**2 <= r**2:
                score += 1
                x3 = -1000
                ball_3_define()
                l3 = 1
                screen.fill(WHITE)
                draw_score(score)
                new_ball(x3, y3, color3)
    x1 = x1 + a1
    y1 = y1 + b1
    x2 = x2 + a2
    y2 = y2 + b2
    x3 = x3 + a3
    y3 = y3 + b3
    if (x1 >= 1170) & (a1 > 0):
        a1 *= -1
    if (x1 <= 30) & (a1 < 0):
        a1 *= -1
    if (y1 >= 570) & (b1 > 0):
        b1 *= -1
    if (y1 <= 30) & (b1 < 0):
        b1 *= -1
    if (x2 >= 1170) & (a2 > 0):
        a2 *= -1
    if (x2 <= 30) & (a2 < 0):
        a2 *= -1
    if (y2 >= 570) & (b2 > 0):
        b2 *= -1
    if (y2 <= 30) & (b2 < 0):
        b2 *= -1
    if (x3 >= 1170) & (a3 > 0):
        a3 *= -1
    if (x3 <= 30) & (a3 < 0):
        a3 *= -1
    if (y3 >= 570) & (b3 > 0):
        b3 *= -1
    if (y3 <= 30) & (b3 < 0):
        b3 *= -1
    screen.fill(WHITE)
    draw_score(score)
    new_ball(x1, y1, color1)
    new_ball(x2, y2, color2)
    new_ball(x3, y3, color3)
    pygame.display.update()
    l1 += 1
    l2 += 1
    l3 += 1

pygame.quit()