import random
import pygame
import math

class Hex:
    def __init__(self, center_point, surface, color='black', length=10, width=1):
        self.center = center_point
        self.surface = surface
        self.color = color
        self.width = width
        self.length = length
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

        pygame.draw.polygon(self.surface, self.color, (p1, p2, p3, p4, p5, p6), self.width)

class Sector:
    def __init__(self, grid_center, surface, color='black', length=10, width=1):
        self.center = grid_center
        self.surface = surface
        self.color = color
        self.length = length
        self.width = width

