# import libraries
import random
import pygame
from left_grid import Hex, Sector, GridWindow
from mouse import MousePosition

# ---------- COLORS ---------- #
BACKGROUND_COLOR = "gray"
HEX_COLOR = "cyan"

# ---------- CONSTANTS ---------- #
SPEED = 300

# pygame setup
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('SWN Faction Tracker')
clock = pygame.time.Clock()
running = True
dt = 0

# Define center screen mid point
centerscreen = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Track mouse coordinates
mouse = MousePosition()
font = pygame.font.Font(None, 36)

# Initiate left-hand grid screen
grid_screen = GridWindow(screen, screen.get_width() / 2, screen.get_height())
sector = Sector((50, 50), screen, seg_length=50)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update screen elements
    screen.fill(BACKGROUND_COLOR)
    grid_screen.draw_screen()

    #update mouse coordinates and display
    mouse.update_position()
    text = font.render(f'{mouse.mouse_x}, {mouse.mouse_y}', True, (255, 255, 255))
    screen.blit(text, ((width * 0.75) - text.get_width() // 2, height // 2 - text.get_height() // 2))

    # Set clip area for the left-hand side of the screen
    clip_area = pygame.Rect(0, 0, screen.get_width() / 2, screen.get_height())
    screen.set_clip(clip_area)
    # Draw hexagonal grid within the clip area
    sector.draw_grid()
    # Reset clip area to the whole screen
    screen.set_clip(None)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        sector.corner = (sector.corner[0], sector.corner[1] - 10)
    if keys[pygame.K_DOWN]:
        sector.corner = (sector.corner[0], sector.corner[1] + 10)
    if keys[pygame.K_LEFT]:
        sector.corner = (sector.corner[0] - 10, sector.corner[1])
    if keys[pygame.K_RIGHT]:
        sector.corner = (sector.corner[0] + 10, sector.corner[1])
    if keys[pygame.K_EQUALS]:
        sector.hex_radius += 5
    if keys[pygame.K_MINUS]:
        sector.hex_radius -= 5

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
