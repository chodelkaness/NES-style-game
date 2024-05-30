import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.rect.bottom = 0
            self.rect.x = random.randint(0, 768)