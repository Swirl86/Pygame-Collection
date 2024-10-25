import pygame
import subprocess
import sys

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOR = (100, 100, 255)
TITLE_COLOR = (255, 69, 0)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Collection")

title_font = pygame.font.SysFont('arial', 65, bold=True)
menu_font = pygame.font.SysFont('arial', 40)

games = {
    "Memory Game": ("Memory_Game/main.py", (WINDOW_WIDTH // 2, 200)),
    "Pong": ("Pong/main.py", (WINDOW_WIDTH // 2, 300)),
    "Tetris": ("Tetris/main.py", (WINDOW_WIDTH // 2, 400)),
}

# Title rendering
title_text = title_font.render("PYGAME COLLECTION", True, TITLE_COLOR)
title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 100))

# Underline settings
underline_y = title_rect.bottom + 10  # Adjust distance from title to underline
underline_thickness = 5  # Thickness of underline

running = True
while running:
    screen.fill(BLACK)

    screen.blit(title_text, title_rect)
    pygame.draw.line(screen, TITLE_COLOR,
                     (title_rect.left, underline_y),
                     (title_rect.right, underline_y),
                     underline_thickness)

    mouse_pos = pygame.mouse.get_pos()
    for game_name, (path, pos) in games.items():
        # Check if the mouse is over the game name for hover effect
        color = HOVER_COLOR if pygame.Rect(menu_font.render(game_name, True, WHITE).get_rect(center=pos)).collidepoint(mouse_pos) else WHITE
        text_surface = menu_font.render(game_name, True, color)
        text_rect = text_surface.get_rect(center=pos)
        screen.blit(text_surface, text_rect)

        if pygame.mouse.get_pressed()[0] and text_rect.collidepoint(mouse_pos):
            subprocess.Popen(["python", path])
            pygame.time.delay(300)  # Small delay to prevent multiple clicks

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
