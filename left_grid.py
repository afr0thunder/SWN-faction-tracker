import random
import pygame
import math


class Hex:
    def __init__(self, center_point, surface, mouse_position, color='black', length=10, width=1):
        self.center = center_point
        self.surface = surface
        self.color = color
        self.width = width
        self.length = length
        self.current_mouse = mouse_position
        self.draw_hex(self.center)

    def draw_hex(self, hex_center):
        length = self.length
        s1 = [x * length for x in (-1, 0)]
        s2 = [x * length for x in (-0.5, math.sqrt(3) / 2)]
        s3 = [x * length for x in (0.5, math.sqrt(3) / 2)]
        s4 = [x * length for x in (1, 0)]
        s5 = [x * length for x in (0.5, -1 * (math.sqrt(3) / 2))]
        s6 = [x * length for x in (-0.5, -1 * (math.sqrt(3) / 2))]

        p1 = [sum(x) for x in zip(s1, hex_center)]
        p2 = [sum(x) for x in zip(s2, hex_center)]
        p3 = [sum(x) for x in zip(s3, hex_center)]
        p4 = [sum(x) for x in zip(s4, hex_center)]
        p5 = [sum(x) for x in zip(s5, hex_center)]
        p6 = [sum(x) for x in zip(s6, hex_center)]

        adjustment = 0.75

        if self.center[0] - (self.length * adjustment) < self.current_mouse[0] < self.center[0] + (
                self.length * adjustment) and self.center[1] - (self.length * adjustment) < self.current_mouse[1] < \
                self.center[1] + (self.length * adjustment):
            self.color = 'cyan'
            self.width = 0

        pygame.draw.polygon(self.surface, self.color, (p1, p2, p3, p4, p5, p6), self.width)


class Sector:
    def __init__(self, grid_corner, surface, color='black', seg_length=10, line_width=1, grid_height=10, grid_width=8):
        self.corner_x = grid_corner[0]
        self.corner_y = grid_corner[1]
        self.surface = surface
        self.color = color
        self.hex_radius = seg_length
        self.line_width = line_width
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.grid_array = []
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
        x_spacing = 0.9
        y_spacing = 1.2
        offset = math.sqrt(3) * self.hex_radius
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                x = offset * col * x_spacing
                y = 1.5 * self.hex_radius * (row + 0.5 * (col % 2)) * y_spacing
                point = [x + self.corner_x, y + self.corner_y]
                array.append(point)

        self.grid_array = array

    def draw_grid(self, mouse_position):
        for loc in self.grid_array:
            Hex(loc, self.surface, mouse_position, color=self.color, length=self.hex_radius, width=self.line_width)


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
        pygame.draw.rect(self.grid_surface, self.border_color, ((0, 0), (self.width, self.height)), width=10)
        self.surface.blit(self.grid_surface, (self.x, self.y))
