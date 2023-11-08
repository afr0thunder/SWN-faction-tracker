# import libraries
import pygame
from screen_left import Sector, GridWindow
from screen_right import Button, Text, Tabs, TabWindow
from mouse import MousePosition
from random_generators import create_system_set
from classes_solar import Hex

# ---------- COLORS ---------- #
DARK_BLUE = (22, 72, 99)
MEDIUM_BLUE = (66, 125, 157)
GRAY_BLUE = (155, 190, 200)
LIGHT_BLUE = (221, 242, 253)
TEXT_WHITE = (255, 255, 255)
BACKGROUND_COLOR = GRAY_BLUE
HEX_HIGHLIGHT_COLOR = 'cyan'

# ---------- CONSTANTS ---------- #
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
GRID_WIDTH = 8
GRID_HEIGHT = 10
FONT_SIZE = 20
ZOOM_INCREMENT = 1
NAVIGATE_INCREMENT = 10
DRAG_SENSITIVITY = 0.6
STARTING_SEG_LENGTH = 75
STARTING_GRID_POSITION = (75, 75)
SELECTED_GRID_SPACE = (0, 0)
SYSTEM_SET = create_system_set(row=GRID_HEIGHT, col=GRID_WIDTH)
TAB_ARRAY = ['SYSTEM', 'STARS', 'PLANETS', 'ANOMALIES', 'FACTION', 'OTHER']
dragging = False
starting_position = (0, 0)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Stars Without Number: Sector and Faction Tracker')
clock = pygame.time.Clock()
running = True
dt = 0

# Define center screen mid point
centerscreen = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Track mouse coordinates
mouse = MousePosition()
font = pygame.font.Font(None, 36)

# Initiate left-hand grid screen
grid_screen = GridWindow(screen, screen.get_width() / 2, screen.get_height(), border_color=DARK_BLUE)
sector = Sector(STARTING_GRID_POSITION, screen, SYSTEM_SET, seg_length=STARTING_SEG_LENGTH, grid_width=GRID_WIDTH,
                grid_height=GRID_HEIGHT, hex_highlight_color=HEX_HIGHLIGHT_COLOR)

