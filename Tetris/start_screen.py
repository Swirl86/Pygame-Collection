import pygame
from difficulty import Difficulty
from constants import *
from utils import draw_gradient_background


def draw_start_screen(screen, selected_difficulty="Easy"):
    """Draw the start screen with difficulty selection for the game."""
    draw_gradient_background(screen)

    # Title
    title_text = XL_FONT.render("Tetris", True, WHITE)
    title_border = XL_FONT.render("Tetris", True, DARKBLUE)
    border_x = WINDOW_WIDTH // 2 - title_text.get_width() // 2
    border_y = WINDOW_HEIGHT // 4

    screen.blit(title_border, (border_x - 4, border_y - 4))
    screen.blit(title_border, (border_x + 4, border_y - 4))
    screen.blit(title_border, (border_x - 4, border_y + 4))
    screen.blit(title_border, (border_x + 4, border_y + 4))
    screen.blit(title_text, (border_x, border_y))

    # Start Button
    start_text = L_FONT.render("Click to Start", True, WHITE)
    start_button_width = start_text.get_width() + 40
    start_button_height = start_text.get_height() + 40
    start_button_rect = pygame.Rect(
        (WINDOW_WIDTH // 2 - start_button_width // 2, WINDOW_HEIGHT // 2 - 50),
        (start_button_width, start_button_height)
    )

    pygame.draw.rect(screen, DARKBLUE, start_button_rect, border_radius=10)
    pygame.draw.rect(screen, WHITE, start_button_rect, 2, border_radius=10)
    start_text_rect = start_text.get_rect(center=start_button_rect.center)
    screen.blit(start_text, start_text_rect)

    # Difficulty Text
    difficulty_text = M_FONT.render("Difficulty Setting", True, WHITE)
    difficulty_text_rect = difficulty_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
    screen.blit(difficulty_text, difficulty_text_rect)

    difficulty_buttons = draw_difficulty_buttons(screen, selected_difficulty, start_button_rect)

    pygame.display.flip()

    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_click = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the start button is clicked
                if start_button_rect.collidepoint(event.pos):
                    waiting_for_click = False
                # Check for difficulty button clicks
                for button_rect, difficulty in difficulty_buttons:
                    if button_rect.collidepoint(event.pos):
                        selected_difficulty = difficulty
                        difficulty_buttons = draw_difficulty_buttons(screen, selected_difficulty, start_button_rect)

    return selected_difficulty

def draw_difficulty_buttons(screen, selected_difficulty, start_button_rect):
    """Draw difficulty buttons with a green border for the selected one."""
    difficulties = Difficulty.get_names()
    difficulty_buttons = []
    button_width = 120
    button_height = 50
    button_spacing = 15
    total_button_width = len(difficulties) * button_width + (len(difficulties) - 1) * button_spacing

    start_button_center_x = start_button_rect.centerx
    initial_x = start_button_center_x - total_button_width // 2

    for i, difficulty in enumerate(difficulties):
        difficulty_text = M_FONT.render(difficulty, True, WHITE)
        button_rect = pygame.Rect(
            (initial_x + i * (button_width + button_spacing), WINDOW_HEIGHT // 2 + 120),
            (button_width, button_height)
        )
        if selected_difficulty == difficulty:
            pygame.draw.rect(screen, GREEN, button_rect, 3, border_radius=5)
        else:
            pygame.draw.rect(screen, DARKBLUE, button_rect, border_radius=5)
            pygame.draw.rect(screen, WHITE, button_rect, 2, border_radius=5)
        text_rect = difficulty_text.get_rect(center=button_rect.center)
        screen.blit(difficulty_text, text_rect)
        difficulty_buttons.append((button_rect, difficulty))

    pygame.display.flip()
    return difficulty_buttons
