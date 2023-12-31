import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Установка размеров окна
screen_width = 800
screen_height = 800
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Capture The Coin Game")

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)
grey = (128, 128, 128)
lgrey = (196, 196, 196)
dgrey = (64, 64, 64)


# Игровое поле
class Grid:
    def __init__(self, h, w, sq_size = 50):
        self.height = h
        self.width = w
        self.sq = [[-1 if (i == 0 or i == h - 1 or j == 0 or j == w - 1) else 0
                      for j in range(w)] for i in range(h)]
        self.size = sq_size


    def print_grid(self):
        print(*self.sq, sep='\n')
    def addplayer(self, x, y):
        self.sq[x][y] = 2
    def draw_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.sq[i][j] == 0:
                    pygame.draw.rect(win, lgrey, (i * self.size, j * self.size + 50, self.size - 1, self.size - 1))
                elif self.sq[i][j] == -1:
                    pygame.draw.rect(win, dgrey, (i * self.size, j * self.size + 50, self.size - 1, self.size - 1))
                elif self.sq[i][j] == 1:
                    pygame.draw.circle(win, red, (i * self.size, j * self.size + 50), self.size - 1)
                elif self.sq[i][j] == 2:
                    pygame.draw.circle(win, blue, (i * self.size + self.size / 2, j * self.size + 50 + self.size / 2), self.size / 2 - 1)

# Игрок
class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 25

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# Монетка
class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = yellow

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# Создание СЕТКИ
maingrid = Grid(16, 15, 50)
maingrid.addplayer(2, 2)

# Создание игроков
player1 = Player(50, 50, red)
player2 = Player(screen_width - 50, 50, blue)

# Создание монеток
coin1 = Coin(200, 300)
coin2 = Coin(600, 300)

# Создание ИИ ботов
class AIPlayer:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 20

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move_randomly(self):
        # Простое случайное движение для ИИ
        self.x += random.randint(-3, 3)
        self.y += random.randint(-3, 3)

# Создание ИИ ботов
bot1 = AIPlayer(50, screen_height - 50, green)
bot2 = AIPlayer(screen_width - 50, screen_height - 50, purple)
bot3 = AIPlayer(50, 50, orange)

# Создание четвертого игрока, управляемого с клавиатуры
class KeyboardPlayer:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 20

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self, keys):
        # Управление с клавиатуры
        if keys[pygame.K_LEFT]:
            self.x -= 3
        if keys[pygame.K_RIGHT]:
            self.x += 3
        if keys[pygame.K_UP]:
            self.y -= 3
        if keys[pygame.K_DOWN]:
            self.y += 3

player4 = KeyboardPlayer(screen_width - 50, screen_height - 50, yellow)

# Основной игровой цикл
running = True
start_time = time.time()
game_duration = 105  # Время в секундах
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление с клавиатуры для четвертого игрока
    keys = pygame.key.get_pressed()
    player4.move(keys)

    # Отображение игрового поля
    win.fill(grey)
    maingrid.draw_grid()

    # Отображение игроков
    player4.draw()

    # Отображение монеток
    coin1.draw()
    coin2.draw()

    # Отображение ИИ ботов
    bot1.move_randomly()
    bot2.move_randomly()
    bot3.move_randomly()
    bot1.draw()
    bot2.draw()
    bot3.draw()

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

# Завершение игры
pygame.quit()
