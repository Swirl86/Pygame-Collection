
import pygame
from constants import *
from utils import draw_gradient_background


def draw_start_screen(screen):
    """Draw the start screen for the game."""
    draw_gradient_background(screen)

    title_text = XL_FONT.render("Tetris", True, WHITE)
    title_border = XL_FONT.render("Tetris", True, DARKBLUE)

    border_x = WINDOW_WIDTH // 2 - title_text.get_width() // 2
    border_y = WINDOW_HEIGHT // 4

    screen.blit(title_border, (border_x - 4, border_y - 4))
    screen.blit(title_border, (border_x + 4, border_y - 4))
    screen.blit(title_border, (border_x - 4, border_y + 4))
    screen.blit(title_border, (border_x + 4, border_y + 4))

    screen.blit(title_text, (border_x, border_y))

    start_text = L_FONT.render("Click to Start", True, WHITE)

    start_button_width = start_text.get_width() + 40
    start_button_height = start_text.get_height() + 40
    start_button_rect = pygame.Rect(
        (WINDOW_WIDTH // 2 - start_button_width // 2, WINDOW_HEIGHT // 2),
        (start_button_width, start_button_height)
    )

    pygame.draw.rect(screen, DARKBLUE, start_button_rect, border_radius=10)
    pygame.draw.rect(screen, WHITE, start_button_rect, 2, border_radius=10)

    start_text_rect = start_text.get_rect(center=start_button_rect.center)
    screen.blit(start_text, start_text_rect)

    pygame.display.flip()

    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_click = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    waiting_for_click = False