import pygame

# Initialize the font module
pygame.font.init()

FPS = 10

# Dimensions
WIDTH, HEIGHT = 300, 600  # Window size
BLOCK_SIZE = 30  # Size of each block
GRID_WIDTH, GRID_HEIGHT = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

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
BLUE = (70, 130, 180)
DARKBLUE = (30, 60, 100)

COLORS = [
    (255, 0, 0),   # Red
    (0, 255, 0),   # Green
    (0, 0, 255),   # Blue
    (255, 255, 0), # Yellow
    (255, 165, 0), # Orange
    (75, 0, 130),  # Indigo
    (238, 130, 238) # Violet
]

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]