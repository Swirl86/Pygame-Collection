import pygame
from constants import *
from utils import draw_gradient_background

def draw_start_screen(screen):
    """Draw the start screen for the game."""
    draw_gradient_background(screen)
    title_text = FONT.render("Choose Grid Size", True, WHITE)
    screen.blit(title_text, (100, 100))

    button_positions = [
        (option_2x2_pos, "2x2"),
        (option_3x2_pos, "3x2"),
        (option_4x4_pos, "4x4"),
        (option_5x4_pos, "5x4"),
        (option_6x6_pos, "6x6"),
    ]

    # Loop through button positions to render buttons and borders
    for index, (pos, label) in enumerate(button_positions):
        # Calculate x and y position for buttons
        x = pos[0]
        y = pos[1]

        # Draw button rectangle with border
        button_rect = pygame.Rect(x, y, 200, 40)
        pygame.draw.rect(screen, WHITE, button_rect, 2)

        # Render button label
        button_text = FONT.render(f"{index + 1}.   {label}", True, WHITE)
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)

    pygame.display.flip()
