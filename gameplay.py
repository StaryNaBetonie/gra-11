import pygame
from planet import Planet
from player import Player
from random import randint

class Gameplay:
    def __init__(self) -> None:
        self.visible_sprites = pygame.sprite.Group()
        self.obsticle_sprites = pygame.sprite.Group()

        self.player = Player(self.visible_sprites, (40, 540))
        self.planets = []
        self.generate_level()
    
    def generate_level(self):
        for i in range(10):
            planet = Planet(self.visible_sprites, (randint(200, 1900), randint(200, 900)), (212, 214, 114))
            self.planets.append(planet)
    
    def gravity_logic(self, planet: Planet):
        guiding_radius = pygame.Vector2()
        guiding_radius.x = planet.rect.centerx - self.player.rect.centerx
        guiding_radius.y = planet.rect.centery - self.player.rect.centery
        distance = guiding_radius.magnitude()

        # if distance > planet.gravitational_field_rad: return
        if distance == 0: return
        
        self.player.velocity.x += (guiding_radius.x / distance) * planet.gravity_force / max(distance, 64)**2
        self.player.velocity.y += (guiding_radius.y / distance) * planet.gravity_force / max(distance, 64)**2
    
    def update(self):
        for planet in self.planets: self.gravity_logic(planet)
        self.player.update()
    
    def render(self, screen):
        self.visible_sprites.draw(screen)
        for planet in self.planets: planet.draw_orbit(screen)