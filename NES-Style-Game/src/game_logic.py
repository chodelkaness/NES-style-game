import pygame
from player import Player
from level import Level
from background import Background
from ui import UI

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.background = Background()
        self.player = Player()
        self.level = Level(screen)
        self.ui = UI(screen)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.level.enemies)
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.level.update()
        self.score += 1
        self.ui.update(self.score)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.background.draw(self.screen)
        self.player.draw(self.screen)
        self.level.draw()
        self.ui.draw()