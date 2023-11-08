from classes_solar import Hex
import pygame
import math


class Sector:
    def __init__(self, grid_corner, surface, system_set, color='black', seg_length=10, line_width=1, grid_height=10, grid_width=8, hex_highlight_color='yellow'):
        self.corner_x = grid_corner[0]
        self.corner_y = grid_corner[1]
        self.surface = surface
        self.color = color
        self.hex_highlight_color = hex_highlight_color
        self.hex_radius = seg_length
        self.line_width = line_width
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.grid_array = []
        self.grid_space_array = []
        self.system_set = system_set
        self.create_grid()

    def print_attributes(self):
        print(f'Corner: {self.corner}')
        print(f'Surface: {self.surface}')
        print(f'Color: {self.color}')
        print(f'Segment Length: {self.hex_radius}')
        print(f'Line Width: {self.line_width}')
        print(f'Grid Rows: {self.grid_width}')
        print(f'Grid Columns: {self.grid_height}')
        print(f'Grid Array Length: {len(self.grid_array)}')

    def create_grid(self):
        array = []
        grid_spaces = []
        x_spacing = 0.9
        y_spacing = 1.2
        offset = math.sqrt(3) * self.hex_radius
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                x = offset * col * x_spacing
                y = 1.5 * self.hex_radius * (row + 0.5 * (col % 2)) * y_spacing
                point = [x + self.corner_x, y + self.corner_y]
                array.append(point)
                grid_spaces.append((row, col))

        self.grid_array = array
        self.grid_space_array = grid_spaces

    def draw_grid(self, mouse_position, mouse_buttons):
        for i in range(len(self.grid_array)):
            if self.grid_space_array[i] in self.system_set:
                empty = False
            else:
                empty = True
            Hex(self.grid_array[i], self.surface, mouse_position, mouse_buttons, self.grid_space_array[i], color=self.color,
                length=self.hex_radius, width=self.line_width, empty=empty, highlight_color=self.hex_highlight_color)


class GridWindow:
    def __init__(self, surface, width, height, x=0, y=0, color='white', border_color='black'):
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

    def draw_border(self):
        pygame.draw.rect(self.surface, self.border_color, ((0, 0), (self.width, self.height)), width=10)
