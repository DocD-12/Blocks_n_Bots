import pygame


class FieldObject(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(topleft=(x * size, (y+2) * size))


class Player(FieldObject):
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size)
        self.x = x
        self.y = y
        self.color = color
        if color == (255, 0, 0):
            self.team = 'R'
        elif color == (0, 0, 255):
            self.team = 'B'
        self.image.fill(self.color)
