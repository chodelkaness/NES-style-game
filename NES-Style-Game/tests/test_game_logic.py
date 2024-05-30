import pygame
from game_logic import Game

def test_game_initialization():
    screen = pygame.Surface((800, 600))
    game = Game(screen)
    assert game.player.rect.center == (400, 300)
    assert len(game.level.enemies) == 10

def test_player_movement():
    player = Player()
    keys = {pygame.K_LEFT: True, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False}
    initial_x = player.rect.x
    player.update(keys)
    assert player.rect.x < initial_x