import pygame
from constants import *

class Card:
    def __init__(self, icon):
        self.icon = icon  # Icon type (e.g., DONUT, SQUARE)
        self.is_flipped = False
        self.is_matched = False

    def draw(self, screen, x, y, border_color=BLACK):
        """Draw the card on the screen at the specified position."""
        if self.is_flipped:
            # Draw the icon based on the type
            if self.icon == 'donut':
                self.draw_icon(screen, DONUT_COLOR, x, y)
            elif self.icon == 'square':
                self.draw_icon(screen, SQUARE_COLOR, x, y)
            elif self.icon == 'diamond':
                self.draw_icon(screen, DIAMOND_COLOR, x, y)
            elif self.icon == 'lines':
                self.draw_icon(screen, LINE_COLOR, x, y)
            elif self.icon == 'oval':
                self.draw_icon(screen, OVAL_COLOR, x, y)
            # Check if icon is a number or symbol
            elif self.icon in NUMBERS or self.icon in SYMBOLS:
                self.draw_text(screen, x, y)
        else:
            pygame.draw.rect(screen, (0, 0, 0), (x, y, CARD_SIZE, CARD_SIZE))

        pygame.draw.rect(screen, border_color, (x, y, CARD_SIZE, CARD_SIZE), BORDER_WIDTH)

    def draw_icon(self, screen, color, x, y):
        """Draw the icon on the card (for shapes)."""
        quarter = int(CARD_SIZE * 0.25)
        half = int(CARD_SIZE * 0.5)

        if self.icon == 'donut':
            pygame.draw.circle(screen, color, (x + half, y + half), half - 5)
            pygame.draw.circle(screen, (255, 255, 255), (x + half, y + half), quarter - 5)
        elif self.icon == 'square':
            pygame.draw.rect(screen, color, (x + quarter, y + quarter, CARD_SIZE - half, CARD_SIZE - half))
        elif self.icon == 'diamond':
            pygame.draw.polygon(screen, color, (
                (x + half, y),
                (x + CARD_SIZE - 1, y + half),
                (x + half, y + CARD_SIZE - 1),
                (x, y + half),
            ))
        elif self.icon == 'lines':
            for i in range(0, CARD_SIZE, 4):
                pygame.draw.line(screen, color, (x, y + i), (x + i, y))
                pygame.draw.line(screen, color, (x + i, y + CARD_SIZE - 1), (x + CARD_SIZE - 1, y + i))
        elif self.icon == 'oval':
            pygame.draw.ellipse(screen, color, (x, y + quarter, CARD_SIZE, half))

    def draw_text(self, screen, x, y):
        """Draw numbers or symbols as text on the card."""
        font = pygame.font.Font(None, 72)  # Font size 72 (adjust as needed)
        text_color = (0, 0, 0)  # Black text color (adjust for visibility)
        text_surface = font.render(self.icon, True, text_color)
        text_rect = text_surface.get_rect(center=(x + CARD_SIZE // 2, y + CARD_SIZE // 2))
        screen.blit(text_surface, text_rect)