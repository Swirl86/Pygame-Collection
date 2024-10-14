import pygame
from constants import *

def handle_start_selection_events(running):
    """Handle events for selecting grid size at the start of the game."""
    grid_selection = None

    while True:  # Loop until the user selects a grid size or quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set running to False if quitting
                return None, running  # Return None for grid size and the updated running state
            elif event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                if event.type == pygame.KEYDOWN:
                    grid_selection = {
                        pygame.K_1: GRID_OPTIONS["2x2"],
                        pygame.K_2: GRID_OPTIONS["3x2"],
                        pygame.K_4: GRID_OPTIONS["4x4"],
                        pygame.K_5: GRID_OPTIONS["5x4"],
                        pygame.K_6: GRID_OPTIONS["6x6"]
                    }.get(event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    grid_selection = check_mouse_click(mouse_pos)

                # If a valid grid size was selected return grid size and running state
                if grid_selection:
                    return grid_selection, running


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
