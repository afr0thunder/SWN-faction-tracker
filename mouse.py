import pygame

class MousePosition:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.buttons = (False, False, False)
        self.update_self()

    def update_self(self):
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.buttons = pygame.mouse.get_pressed(num_buttons = 3)
