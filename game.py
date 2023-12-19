import pygame
import random
import time

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (127, 127, 127)

class Game:
    def __init__(self, size, tile_size=32):
        self.grid = [[-1 if (i == 0 or i == size - 1 or j == 0 or j == size -1) else 0
                      for j in range(size)] for i in range(size)]

        self.screen_width = size * tile_size
        self.screen_height = size * tile_size
        self.win = None
        self.tile_size = tile_size
        self.player_speed = 3 * tile_size

    def start(self):
        pygame.init()

        self.win = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Capture The Coin Game")

        running = True
        start_time = time.time()
        game_duration = 105  # Время в секундах
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Управление с клавиатуры для четвертого игрока
            keys = pygame.key.get_pressed()
            # player4.move(keys)

            # Отображение игрового поля
            self.win.fill(grey)
            self.draw()

            # Отображение ИИ ботов

            # Отображение текущих очков
            font = pygame.font.Font(None, 36)
            text = font.render(f'Player 1: 0  Player 2: 0', True, white)
            self.win.blit(text, (10, 10))

            # Отображение времени игры
            passed_time = int(time.time() - start_time)
            remaining_time = max(0, game_duration - passed_time)
            time_text = font.render(f'Time: {remaining_time // 60}:{remaining_time % 60:02d}', True, white)
            self.win.blit(time_text, (self.screen_width - 150, 10))

            # Обновление экрана
            pygame.display.update()

            # Проверка окончания времени игры
            if passed_time >= game_duration:
                running = False

    def print_grid(self):
        print(*self.grid, sep='\n')

    def draw(self):
        for x in range(0, self.screen_width, self.tile_size):
            pygame.draw.line(self.win, white, (x, 0), (x, self.screen_height))
        for y in range(0, self.screen_height, self.tile_size):
            pygame.draw.line(self.win, white, (0, y), (self.screen_width, y))

    def get_tile_size(self):
        return self.tile_size