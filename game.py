import pygame
import random
import time
from player import *

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (127, 127, 127)


class Game:
    def __init__(self, size, tile_size=32, info_size=2):
        self.grid = [[-1 if (i == 0 or i == size - 1 or j == 0 or j == size - 1) else 0
                      for j in range(size)] for i in range(size)]

        self.info_size = info_size
        self.screen_width = size * tile_size
        self.screen_height = (size + info_size) * tile_size
        self.window = None
        self.tile_size = tile_size
        self.player_speed = 3 * tile_size
        self.n = size
        self.walls = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.teams = []
        self.start_time = None
        self.game_duration = 0

    def add_team(self, team):
        self.teams.append(team)

    def set_time(self, time_duration):
        self.game_duration = time_duration

    def start(self):
        pygame.init()
        clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Capture The Coin Game")

        running = True
        self.start_time = time.time()

        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == -1:
                    x = FieldObject(i, j, self.tile_size)
                    self.walls.add(x)

        for team in self.teams:
            for player in team.players:
                self.all_sprites.add(player)

        # -------------------------------------------------------------------------------
        while running:
            dt = clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Управление с клавиатуры
            # keys = pygame.key.get_pressed()
            for team in self.teams:
                for player in team.players:
                    player.make_move(self.grid)

            # Отображение игроков
            for team in self.teams:
                for player in team.players:
                    player.update(dt)

            # Отображение блоков


            # Отображение игрового поля
            self.window.fill(white)
            self.draw_grid()
            self.walls.draw(self.window)
            self.all_sprites.draw(self.window)

            # Отображение информации об игре
            self.draw_game_info()

            # Обновление экрана
            pygame.display.update()

            # Проверка окончания времени игры
            if int(time.time() - self.start_time) >= self.game_duration > 0:
                running = False


    # ------------------------------------------------------------------------------
    def print_grid(self):
        print(*self.grid, sep='\n')

    def draw_grid(self):
        for x in range(0, self.screen_width, self.tile_size):
            pygame.draw.line(self.window, grey, (x, 0), (x, self.screen_height - (self.info_size + 1) * self.tile_size))
        for y in range(0, self.screen_height - self.info_size * self.tile_size, self.tile_size):
            pygame.draw.line(self.window, grey, (0, y), (self.screen_width, y))

    def draw_game_info(self):
        font = pygame.font.Font(None, self.tile_size)
        text = font.render(f'Team {self.teams[0].name}: 0', True, self.teams[0].color)
        self.window.blit(text, (0.5 * self.tile_size, (self.tile_size + 0.5) * self.n))
        # text = font.render(f'Team 2: 0', True, blue)
        # self.window.blit(text, (self.screen_width - 5 * self.tile_size, (self.tile_size + 0.5) * self.n))

        passed_time = int(time.time() - self.start_time)
        remaining_time = self.game_duration - passed_time
        if self.game_duration > 0:
            time_text = font.render(f'Time:   {remaining_time // 60}:{remaining_time % 60:02d}', True, black)
        else:
            time_text = font.render(f'Time:      {passed_time // 60}:{passed_time % 60:02d}', True, black)
        self.window.blit(time_text, (self.screen_width - self.n // 2 * self.tile_size, (self.tile_size + 0.5) * self.n))

    def get_tile_size(self):
        return self.tile_size
