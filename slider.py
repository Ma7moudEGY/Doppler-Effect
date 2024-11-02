import pygame

WIDTH = 150
HEIGHT = 20

class Slider:
    def __init__(self, x, y, orientation, body):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.body = body

    def draw(self, win):
        if self.orientation.lower() == "h":
            rect = pygame.Rect(self.x, self.y ,WIDTH,HEIGHT)
            pygame.draw.rect(win, "white", rect)
            pygame.draw.circle(win, "red", (self.x + WIDTH // 2, self.y + HEIGHT // 2), 10)

        elif self.orientation.lower() == "v":
            rect = pygame.Rect(self.x, self.y,HEIGHT,WIDTH)
            pygame.draw.rect(win, "red", rect)
            pygame.draw.circle(win, "white", (self.x + HEIGHT // 2, self.y + WIDTH // 2), 10)
