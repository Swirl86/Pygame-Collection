import pygame
from constants import *
from utils import draw_gradient_background

def draw_winner_screen():
    """Draw the winner screen to display the victory message and restart option."""
    screen = pygame.display.set_mode(INITIAL_SCREEN_SIZE)
    draw_gradient_background(screen)
    text = XL_FONT.render("You Win!", True, BLACK)
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, text_rect)

    restart_text = M_FONT.render("Press R to Restart or Esc to Quit", True, BLACK)
    restart_rect = restart_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
    screen.blit(restart_text, restart_rect)

    pygame.display.flip()

    waiting = True
    while waiting:  # Loop until the user chooses to restart or quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                    return True
                elif event.key == pygame.K_ESCAPE:
                    waiting = False
                    return False
