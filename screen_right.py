import pygame


class Button:
    def __init__(self, surface, text, width, height, position, color='white', text_color='black', font_size=10):
        self.surface = surface
        self.text = text
        self.font_size = font_size
        self.width = width
        self.height = height
        self.position = position
        self.color = color
        self.text_color = text_color
        self.draw_button()

    def draw_button(self):
        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.text, True, self.text_color)
        button = pygame.Surface((self.width, self.height))
        button.fill(self.color)

        # Corrected the blit operation to place the text onto the button
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        button.blit(text, text_rect)

        # Blit the button surface onto the main surface at the specified position
        self.surface.blit(button, self.position)
