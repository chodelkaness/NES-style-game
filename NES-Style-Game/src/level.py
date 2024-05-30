import pygame
from enemy import Enemy

class Level:
    def __init__(self, screen):
        self.screen = screen
        self.enemies = pygame.sprite.Group()
        for _ in range(10):
            enemy = Enemy(random.randint(0, 768), random.randint(-100, -40))
            self.enemies.add(enemy)

    def update(self):
        self.enemies.update()

    def draw(self):
        self.enemies.draw(self.screen)