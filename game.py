import pygame
import random
import time


class Game:
    def __init__(self, size):
        self.grid = [[-1 if (i == 0 or i == size - 1 or j == 0 or j == size -1) else 0
                      for j in range(size)] for i in range(size)]

    def start(self):
        pygame.init()

        screen_width = 1000
        screen_height = 1000
        win = pygame.display.set_mode((screen_width, screen_height))
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
            win.fill(grey)
            self.draw()

            # Отображение ИИ ботов

            # Отображение текущих очков
            font = pygame.font.Font(None, 36)
            text = font.render(f'Player 1: 0  Player 2: 0', True, white)
            win.blit(text, (10, 10))

            # Отображение времени игры
            passed_time = int(time.time() - start_time)
            remaining_time = max(0, game_duration - passed_time)
            time_text = font.render(f'Time: {remaining_time // 60}:{remaining_time % 60:02d}', True, white)
            win.blit(time_text, (screen_width - 150, 10))

            # Обновление экрана
            pygame.display.update()

            # Проверка окончания времени игры
            if passed_time >= game_duration:
                running = False

    def print_grid(self):
        print(*self.grid, sep='\n')

    def draw(self):
        for x in range(0, screen_width, 50):
            pygame.draw.line(win, white, (x, 0), (x, screen_height))
        for y in range(0, screen_height, 50):
            pygame.draw.line(win, white, (0, y), (screen_width, y))