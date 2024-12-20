from constants import *
from game import Game
from start_screen import draw_start_screen


def main():
    """Main function to start the Tetris game."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")

    selected_difficulty = "Easy"
    selected_difficulty = draw_start_screen(screen, selected_difficulty)

    game = Game(screen, selected_difficulty)
    game.run()

if __name__ == "__main__":
    main()
