import os
import pygame

# Initialize the font module
pygame.font.init()

FPS = 30
EXPLOSION_FPS = 60
SLOWEST_DROP_RATE = 550
FASTEST_DROP_RATE = 50

# Dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 640
BORDER_THICKNESS = 2

GAME_WIDTH, GAME_HEIGHT = 300, 600  # Game Window size
BLOCK_SIZE = 30  # Size of each block
GRID_WIDTH, GRID_HEIGHT = GAME_WIDTH // BLOCK_SIZE, GAME_HEIGHT // BLOCK_SIZE

RIGHT_SIDE_MARGIN = 80

NEXT_SHAPE_WIDTH = BLOCK_SIZE * 6
NEXT_SHAPE_HEIGHT = BLOCK_SIZE * 3
NEXT_SHAPE_X = GAME_WIDTH + RIGHT_SIDE_MARGIN
NEXT_SHAPE_Y = (WINDOW_HEIGHT - NEXT_SHAPE_HEIGHT) // 2

# Fonts variables
XS_FONT = pygame.font.Font(None, 16)
S_FONT = pygame.font.Font(None, 18)
FONT = pygame.font.Font(None, 28)
M_FONT = pygame.font.Font(None, 36)
L_FONT = pygame.font.Font(None, 52)
XL_FONT = pygame.font.Font(None, 74)
ICON_FONT = pygame.font.SysFont("segoeuisymbol", 74)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
DARKBLUE = (30, 60, 100)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)
TRANSPARENT_BLACK = (0, 0, 0, 128)

COLORS = {
    'Cyan': (0, 255, 255),
    'Blue': (0, 0, 255),
    'Orange': (255, 165, 0),
    'Yellow': (255, 255, 0),
    'Green': (0, 255, 0),
    'Purple': (128, 0, 128),
    'Red': (255, 0, 0),
}

LIGHT_COLORS = {
    'Cyan': (173, 216, 230),  # Light Cyan
    'Blue': (173, 216, 230),  # Light Blue
    'Orange': (255, 224, 178), # Light Orange
    'Yellow': (255, 255, 224), # Light Yellow
    'Green': (144, 238, 144),  # Light Green
    'Purple': (230, 190, 255),  # Light Purple
    'Red': (255, 182, 193),      # Light Red
}

# Tetrimino shapes
SHAPES = [
    ( [[1, 1, 1, 1]], 'Cyan' ),  # I shape
    ( [[1, 1], [1, 1]], 'Yellow' ),  # O shape
    ( [[0, 1, 0], [1, 1, 1]], 'Purple' ),  # T shape
    ( [[1, 0, 0], [1, 1, 1]], 'Blue' ),  # L shape
    ( [[0, 0, 1], [1, 1, 1]], 'Red' ),  # J shape
    ( [[1, 1, 0], [0, 1, 1]], 'Green' ),  # S shape
    ( [[0, 1, 1], [1, 1, 0]], 'Orange' ),  # Z shape
]

SOUNDS_DIR = os.path.join(os.path.dirname(__file__), 'sounds')

SOUND_ON_ICON = '\U0001F50A'  # Unicode for speaker
SOUND_OFF_ICON = '\U0001F507'  # Unicode for mute