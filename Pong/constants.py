import pygame

# Initialize the font module
pygame.font.init()

# Game window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREEN = (0, 128, 0)
RED = (255, 0, 0)    # Player color
GREEN = (0, 255, 0)  # Opponent color

# Dimensions for the scoreboard frame
SCOREBOARD_HEIGHT = 60  # Height of the scoreboard area
SCOREBOARD_PADDING = 10  # Padding inside the scoreboard frame

# Game variables
BALL_SPEED_X = 7 * (-1)  # Initially moves to the left
BALL_SPEED_Y = 7
BALL_RECT = pygame.Rect(WIDTH / 2 - 15, HEIGHT / 2 - 15, 30, 30)
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
FRAME_RECT = pygame.Rect(0, 0, WIDTH, SCOREBOARD_HEIGHT)

# Speed variables
PLAYER_SPEED = 0
OPPONENT_SPEED = 7

# The lower the value, the faster the reaction
REACTION_SPEED = 0.3  # 30% chance of not reacting to the ball

# Fonts variables
XS_FONT = pygame.font.Font(None, 16)
TIMER_FONT = pygame.font.Font(None, 18)
FONT = pygame.font.Font(None, 28)
RESTART_FONT = pygame.font.Font(None, 36)
WINNER_FONT = pygame.font.Font(None, 74)

# Timer variable
TIMER_SECONDS = 300  # 5 minutes
TIMER_FONT = pygame.font.Font(None, 18)

