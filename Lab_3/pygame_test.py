import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode([477, 674])

pygame.display.set_caption("Sea")


done = False
clock = pygame.time.Clock()
pi = 3.141


    
    

rect(screen, (0, 0, 114), (0, 0, 477, 70))
rect(screen, (116, 92, 255), (0, 70, 477, 40))
rect(screen, (233, 151, 255), (0, 110, 477, 65))
rect(screen, (255, 150, 182), (0, 175, 477, 90))
rect(screen, (255, 175, 96), (0, 265, 477, 85))
rect(screen, (0, 140, 255), (0, 350, 477, 324))

polygon(screen, (0, 0, 0), [[x, y], [, 50], [90, 90], [30, 30]])



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
