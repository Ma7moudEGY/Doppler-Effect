import pygame

pygame.font.init()
text_font = pygame.font.SysFont("comicsans", 20)

class Body:
    def __init__(self, x, y, color, velocity, name):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = velocity
        self.name = name 
        self.text = text_font.render(str(self.name), True, self.color)
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), 15)
        text_width = self.text.get_width()
        win.blit(self.text,(self.x - text_width/2 , self.y - 50))

    def move(self):
        self.x += self.velocity/10