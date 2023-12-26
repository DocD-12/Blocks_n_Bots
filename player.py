import pygame


class Team:
    def __init__(self, num):
        self.scores = 0
        self.players = []
        self.number = num
        if num == 0:
            self.name = 'Red'
            self.color = (255, 0, 0)
        elif num == 1:
            self.name = 'Blue'
            self.color = (0, 0, 255)

    def add_player(self, player):
        player.to_team(self.name, self.number, self.color)
        player.image.fill(self.color)
        self.players.append(player)

    def get_scores(self):
        return self.scores


class FieldObject(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(topleft=(x * size, (y + 2) * size))


class Player(FieldObject):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.x = x
        self.y = y
        self.team = 0
        self.color = (0, 0, 0)
        self.team_color = (0, 0, 0)
        self.team_name = 'Null'
        self.team_num = 0

    def to_team(self, name, num, color):
        self.team_name = name
        self.team_num = num
        self.team_color = color
