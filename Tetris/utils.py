import pygame
from constants import *

def draw_gradient_background(screen):
    """Draws a vertical gradient background across the screen."""
    for i in range(WINDOW_HEIGHT):
        # Calculate the color values for the gradient
        green_value = min(128, i * 255 // WINDOW_HEIGHT)  # Interpolate green value
        blue_value = min(128, i * 255 // WINDOW_HEIGHT)   # Interpolate blue value
        color = (0, green_value, blue_value)  # Teal color in RGB

        # Draw a filled rectangle for each row
        pygame.draw.rect(screen, color, (0, i, WINDOW_WIDTH, 1))

def draw_transparent_overlay(screen):
    """Draws a semi-transparent overlay on the screen."""
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    overlay.fill(TRANSPARENT_BLACK)
    screen.blit(overlay, (0, 0))

def draw_grid_background(screen, bg_color = BLACK, grid_color = DARKBLUE):
    """Draw a grid pattern on the background."""
    screen.fill(bg_color)

    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, grid_color, (x, 0), (x, WINDOW_HEIGHT))

    for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, grid_color, (0, y), (WINDOW_WIDTH, y))

def get_light_color(rgb_color):
    for color_name, color_value in COLORS.items():
        if color_value == rgb_color:
            return LIGHT_COLORS[color_name]
    return WHITE

def get_darken_color(color, factor=0.7):
    r, g, b = color
    return (int(r * factor), int(g * factor), int(b * factor))

def calculate_level(lines_cleared):
    return int(lines_cleared / 5)