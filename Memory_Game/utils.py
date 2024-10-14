import pygame
from constants import INITIAL_SCREEN_SIZE


def draw_gradient_background(screen):
    """Draws a vertical gradient background across the screen."""
    for i in range(INITIAL_SCREEN_SIZE[1]):
        # Calculate the color values for the gradient
        green_value = min(128, i * 255 // INITIAL_SCREEN_SIZE[1])  # Interpolate green value
        blue_value = min(128, i * 255 // INITIAL_SCREEN_SIZE[1])   # Interpolate blue value
        color = (0, green_value, blue_value)  # Teal color in RGB
        
        # Draw a filled rectangle for each row
        pygame.draw.rect(screen, color, (0, i, INITIAL_SCREEN_SIZE[0], 1))


def draw_transparent_overlay(screen, color=(0, 0, 0, 128)):
    """Draws a semi-transparent overlay on the screen."""
    overlay = pygame.Surface((INITIAL_SCREEN_SIZE[0], INITIAL_SCREEN_SIZE[1]), pygame.SRCALPHA)  # Create a new surface with an alpha channel
    overlay.fill(color)  # Fill it with the desired color (RGBA)
    screen.blit(overlay, (0, 0))  # Draw the overlay on the screen