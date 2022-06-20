import pygame

class Cube:
    def __init__(self, x, y, width, height, val=0, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.val = val
        self.color = color

    def __str__(self):
        return str(self.val)

    def draw(self, win):
        pygame.draw.rect(win, (211, 211, 211),
                         (self.x - 2, self.y - 2,
                          self.width + 4, self.height + 4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.val != 0:
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(str(self.val), True, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False
