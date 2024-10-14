import pygame
from constants import *

def handle_start_selection_events(running, grid_size = None, game_started = False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running[0] = False
        elif event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
            if event.type == pygame.KEYDOWN:
                grid_size = {
                    pygame.K_1: GRID_OPTIONS["2x2"],
                    pygame.K_2: GRID_OPTIONS["3x2"],
                    pygame.K_4: GRID_OPTIONS["4x4"],
                    pygame.K_5: GRID_OPTIONS["5x4"],
                    pygame.K_6: GRID_OPTIONS["6x6"]
                }.get(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                grid_size = check_mouse_click(mouse_pos)

            if grid_size:
                game_started = True

    return grid_size, game_started

def check_mouse_click(mouse_pos):
    """Check if a menu option has been clicked and return the corresponding grid size tuple."""
    if button_2x2.collidepoint(mouse_pos):
        return GRID_OPTIONS["2x2"]
    elif button_3x2.collidepoint(mouse_pos):
        return GRID_OPTIONS["3x2"]
    elif button_4x4.collidepoint(mouse_pos):
        return GRID_OPTIONS["4x4"]
    elif button_5x4.collidepoint(mouse_pos):
        return GRID_OPTIONS["5x4"]
    elif button_6x6.collidepoint(mouse_pos):
        return GRID_OPTIONS["6x6"]
    return None  # Return None if no button is clicked
