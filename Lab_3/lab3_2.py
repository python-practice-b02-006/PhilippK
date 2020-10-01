# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 19:17:54 2020

@author: Филипп
"""

import pygame
import numpy as np
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode([600, 402])

pygame.display.set_caption("Sea")

done = False
clock = pygame.time.Clock()
pi = 3.141


rect(screen, (140, 254, 243), (0, 0, 600, 183))
rect(screen, (59, 56, 255), (0, 183, 600, 100))
rect(screen, (233, 255, 0), (0, 283, 600, 119))
circle(screen, (233, 255, 0), [530, 80], 60)

line(screen, (255, 149, 0), [100, 370], [100, 250], 4)
polygon(screen, (255, 70, 100), [[40, 270], [160, 270], [102, 250], [98, 250]])
line(screen, (60, 60, 60), [98, 250], [55, 270])
line(screen, (60, 60, 60), [98, 250], [70, 270])
line(screen, (60, 60, 60), [98, 250], [85, 270])
line(screen, (150, 150, 150), [98, 250], [98, 270])
line(screen, (150, 150, 150), [102, 250], [102, 270])
line(screen, (60, 60, 60), [102, 250], [115, 270])
line(screen, (60, 60, 60), [102, 250], [130, 270])
line(screen, (60, 60, 60), [102, 250], [145, 270])

x = 320
y = 220
lsh = [[x, y]]
r = 20
c = np.pi/20
while c <= np.pi/2:
    lsh.append([x + r - r * np.cos(c), y + r * np.sin(c)])
    c += pi/20
lsh.append([x + 7*r, y + r])
lsh.append([x + 9*r, y])
polygon(screen, (170, 50, 0), lsh)
line(screen, (30, 30, 30), [x + 3*r, y], [x + 3*r, y - 4*r], 2)
polygon(screen, (180, 180, 180), [[x + 3*r, y - 4*r], [x + 3.75*r, y - 2*r],
                                  [x + 3*r, y], [x + 5.25*r, y - 2*r]])
polygon(screen, (30, 30, 30), [[x + 3*r, y - 4*r], [x + 3.75*r, y - 2*r],
                               [x + 3*r, y], [x + 5.25*r, y - 2*r]], 1)
line(screen, (30, 30, 30), [x + 3.75*r, y - 2*r], [x + 5.25*r, y - 2*r], 1)
circle(screen, (20, 20, 20), [x + 7*r + 10, y + 8], 6)
circle(screen, (255, 255, 255), [x + 7*r + 10, y + 8], 4)
line(screen, (30, 30, 30), [x + r, y], [x + r, y + r])
line(screen, (30, 30, 30), [x + 7*r, y], [x + 7*r, y + r])

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
