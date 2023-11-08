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
        self.hover_color = text_color
        self.text_color = text_color
        self.text_hover_color = color
        self.is_hovering = False
        self.draw_button()

    def draw_button(self):
        draw_color = self.hover_color if self.is_hovering else self.color
        draw_text = self.text_hover_color if self.is_hovering else self.text_color

        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.text, True, draw_text)

        # Create a rectangle for the button
        button_rect = pygame.Rect(self.position[0] - (self.width // 2), self.position[1] - (self.height // 2),
                                  self.width, self.height)

        # Draw a rounded rectangle on the surface instead of creating a new surface
        border_radius = 12  # Example border radius; you can make this an attribute or a parameter
        pygame.draw.rect(self.surface, draw_color, button_rect, border_radius=border_radius)

        # Get text rectangle and position it in the center of the button
        text_rect = text.get_rect(center=button_rect.center)

        # Blit the text onto the main surface, not onto the button because we're not using a separate button surface anymore
        self.surface.blit(text, text_rect)

    def contains_point(self, point):
        if self.position[0] - (self.width // 2) < point[0] < self.position[0] + (
                self.width // 2) and self.position[1] - (self.height // 2) < point[1] < \
                self.position[1] + (self.height // 2):
            return True
        return False

    def update(self, mouse_position):
        # Update the hovering state based on the mouse position
        self.is_hovering = self.contains_point(mouse_position)
        self.draw_button()  # Redraw the button with the updated state


class Text:
    def __init__(self, surface, text, width, height, position, color='white', text_color='black', font_size=10):
        self.surface = surface
        self.text = text
        self.font_size = font_size
        self.width = width
        self.height = height
        self.position = position
        self.color = color
        self.text_color = text_color
        self.draw_text()

    def draw_text(self):

        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.text, True, self.text_color)

        # Create a rectangle for the button
        button_rect = pygame.Rect(self.position[0] - (self.width // 2), self.position[1] - (self.height // 2),
                                  self.width, self.height)

        pygame.draw.rect(self.surface, self.color, button_rect)

        # Get text rectangle and position it in the center of the button
        text_rect = text.get_rect(center=button_rect.center)

        # Blit the text onto the main surface
        self.surface.blit(text, text_rect)


class InfoWindow:
    def __init__(self, surface, width, height, x, y, color='white', border_color='black'):
        self.surface = surface
        self.width = width
        self.x = x
        self.y = y
        self.height = height
        self.color = color
        self.border_color = border_color
        self.position = ((0, 0), (self.width, self.height))
        self.grid_surface = pygame.Surface((width, height))
        self.draw_screen()

    def draw_screen(self):
        pygame.draw.rect(self.grid_surface, self.color, ((0, 0), (self.width, self.height)))
        self.surface.blit(self.grid_surface, (self.x, self.y))
