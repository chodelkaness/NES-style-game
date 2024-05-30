import pygame

def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    except pygame.error as e:
        print(f"Cannot load image: {name}")
        raise SystemExit(e)