class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 25

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)