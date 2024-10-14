import pygame
from game import MemoryGame
from constants import *
from start_screen import draw_start_screen, check_mouse_click

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

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):  # Handle key presses and mouse clicks
                    if event.type == pygame.KEYDOWN:  # Handle key presses for grid size selection
                        grid_selection = {
                            pygame.K_1: GRID_OPTIONS["2x2"],
                            pygame.K_2: GRID_OPTIONS["3x2"],
                            pygame.K_4: GRID_OPTIONS["4x4"],
                            pygame.K_5: GRID_OPTIONS["5x4"],
                            pygame.K_6: GRID_OPTIONS["6x6"]
                        }.get(event.key)  # Get grid size based on pressed key
                    elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse clicks for grid size selection
                        mouse_pos = pygame.mouse.get_pos()
                        grid_selection = check_mouse_click(mouse_pos)  # Check mouse click for grid size

                    # If a valid grid size was selected, update the state
                    if grid_selection:
                        grid_size = grid_selection
                        game_started = True

        else:
            # Create the window with the selected grid size
            window_width = grid_size[0] * (CARD_SIZE + PADDING) - PADDING
            window_height = grid_size[1] * (CARD_SIZE + PADDING) - PADDING
            DISPLAYSURF = pygame.display.set_mode((window_width, window_height))  # Update the window size

            if game is None:  # Initialize the game only once
                game = MemoryGame(grid_size)  # Create the game with the selected grid size

            while game_started:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_started = False
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        card_x = mouse_x // (CARD_SIZE + PADDING)
                        card_y = mouse_y // (CARD_SIZE + PADDING)
                        card_index = card_x + card_y * grid_size[0]

                        if card_index < len(game.cards):
                            game.flip_card(card_index)

                # Draw the game
                DISPLAYSURF.fill(WHITE)  # Clear the screen with a white background
                game.draw(DISPLAYSURF)  # Draw the game state
                game.update()  # Update the game state to manage card visibility
                pygame.display.flip()  # Update the display
                clock.tick(FPS)  # Control the frame rate

    pygame.quit()

if __name__ == '__main__':
    main()
