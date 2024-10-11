import pygame

from constants import HEIGHT, WIDTH

def clamp(value, min_value, max_value):
    """Clamp the value between min_value and max_value."""
    return max(min_value, min(value, max_value))

def keep_within_bounds(rect, top_limit, bottom_limit):
    """Keep the item within the specified vertical bounds."""
    rect.top = clamp(rect.top, top_limit, bottom_limit)
    rect.bottom = clamp(rect.bottom, top_limit, bottom_limit)


def draw_gradient_lines(screen):
    """Draws horizontal gradient lines across the screen."""
    for i in range(0, HEIGHT, 2):
        blue_value = min(255, i // 2)  # Max blue value is 255
        color = (0, 0, blue_value)
        pygame.draw.line(screen, color, (0, i), (WIDTH, i))


def draw_transparent_overlay(screen, color=(0, 0, 0, 128)):
    """Draws a semi-transparent overlay on the screen."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # Create a new surface with an alpha channel
    overlay.fill(color)  # Fill it with the desired color (RGBA)
    screen.blit(overlay, (0, 0))  # Draw the overlay on the screen