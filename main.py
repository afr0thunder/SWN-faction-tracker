# imports
import random
import pygame
from grid import Hex, Sector

# ---------- COLORS ---------- #
BACKGROUND_COLOR = "gray"
HEX_COLOR = "cyan"

# ---------- CONSTANTS ---------- #
SPEED = 300

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('SWN Faction Tracker')
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
centerscreen = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BACKGROUND_COLOR)

    pygame.draw.circle(screen, "red", player_pos, 40)
    hex = Hex(centerscreen, screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= SPEED * dt
    if keys[pygame.K_s]:
        player_pos.y += SPEED * dt
    if keys[pygame.K_a]:
        player_pos.x -= SPEED * dt
    if keys[pygame.K_d]:
        player_pos.x += SPEED * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()