# Define tabs index for right screen
main_index = Tabs(screen, TAB_ARRAY, SCREEN_WIDTH // 2, 30, (SCREEN_WIDTH // 2, 0), color=BACKGROUND_COLOR, selected_color=LIGHT_BLUE, text_color=DARK_BLUE, font_size=FONT_SIZE)
tab_window = TabWindow(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30 - 30 - 10, (SCREEN_WIDTH // 2, 30), color=LIGHT_BLUE, text_color=DARK_BLUE, font_size=FONT_SIZE)

# Buttons
system_button = Button(screen, 'GENERATE SYSTEMS', 150, 30, ((SCREEN_WIDTH - 75 - 5 - 150 - 5 - 150 - 5 - 150 - 5 - 150 - 5), (SCREEN_HEIGHT - 20)), font_size=FONT_SIZE, color=DARK_BLUE, text_color=LIGHT_BLUE)
exit_button = Button(screen, 'EXIT', 150, 30, ((SCREEN_WIDTH - 75 - 5), (SCREEN_HEIGHT - 20)), font_size=FONT_SIZE, color=DARK_BLUE, text_color=LIGHT_BLUE)
load_button = Button(screen, 'LOAD', 150, 30, ((SCREEN_WIDTH - 75 - 5 - 150 - 5), (SCREEN_HEIGHT - 20)), font_size=FONT_SIZE, color=DARK_BLUE, text_color=LIGHT_BLUE)
save_button = Button(screen, 'SAVE', 150, 30, ((SCREEN_WIDTH - 75 - 5 - 150 - 5 - 150 - 5), (SCREEN_HEIGHT - 20)), font_size=FONT_SIZE, color=DARK_BLUE, text_color=LIGHT_BLUE)
grid_height_up = Button(screen, '+', 20, 15, (((SCREEN_WIDTH // 2) + 10 + 4), (SCREEN_HEIGHT - 28)), font_size=FONT_SIZE, color=DARK_BLUE, text_color=LIGHT_BLUE)
grid_height_down = Button(screen, '-', 20, 15, (((SCREEN_WIDTH // 2) + 10 + 4), (SCREEN_HEIGHT - 12)), font_size=FONT_SIZE, color=DARK_BLUE, text_color=LIGHT_BLUE)
grid_width_up = Button(screen, '+', 20, 15, (((SCREEN_WIDTH // 2) + 10 + 4 + 150), (SCREEN_HEIGHT - 28)), font_size=FONT_SIZE, color=DARK_BLUE, text_color=LIGHT_BLUE)
grid_width_down = Button(screen, '-', 20, 15, (((SCREEN_WIDTH // 2) + 10 + 4 + 150), (SCREEN_HEIGHT - 12)), font_size=FONT_SIZE, color=DARK_BLUE, text_color=LIGHT_BLUE)
faction_button = Button(screen, 'GENERATE FACTIONS', 150, 30, ((SCREEN_WIDTH - 75 - 5 - 150 - 5 - 150 - 5 - 150 - 5), (SCREEN_HEIGHT - 20)), font_size=FONT_SIZE, color=DARK_BLUE, text_color=LIGHT_BLUE)

# Texts
dimension_text = Text(screen, f'{GRID_HEIGHT} rows x {GRID_WIDTH} cols', 50, 30, ((SCREEN_WIDTH // 2) + 89, SCREEN_HEIGHT - 20), color=BACKGROUND_COLOR, text_color=DARK_BLUE, font_size=FONT_SIZE)

while running:
    # update mouse coordinates and display
    mouse.update_self()
    mouse_position = (mouse.x, mouse.y)
    mouse_buttons = mouse.buttons

    # poll for events
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse wheel scrolling for zooming in and out
        if event.type == pygame.MOUSEWHEEL:
            # Check if the mouse is on the left-hand side (where the grid is)
            if mouse_position[0] < SCREEN_WIDTH // 2:
                # Adjust the hex_radius based on the scroll direction
                # event.y > 0 means scrolling up, event.y < 0 means scrolling down
                if event.y > 0:
                    sector.hex_radius += ZOOM_INCREMENT
                elif event.y < 0:
                    sector.hex_radius -= ZOOM_INCREMENT
                # Prevent the hex_radius from getting too small or too big
                sector.hex_radius = max(10, min(sector.hex_radius, 200))

        # Drag the grid screen with the mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mouse_position[0] < SCREEN_WIDTH // 2:
                dragging = True
                pygame.mouse.get_rel()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False
        if dragging:
            change = pygame.mouse.get_rel()
            sector.corner_x += change[0] * DRAG_SENSITIVITY
            sector.corner_y += change[1] * DRAG_SENSITIVITY

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the event was a click on the left mouse button
            if event.button == 1 and mouse_position[0] <= SCREEN_WIDTH // 2:  # 1 is the left mouse button
                # Now check each hex to see if it was clicked
                for i in range(len(sector.grid_array)):
                    hexagon = Hex(sector.grid_array[i], screen, mouse_position, mouse_buttons,
                                  sector.grid_space_array[i],
                                  color=sector.color, length=sector.hex_radius, width=sector.line_width,
                                  empty=sector.grid_space_array[i] not in sector.system_set)
                    if hexagon.contains_point(mouse_position):
                        SELECTED_GRID_SPACE = sector.grid_space_array[i]
                        break  # No need to check the other hexes

            elif event.button == 1 and mouse_position[0] >= SCREEN_WIDTH // 2:
                if grid_height_up.contains_point(mouse_position):
                    GRID_HEIGHT += 1
                if grid_height_down.contains_point(mouse_position):
                    GRID_HEIGHT -= 1
                if grid_width_up.contains_point(mouse_position):
                    GRID_WIDTH += 1
                if grid_width_down.contains_point(mouse_position):
                    GRID_WIDTH -= 1
                dimension_text.text = f'{GRID_HEIGHT} rows x {GRID_WIDTH} cols'

                if exit_button.contains_point(mouse_position):
                    running = False

                if system_button.contains_point(mouse_position):
                    sector.grid_width = GRID_WIDTH
                    sector.grid_height = GRID_HEIGHT
                    SYSTEM_SET = create_system_set(row=GRID_HEIGHT, col=GRID_WIDTH)
                    sector.system_set = SYSTEM_SET
                main_index.update_tab(mouse_position)

    # update screen elements
    screen.fill(BACKGROUND_COLOR)
    grid_screen.draw_screen()

    # Draw Tabs, Buttons, and Texts
    main_index.draw_tabs()
    tab_window.draw_tab()
    system_button.update(mouse_position)
    faction_button.update((mouse_position))
    exit_button.update(mouse_position)
    load_button.update(mouse_position)
    save_button.update(mouse_position)
    grid_height_up.update(mouse_position)
    grid_height_down.update(mouse_position)
    grid_width_up.update(mouse_position)
    grid_width_down.update(mouse_position)
    dimension_text.draw_text()


    text = font.render(f'{SELECTED_GRID_SPACE[0] + 1}, {SELECTED_GRID_SPACE[1] + 1}', True, TEXT_WHITE)
    screen.blit(text, ((SCREEN_WIDTH * 0.75) - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    # Set clip area for the left-hand side of the screen
    clip_area = pygame.Rect(0, 0, screen.get_width() / 2, screen.get_height())
    screen.set_clip(clip_area)
    # Draw hexagonal grid within the clip area
    sector.create_grid()
    sector.draw_grid(mouse_position, mouse_buttons)
    # Reset clip area to the whole screen
    screen.set_clip(None)

    # draw border
    grid_screen.draw_border()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        sector.corner_y -= NAVIGATE_INCREMENT
    if keys[pygame.K_UP]:
        sector.corner_y += NAVIGATE_INCREMENT
    if keys[pygame.K_RIGHT]:
        sector.corner_x -= NAVIGATE_INCREMENT
    if keys[pygame.K_LEFT]:
        sector.corner_x += NAVIGATE_INCREMENT
    if keys[pygame.K_EQUALS]:
        sector.hex_radius += ZOOM_INCREMENT
    if keys[pygame.K_MINUS]:
        sector.hex_radius -= ZOOM_INCREMENT

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
