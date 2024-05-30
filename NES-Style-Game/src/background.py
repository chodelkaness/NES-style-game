import pygame
import os

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets/images', image_file)).convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self, screen):
        for x in range(0, 800, 32):
            for y in range(0, 600, 32):
                screen.blit(self.image, (x, y))