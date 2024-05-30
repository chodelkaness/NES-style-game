python

import pygame
import random
from enemy import Enemy

class Level:
    def __init__(self, screen):
        self.screen = screen
        self.enemies = pygame.sprite.Group()
        for _ in range(5):
            enemy = Enemy(random.randint(0, 768), random.randint(-100, -40), 'enemy1.png')
            self.enemies.add(enemy)
        for _ in range(5):
            enemy = Enemy(random.randint(0, 768), random.randint(-100, -40), 'enemy2.png')
            self.enemies.add(enemy)

    def update(self):
        self.enemies.update()

    def draw(self):
        self.enemies.draw(self.screen)