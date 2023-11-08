import pygame
import math


class Hex:
    def __init__(self, center_point, surface, mouse_position, mouse_buttons, grid_space, color='black', length=10,
                 width=1, empty=True, highlight_color='yellow'):
        self.center = center_point
        self.x = center_point[0]
        self.y = center_point[1]
        self.surface = surface
        self.color = color
        self.hightlight_color = highlight_color
        self.width = width
        self.hex_radius = length
        self.grid_space = grid_space
        self.current_mouse = mouse_position
        self.current_mouse_buttons = mouse_buttons
        self.empty = empty
        self.system = None
        self.draw_hex(self.center)

    def draw_hex(self, hex_center):
        length = self.hex_radius
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

        if self.contains_point(self.current_mouse):
            self.color = self.hightlight_color
            self.width = 0

        pygame.draw.polygon(self.surface, self.color, (p1, p2, p3, p4, p5, p6), self.width)
        if not self.empty:
            self.system = SolarSystem(self.center, self.surface, self.current_mouse, self.grid_space, self.hex_radius)

    def contains_point(self, point):
        adjustment = 0.75
        if self.center[0] - (self.hex_radius * adjustment) < point[0] < self.center[0] + (
                self.hex_radius * adjustment) and self.center[1] - (self.hex_radius * adjustment) < point[1] < \
                self.center[1] + (self.hex_radius * adjustment):
            return True
        return False



class SolarSystem:
    def __init__(self, center_point, surface, mouse_position, grid_space, length, color='black', width=1):
        self.center = center_point
        self.x = center_point[0]
        self.y = center_point[1]
        self.surface = surface
        self.color = color
        self.width = width
        self.hex_radius = length
        self.grid_space = grid_space
        self.current_mouse = mouse_position
        self.draw_system()

    def draw_system(self):
        adjustment = 0.75
        pygame.draw.circle(self.surface, self.color, self.center, self.hex_radius * adjustment, width=1)
