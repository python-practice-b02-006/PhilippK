# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:29:43 2020

@author: Филипп
"""

import pygame
import numpy as np
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode([600, 402])

pygame.display.set_caption("Sea")

def ship(x, y, s, v):
    lsh = [[x, y]]
    r = 10 * s
    c = np.pi/20
    while c <= np.pi/2:
        lsh.append([x + r - r * np.cos(c), y + r * np.sin(c)])
        c += pi/20
    lsh.append([x + 7*r, y + r])
    lsh.append([x + 9*r, y])
    polygon(screen, (170, 50, 0), lsh)
    line(screen, (30, 30, 30), [x + 3*r, y], [x + 3*r, y - 4*r], v)
    polygon(screen, (180, 180, 180), [[x + 3*r, y - 4*r], [x + 3.75*r, y - 2*r],
                                      [x + 3*r, y], [x + 5.25*r, y - 2*r]])
    polygon(screen, (30, 30, 30), [[x + 3*r, y - 4*r], [x + 3.75*r, y - 2*r],
                                   [x + 3*r, y], [x + 5.25*r, y - 2*r]], 1)
    line(screen, (30, 30, 30), [x + 3.75*r, y - 2*r], [x + 5.25*r, y - 2*r], 1)
    circle(screen, (20, 20, 20), [x + 7*r + 5*s, y + 4*s], 3*s)
    circle(screen, (255, 255, 255), [x + 7*r + 5*s, y + 4*s], 2*s)
    line(screen, (30, 30, 30), [x + r, y], [x + r, y + r])
    line(screen, (30, 30, 30), [x + 7*r, y], [x + 7*r, y + r])
    

def clouds():
    ellipse(screen, (255, 255, 255), [100, 40, 20, 20])
    ellipse(screen, (180, 180, 180), [100, 40, 20, 20], 1)
    ellipse(screen, (255, 255, 255), [110, 40, 20, 20])
    ellipse(screen, (180, 180, 180), [110, 40, 20, 20], 1)
    ellipse(screen, (255, 255, 255), [90, 50, 20, 20])
    ellipse(screen, (180, 180, 180), [90, 50, 20, 20], 1)
    ellipse(screen, (255, 255, 255), [105, 50, 20, 20])
    ellipse(screen, (180, 180, 180), [105, 50, 20, 20], 1)
    ellipse(screen, (255, 255, 255), [115, 50, 20, 20])
    ellipse(screen, (180, 180, 180), [115, 50, 20, 20], 1)
    ellipse(screen, (255, 255, 255), [120, 40, 20, 20])
    ellipse(screen, (180, 180, 180), [120, 40, 20, 20], 1)
    ellipse(screen, (255, 255, 255), [125, 50, 20, 20])
    ellipse(screen, (180, 180, 180), [125, 50, 20, 20], 1)
    
    ellipse(screen, (255, 255, 255), [50, 100, 30, 20])
    ellipse(screen, (180, 180, 180), [50, 100, 30, 20], 1)
    ellipse(screen, (255, 255, 255), [65, 100, 30, 20])
    ellipse(screen, (180, 180, 180), [65, 100, 30, 20], 1)
    ellipse(screen, (255, 255, 255), [35, 110, 30, 20])
    ellipse(screen, (180, 180, 180), [35, 110, 30, 20], 1)
    ellipse(screen, (255, 255, 255), [57, 110, 30, 20])
    ellipse(screen, (180, 180, 180), [57, 110, 30, 20], 1)
    ellipse(screen, (255, 255, 255), [70, 110, 30, 20])
    ellipse(screen, (180, 180, 180), [70, 110, 30, 20], 1)
    ellipse(screen, (255, 255, 255), [80, 100, 30, 20])
    ellipse(screen, (180, 180, 180), [80, 100, 30, 20], 1)
    ellipse(screen, (255, 255, 255), [90, 110, 30, 20])
    ellipse(screen, (180, 180, 180), [90, 110, 30, 20], 1)
    
    ellipse(screen, (255, 255, 255), [300, 40, 50, 60])
    ellipse(screen, (180, 180, 180), [300, 40, 50, 60], 1)
    ellipse(screen, (255, 255, 255), [325, 40, 50, 60])
    ellipse(screen, (180, 180, 180), [325, 40, 50, 60], 1)
    ellipse(screen, (255, 255, 255), [275, 70, 50, 60])
    ellipse(screen, (180, 180, 180), [275, 70, 50, 60], 1)
    ellipse(screen, (255, 255, 255), [312, 70, 50, 60])
    ellipse(screen, (180, 180, 180), [312, 70, 50, 60], 1)
    ellipse(screen, (255, 255, 255), [337, 70, 50, 60])
    ellipse(screen, (180, 180, 180), [337, 70, 50, 60], 1)
    ellipse(screen, (255, 255, 255), [350, 40, 50, 60])
    ellipse(screen, (180, 180, 180), [350, 40, 50, 60], 1)
    ellipse(screen, (255, 255, 255), [362, 70, 50, 60])
    ellipse(screen, (180, 180, 180), [362, 70, 50, 60], 1)
        
    
def sun():
    ls = [[580, 80]]
    a = np.pi/20 - np.pi/40 
    b = np.pi/20
    while a <= 2*np.pi:
        ls.append([530 + 60 * np.cos(a), 80 + 60 * np.sin(a)])
        ls.append([530 + 40 * np.cos(b), 80 + 40 * np.sin(b)])
        a += pi/20
        b += pi/20
    polygon(screen, (233, 255, 0), ls)
    
    
def coast():
    i = 0
    while i <= 600:
        circle(screen, (233, 255, 0), (i, 309), 30)
        circle(screen, (59, 56, 255), (i + 30, 257), 30)
        i += 60
    line(screen, (100, 100, 100), [0, 283], [600, 283], 1)
        

def umbrellas():
    line(screen, (255, 149, 0), [100, 370], [100, 250], 4)
    polygon(screen, (255, 70, 100), [[40, 270], [160, 270], [102, 250], [98, 250]])
    line(screen, (255, 149, 0), [200, 370], [200, 280], 2)
    polygon(screen, (255, 70, 100), [[170, 290], [230, 290], [201, 280], [199, 280]])
    
    line(screen, (60, 60, 60), [98, 250], [55, 270])
    line(screen, (60, 60, 60), [98, 250], [70, 270])
    line(screen, (60, 60, 60), [98, 250], [85, 270])
    line(screen, (150, 150, 150), [98, 250], [98, 270])
    line(screen, (150, 150, 150), [102, 250], [102, 270])
    line(screen, (60, 60, 60), [102, 250], [115, 270])
    line(screen, (60, 60, 60), [102, 250], [130, 270])
    line(screen, (60, 60, 60), [102, 250], [145, 270])
    
    line(screen, (60, 60, 60), [199, 280], [177, 290])
    line(screen, (60, 60, 60), [199, 280], [184, 290])
    line(screen, (60, 60, 60), [199, 280], [191, 290])
    line(screen, (150, 150, 150), [199, 280], [199, 290])
    line(screen, (150, 150, 150), [199, 280], [201, 290])
    line(screen, (60, 60, 60), [199, 280], [209, 290])
    line(screen, (60, 60, 60), [199, 280], [216, 290])
    line(screen, (60, 60, 60), [199, 280], [223, 290])
    

done = False
clock = pygame.time.Clock()
pi = 3.141


rect(screen, (140, 254, 243), (0, 0, 600, 183))
rect(screen, (59, 56, 255), (0, 183, 600, 100))
rect(screen, (233, 255, 0), (0, 283, 600, 119))
sun()
clouds()
coast()
umbrellas()
ship(140, 188, 1, 1)
ship(320, 220, 2, 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
pygame.display.update()

while not finished:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
