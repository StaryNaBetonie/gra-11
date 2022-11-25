from lib2to3 import pygram
import pygame

def get_circle_surface(rad, color):
    surface = pygame.Surface((2 * rad, 2*rad), flags = pygame.SRCALPHA)
    pygame.draw.circle(surface, color, (rad, rad), rad)
    return surface

