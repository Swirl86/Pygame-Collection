import pygame
import sys
from constants import *

def draw_start_screen(screen):
    for i in range(0, HEIGHT, 2):
        # Ensure the RGB values are within valid range (0-255)
        blue_value = min(255, i // 2)  # Max blue value is 255
        color = (0, 0, blue_value)  # RGB tuple
        pygame.draw.line(screen, color, (0, i), (WIDTH, i))

    # Render the title text
    title_text = XL_FONT.render("PYGAME PONG", True, WHITE)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(title_text, title_rect)

    # Render the start text
    start_text = L_FONT.render("Click to Start", True, WHITE)
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(start_text, start_rect)

    pygame.draw.rect(screen, WHITE, title_rect.inflate(20, 20), 2)  # Draw border around title

    pygame.display.flip()

    # Wait for the user's click to start the game
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    waiting_for_click = False  # Start the game
