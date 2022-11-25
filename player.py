import pygame
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos) -> None:
        super().__init__(groups)
        self.image = get_circle_surface(16, (114, 214, 202))
        self.rect = self.image.get_rect(center = pos)
        self.velocity = pygame.Vector2()

        self.mass = 1
    
    def bounce(self):
        if self.rect.left < 0:
            self.velocity.x = abs(self.velocity.x)
        elif self.rect.right > 1920:
            self.velocity.x = -abs(self.velocity.x)

        if self.rect.top < 0:
            self.velocity.y = abs(self.velocity.y)
        elif self.rect.bottom > 1080:
            self.velocity.y = -abs(self.velocity.y)


    def update(self):
        self.bounce()
        self.rect.center += self.velocity
        