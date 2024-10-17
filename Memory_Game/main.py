import pygame
from event_handler import handle_start_selection_events
from game import MemoryGame
from constants import *
from start_screen import draw_start_screen
from winner_screen import draw_winner_screen

pygame.init()

# Define the initial display size for the menu
DISPLAYSURF = pygame.display.set_mode(INITIAL_SCREEN_SIZE)
pygame.display.set_caption('Memory Game')

def main():
    global DISPLAYSURF  # Make DISPLAYSURF global to modify it later
    clock = pygame.time.Clock()
    running = True
    game_started = False
    grid_size = None
    game = None

    # Main loop
    while running:
        if not game_started:
            draw_start_screen(DISPLAYSURF)

            grid_size, running = handle_start_selection_events(running)
            if grid_size:  # Ensure a valid grid size was selected
                game_started = True  # Set game_started to True if a grid size was chosen

        else:
            window_grid_size = list(grid_size)

            if window_grid_size[0] < MIN_GRID_SIZE[0]:
                window_grid_size[0] = MIN_GRID_SIZE[0]
            if window_grid_size[1] < MIN_GRID_SIZE[1]:
                window_grid_size[1] = MIN_GRID_SIZE[1]

            window_width = (CARD_SIZE + PADDING) * window_grid_size[0] + PADDING
            window_height = (CARD_SIZE + PADDING) * window_grid_size[1] + PADDING + BOTTOM_INFO_TEXT_HEIGHT
            DISPLAYSURF = pygame.display.set_mode((window_width, window_height))

            if game is not None:
                game.grid_size = grid_size
                game.reset_game()
            else:
                game = MemoryGame(grid_size)

            while game_started:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_started = False
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:  # Press 'R' to reset the game
                            game.reset_game()
                        elif event.key == pygame.K_ESCAPE:  # Press 'Esc' to go back to the start screen
                            grid_size = None
                            game_started = False
                            game = None  # Reset the game instance
                            DISPLAYSURF = pygame.display.set_mode(INITIAL_SCREEN_SIZE)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        card_x = mouse_x // (CARD_SIZE + PADDING)
                        card_y = mouse_y // (CARD_SIZE + PADDING)
                        card_index = card_x + card_y * grid_size[0]

                        if card_index < len(game.cards):
                            game.flip_card(card_index)

                # Draw the game
                DISPLAYSURF.fill(GRAY)  # Clear the screen

                if game is not None:  # Ensure the game instance is initialized
                    game.draw(DISPLAYSURF)  # Draw the game state
                    game.update_game_timer()

                if game and game.update():  # Update the game state to manage card visibility
                    if not draw_winner_screen(game.elapsed_time, game.moves):  # Check if the player chooses to quit
                        running = False  # Quit the game
                    game.reset_game()
                    grid_size = None
                    game_started = False  # Reset grid_size and game_started to allow for grid size selection

                pygame.display.flip()
                clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
