import pygame
import sys
from game import Game
from constants import WIDTH, HEIGHT
from start_screen import draw_start_screen

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Create a clock for controlling the game speed
clock = pygame.time.Clock()

# Show start screen
draw_start_screen(screen)

# Create a game instance
game = Game(screen, clock)

# Render the game elements on the screen and introduce a brief pause before the ball begins to move
game.draw_game_elements()
pygame.time.delay(300)

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
