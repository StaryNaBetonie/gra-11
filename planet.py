import imp
import pygame
from support import get_circle_surface

class Planet(pygame.sprite.Sprite):
    def __init__(self, groups, pos, color) -> None:
        super().__init__(groups)
        self.image = get_circle_surface(64, color)
        self.rect = self.image.get_rect(center = pos)

        self.gravitational_field_rad = 200
        self.gravity_force = 2000
    
    def draw_orbit(self, screen):
        pygame.draw.circle(screen, 'white', self.rect.center, self.gravitational_field_rad, 2)