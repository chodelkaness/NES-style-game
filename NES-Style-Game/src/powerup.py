import pygame
import os

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, image_file, effect):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets/images', image_file)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.effect = effect

    def apply_effect(self, player):
        if self.effect == 'heal':
            player.health += 10
        elif self.effect == 'speed':
            player.speed += 2
