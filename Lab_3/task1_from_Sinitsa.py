import pygame
import numpy as np
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


def main():
    
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    
    a = 0
    
    while not finished:
        clock.tick(10)
        d = int(100*np.cos(a))
        r = int(10*np.cos(a))
        rect(screen, WHITE, [0, 0, 400, 400])  # Makes screen white.
        circle(screen, YELLOW, (200, 200 + d), 100)  # Draws main face in fixed coordinates.
        rect(screen, BLACK, [150, 250 + d, 100, 20 + r]) # Draws mouth in fixed coordinates.
        draw_eye(150, 160 + d, 20 + r)
        draw_eye(250, 160 + d, 20 - r)
        draw_left_eyebrow(50, 80 + d)
        draw_right_eyebrow(220, 55 + d)
        a += np.pi / 20
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

def draw_eye(x, y, r):
    """
    Draws eye in (x, y) coordinates and with radius r.

    Returns
    -------
    None.

    """
    circle(screen, RED, (x, y), 2*r)
    circle(screen, BLACK, (x, y), r)


def draw_left_eyebrow(x, y):
    """
    Draws left eyebrow in fixed coordinates.

    Parameters
    ----------
    x : TYPE int
        DESCRIPTION. x coordinate of top left corner of minimum rectangle(
        sides are parallel to coordinate axes) that consists the rectangle
        of eyebrow.
    y : TYPE int
        DESCRIPTION. y coordinate of top left corner of minimum rectangle(
        sides are parallel to coordinate axes) that consists the rectangle
        of eyebrow.

    Returns
    -------
    None.

    """
    surface = pygame.Surface([200, 100], pygame.SRCALPHA)
    rect(surface, BLACK, [0, 0, 100, 10])
    surface_rot = pygame.transform.rotate(surface, -30)
    screen.blit(surface_rot, [x, y])


def draw_right_eyebrow(x, y):
    """
    Draws right eyebrow in fixed coordinates.

    Parameters
    ----------
    x : TYPE int
        DESCRIPTION. x coordinate of top left corner of minimum rectangle(
        sides are parallel to coordinate axes) that consists the rectangle
        of eyebrow.
    y : TYPE int
        DESCRIPTION. y coordinate of top left corner of minimum rectangle(
        sides are parallel to coordinate axes) that consists the rectangle
        of eyebrow.

    Returns
    -------
    None.

    """
    surface = pygame.Surface([200, 100], pygame.SRCALPHA)
    rect(surface, BLACK, [0, 0, 90, 10])
    surface_rot = pygame.transform.rotate(surface, 25)
    screen.blit(surface_rot, [x, y])


main()
pygame.quit()
































