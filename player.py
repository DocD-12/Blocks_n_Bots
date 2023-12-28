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
        self.rect = self.image.get_rect(topleft=(x * size, y * size))
        self.tile_size = size


class Player(FieldObject):
    def __init__(self, x, y, size, human=False):
        super().__init__(x, y, size)
        self.x = x
        self.y = y
        self.team = 0
        self.color = (0, 0, 0)
        self.team_color = (0, 0, 0)
        self.team_name = 'Null'
        self.team_num = 0
        self.id = None
        self.human = human

        self.walk_buffer = 50
        self.pos = pygame.math.Vector2(x, y) * size
        self.dirvec = pygame.math.Vector2(0, 0)
        self.last_pos = self.pos
        self.next_pos = self.pos

        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.between_tiles = False

        self.image = pygame.Surface((size, size))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))

        self.speed = 1 * size
        self.lock = 0

    def to_team(self, name, num, color):
        self.team_name = name
        self.team_num = num
        self.team_color = color

    def set_id(self, player_id):
        self.id = player_id

    def update(self, dt):
        self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))

        if self.pos != self.next_pos:
            delta = self.next_pos - self.pos
            if delta.length() > (self.dirvec * self.speed * dt).length():
                self.pos += self.dirvec * self.speed * dt
            else:
                self.pos = self.next_pos
                self.dirvec = pygame.math.Vector2(0, 0)
                self.between_tiles = False
        else:
            self.lock = 0

        self.rect.topleft = self.pos

    def step(self, ndv):
        self.dirvec = ndv
        self.between_tiles = True
        current_index = self.rect.centerx // self.tile_size, self.rect.centery // self.tile_size
        self.last_pos = pygame.math.Vector2(current_index) * self.tile_size
        self.next_pos = self.last_pos + self.dirvec * self.tile_size

    def make_move(self, grid):
        if self.id == 10:
            if grid[self.y][self.x + 1] == 0:
                self.right()
        if self.id == 20:
            print(grid[self.y + 1][self.x])
            print("Coords:", self.x, self.y)
            if grid[self.y + 1][self.x] == 0:
                self.down()

    def left(self):
        new_dir_vec = pygame.math.Vector2(0, 0)
        if self.lock == 0:
            self.lock = 1
            self.x = self.x - 1
            new_dir_vec = pygame.math.Vector2(-1, 0)

        if new_dir_vec != pygame.math.Vector2(0, 0):
            self.step(new_dir_vec)

    def right(self):
        new_dir_vec = pygame.math.Vector2(0, 0)
        if self.lock == 0:
            self.lock = 1
            self.x = self.x + 1
            new_dir_vec = pygame.math.Vector2(1, 0)

        if new_dir_vec != pygame.math.Vector2(0, 0):
            self.step(new_dir_vec)

    def down(self):
        new_dir_vec = pygame.math.Vector2(0, 0)
        if self.lock == 0:
            self.lock = 1
            self.y = self.y + 1
            new_dir_vec = pygame.math.Vector2(0, 1)

        if new_dir_vec != pygame.math.Vector2(0, 0):
            self.step(new_dir_vec)

    def up(self):
        new_dir_vec = pygame.math.Vector2(0, 0)
        if self.lock == 0:
            self.lock = 1
            self.y = self.y - 1
            new_dir_vec = pygame.math.Vector2(0, -1)

        if new_dir_vec != pygame.math.Vector2(0, 0):
            self.step(new_dir_vec)
