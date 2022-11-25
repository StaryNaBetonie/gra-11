import pygame
from gameplay import Gameplay

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN|pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.running = True
        self.events = {'w': False, 'a':False, 's':False, 'd':False}
        self.gameplay = Gameplay()
    
    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.screen = pygame.display.set_mode((1344, 758), pygame.SCALED)
                if event.key == pygame.K_w:
                    self.events['w'] = True
                if event.key == pygame.K_a:
                    self.events['a'] = True
                if event.key == pygame.K_s:
                    self.events['s'] = True
                if event.key == pygame.K_d:
                    self.events['d'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.events['w'] = False
                if event.key == pygame.K_a:
                    self.events['a'] = False
                if event.key == pygame.K_s:
                    self.events['s'] = False
                if event.key == pygame.K_d:
                    self.events['d'] = False

    def render(self):
        self.screen.fill((40, 40, 40))
        self.gameplay.render(self.screen)
        pygame.display.update()

    def main_loop(self):
        while self.running:
            self.clock.tick(60)
            self.get_events()
            self.render()
            self.gameplay.update()
    
if __name__ == '__main__':
    game = Game()
    game.main_loop()