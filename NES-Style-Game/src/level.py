import pygame
import random
from enemy import Enemy
from background import Background

class Level:
    def __init__(self, screen, level_num):
        self.screen = screen
        self.level_num = level_num
        self.enemies = pygame.sprite.Group()
        self.background = Background(f'background_tile_{level_num}.png')
        
        if level_num == 1:
            for _ in range(5):
                enemy = Enemy(random.randint(0, 768), random.randint(-100, -40), 'enemy1.png')
                self.enemies.add(enemy)
        elif level_num == 2:
            for _ in range(5):
                enemy = Enemy(random.randint(0, 768), random.randint(-100, -40), 'enemy2.png')
                self.enemies.add(enemy)

    def update(self):
        self.enemies.update()

    def draw(self):
        self.background.draw(self.screen)
        self.enemies.draw(self.screen)