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
YELLOW = (155, 150, 90)


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
def star_define():
    '''определяет звезду '''
    global x4, y4, a4, color4
    x4 = randint(100, 1100)
    y4 = randint(100, 500)
    a4 = random() * (randint(0, 1) - 0.5) # скорость по x
    a4 = int(5*a4)
    color4 = YELLOW
def new_ball(x, y, color):
    '''рисует новый шарик '''
    global r
    r = 30
    circle(screen, color, (x, y), r)
def star(x, y, color):
    '''рисует звезду '''
    polygon(screen, color, [[x-15, y], [x-9, y-3], [x-12, y-12], [x-3, y-9], [x, y-15],
                            [x+3, y-9], [x+12, y-12], [x+9, y-3], [x+15, y],
                            [x+9, y+3], [x+12, y+12], [x+3, y+9], [x, y+15],
                            [x-3, y+9], [x-12, y+12], [x-9, y+3]])
def draw_score(score):
    text = str(score)
    surface = font.render(text, False, (0, 0, 0))
    screen.blit(surface, (100, 60))   
        

name = input('Введите имя: ')
res = open('C:/Users/Филипп/Documents/github/PhilippK/Lab_4/Results.txt', 'a')

clock = pygame.time.Clock()
finished = False
screen.fill(WHITE)
surname = font.render(name, False, (0, 0, 0))
screen.blit(surname, (30, 30))
score = 0
draw_score(score)
ball_1_define()
ball_2_define()
ball_3_define()
star_define()
l1, l2, l3, l4 = 1, 1, 1, 1 # задает шаг передвижения шариков и звезды
new_ball(x1, y1, color1)
new_ball(x2, y2, color2)
new_ball(x3, y3, color3)
star(x4, y4, color4)
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
    if l4 == 100:
        star_define()
        l4 = 1
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
                screen.blit(surname, (30, 30))
            if (event.pos[0] - x2)**2 + (event.pos[1] - y2)**2 <= r**2:
                score += 1
                x2 = -1000
                ball_2_define()
                l2 = 1
                screen.fill(WHITE)
                draw_score(score)
                new_ball(x2, y2, color2)
                screen.blit(surname, (30, 30))
            if (event.pos[0] - x3)**2 + (event.pos[1] - y3)**2 <= r**2:
                score += 1
                x3 = -1000
                ball_3_define()
                l3 = 1
                screen.fill(WHITE)
                draw_score(score)
                new_ball(x3, y3, color3)
                screen.blit(surname, (30, 30))
            if (event.pos[0] - x4)**2 + (event.pos[1] - y4)**2 <= 81:
                score += 3
                x4 = -1000
                star_define()
                l4 = 1
                screen.fill(WHITE)
                draw_score(score)
                star(x4, y4, color4)
                screen.blit(surname, (30, 30))
    x1 = x1 + a1
    y1 = y1 + b1
    x2 = x2 + a2
    y2 = y2 + b2
    x3 = x3 + a3
    y3 = y3 + b3
    x4 = x4 + a4
    y4 = int(y4 + 0.1*l4)
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
    star(x4, y4, color4)
    new_ball(x1, y1, color1)
    new_ball(x2, y2, color2)
    new_ball(x3, y3, color3)
    star(x4, y4, color4)
    screen.blit(surname, (30, 30))
    pygame.display.update()
    l1 += 1
    l2 += 1
    l3 += 1
    l4 += 1
    
score = str(score)
res.write(name + ' ' + score + '\n')
res.close()

pygame.quit()
