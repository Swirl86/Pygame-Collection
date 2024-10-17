import pygame

# Initialize the font module
pygame.font.init()

FPS = 30

# Dimensions
INITIAL_SCREEN_SIZE = (600, 500)
CARD_SIZE = 100
GRID_OPTIONS = {
    "2x2": (2, 2),  # 4 cards total, 2 unique pairs
    "3x2": (3, 2),  # 6 cards total, 3 unique pairs
    "4x4": (4, 4),  # 16 cards total, 8 unique pairs
    "5x4": (5, 4),  # 20 cards total, 10 unique pairs
    "6x6": (6, 6),  # 36 cards total, 18 unique pairs
}
MIN_GRID_SIZE = (3, 2)
PADDING = 10
TOP_INFO_TEXT_HEIGHT = 30
BOTTOM_INFO_TEXT_HEIGHT = 50
BORDER_WIDTH = 5

# Define the button dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40

# Define the button positions
option_2x2_pos = (100, 200)  # Position for 2x2 button
option_3x2_pos = (310, 200)  # Position for 3x2 button
option_4x4_pos = (200, 250)  # Position for 4x4 button
option_5x4_pos = (100, 300)  # Position for 5x4 button
option_6x6_pos = (310, 300)  # Position for 6x6 button

# Define button rectangles
button_2x2 = pygame.Rect(option_2x2_pos[0], option_2x2_pos[1], 200, 40)
button_3x2 = pygame.Rect(option_3x2_pos[0], option_3x2_pos[1], 200, 40)
button_4x4 = pygame.Rect(option_4x4_pos[0], option_4x4_pos[1], 200, 40)
button_5x4 = pygame.Rect(option_5x4_pos[0], option_5x4_pos[1], 200, 40)
button_6x6 = pygame.Rect(option_6x6_pos[0], option_6x6_pos[1], 200, 40)

# Fonts variables
XS_FONT = pygame.font.Font(None, 16)
S_FONT = pygame.font.Font(None, 18)
FONT = pygame.font.Font(None, 28)
M_FONT = pygame.font.Font(None, 36)
L_FONT = pygame.font.Font(None, 52)
XL_FONT = pygame.font.Font(None, 74)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
ORANGE = (255, 165, 0)
BLUE = (70, 130, 180)
DARKBLUE = (30, 60, 100)

DONUT_COLOR = (255, 200, 200)  # Donut color
SQUARE_COLOR = (200, 255, 200)  # Square color
DIAMOND_COLOR = (200, 200, 255)  # Diamond color
LINE_COLOR = (255, 255, 100)  # Line color
OVAL_COLOR = (255, 100, 255)  # Oval color

# Icon types
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

# Numbers and symbols
NUMBERS = [str(i) for i in range(10)]
SYMBOLS = ['+', '-', '=', '?', '&', '%', '#', 'A', 'B', 'C']

ICONS = ([DONUT, SQUARE, DIAMOND, LINES, OVAL]  + NUMBERS + SYMBOLS)