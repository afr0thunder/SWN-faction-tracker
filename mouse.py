import pygame

class MousePosition:
    def __init__(self):
        self.mouse_x = 0
        self.mouse_y = 0
        self.update_position()

    def update_position(self):
        self.mouse_x = pygame.mouse.get_pos()[0]
        self.mouse_y = pygame.mouse.get_pos()[1]
