import pygame
from player import Player
from level import Level
from background import Background
from ui import UI

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.background = Background('background_tile.png')
        self.player = Player()
        self.level = Level(screen, 1)  # Starting with level 1
        self.ui = UI(screen)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.level.enemies)
        self.score = 0
        self.health = 100

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.level.update()
        self.score += 1
        self.health -= 1  # Decrease health as an example
        self.ui.update(self.score, self.health)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.background.draw(self.screen)
        self.player.draw(self.screen)
        self.level.draw()
        self.ui.draw()