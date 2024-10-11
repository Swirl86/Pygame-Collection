import pygame
import sys
from game_logic import Game  # Ensure Game class is implemented properly
from constants import *      # Ensure constants are defined correctly

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Create a clock for controlling the game speed
clock = pygame.time.Clock()

# Create a game instance
game = Game(screen, clock)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        game.handle_event(event)

    game.update_game_state()

    game.draw_game_elements()

    # Control the game speed (frames per second)
    clock.tick(60)  # Limit to 60 frames per second

    # Refresh the screen
    pygame.display.flip()
