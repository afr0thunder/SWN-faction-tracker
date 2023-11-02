import pygame

class MousePosition:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.update_position()

    def update_position(self):
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
