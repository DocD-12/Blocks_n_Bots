import pygame
import random

# Initialize Pygame
pygame.init()

# Define the size of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the size of the grid and the cell size
GRID_SIZE = 10
CELL_SIZE = 40

# Calculate the size of the grid in pixels
GRID_WIDTH = GRID_SIZE * CELL_SIZE
GRID_HEIGHT = GRID_SIZE * CELL_SIZE

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("AI Bots Game")

# Generate a random maze with obstacles
def generate_maze():
    maze = []
    for _ in range(GRID_SIZE):
        row = [True if random.random() < 0.3 else False for _ in range(GRID_SIZE)]
        maze.append(row)
    return maze

# Draw the grid on the game window
def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(window, WHITE, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(window, WHITE, (0, y), (WINDOW_WIDTH, y))

# Draw the maze on the game window
def draw_maze(maze):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if maze[x][y]:
                pygame.draw.rect(window, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Draw the players on the game window
def draw_players(player1_pos, player2_pos):
    pygame.draw.rect(window, RED, (player1_pos[0] * CELL_SIZE, player1_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(window, GREEN, (player2_pos[0] * CELL_SIZE, player2_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Game loop
def game_loop():
    # Generate random positions for the players
    player1_pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
    player2_pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))

    # Generate the maze
    maze = generate_maze()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.fill(BLACK)

        # Draw the grid, maze, and players
        draw_grid()
        draw_maze(maze)
        draw_players(player1_pos, player2_pos)

        pygame.display.update()

# Start the game loop
game_loop()