
from constants import *
from utils import *

class Renderer:
    def __init__(self, screen, game_surface, tetris):
        self.screen = screen
        self.game_surface = game_surface
        self.tetris = tetris

    def draw_grid(self):
        """Draw the game grid on the game_surface."""
        draw_grid_background(self.game_surface)
        pygame.draw.rect(self.game_surface, DARKBLUE, (0, 0, GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE), BORDER_THICKNESS)
        for y in range(len(self.tetris.grid)):
            for x in range(len(self.tetris.grid[y])):
                block_color = self.tetris.grid[y][x]
                if block_color != 0: # Check for non-empty cells
                    # Draw the grid block
                    pygame.draw.rect(self.game_surface, block_color, (x * BLOCK_SIZE + 1, y * BLOCK_SIZE + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2))
                    # Draw the light border for the grid block
                    light_color = get_light_color(block_color)
                    pygame.draw.rect(self.game_surface, light_color, (x * BLOCK_SIZE + 1, y * BLOCK_SIZE + 1, BLOCK_SIZE - 1, BLOCK_SIZE - 2), BORDER_THICKNESS)

    def draw_current_shape(self):
        """Draw the current Tetrimino on the game_surface."""
        shape, position = self.tetris.get_current_shape_status()
        color = self.tetris.current_shape['color']
        light_color = self.tetris.current_shape['light_color']
        for y, row in enumerate(shape):
            for x, block in enumerate(row):
                if block:
                    pixelx = (x + position[1]) * BLOCK_SIZE
                    pixely = (y + position[0]) * BLOCK_SIZE
                     # Draw the current Tetrimino block on game_surface
                    pygame.draw.rect(self.game_surface, color, (pixelx, pixely, BLOCK_SIZE - 2, BLOCK_SIZE - 2))
                    # Draw the light border around the Tetrimino block
                    pygame.draw.rect(self.game_surface, light_color, (pixelx, pixely, BLOCK_SIZE - 2, BLOCK_SIZE - 2), BORDER_THICKNESS)

    def draw_next_shape(self):
        """Draw the next Tetrimino shape on the right side of the game surface."""
        next_shape = self.tetris.get_next_shape_status()
        color = next_shape['color']
        shape = next_shape['shape']
        pygame.draw.rect(self.screen, BLACK, (NEXT_SHAPE_X, NEXT_SHAPE_Y, NEXT_SHAPE_WIDTH + 35, NEXT_SHAPE_HEIGHT + 35))
        pygame.draw.rect(self.screen, DARKBLUE, (NEXT_SHAPE_X, NEXT_SHAPE_Y, NEXT_SHAPE_WIDTH + 35, NEXT_SHAPE_HEIGHT + 35), 2)
        # Calculate the center position for the next shape
        shape_width = len(shape[0]) * BLOCK_SIZE
        shape_height = len(shape) * BLOCK_SIZE
        # Calculate starting position to center the shape
        start_x = NEXT_SHAPE_X + (NEXT_SHAPE_WIDTH + 35 - shape_width) // 2
        start_y = NEXT_SHAPE_Y + (NEXT_SHAPE_HEIGHT + 35 - shape_height) // 2
        for y, row in enumerate(shape):
            for x, block in enumerate(row):
                if block:
                    pixelx = start_x + (x * BLOCK_SIZE)
                    pixely = start_y + (y * BLOCK_SIZE)
                    pygame.draw.rect(self.screen, color, (pixelx, pixely, BLOCK_SIZE - 2, BLOCK_SIZE - 2))
                    light_color = self.tetris.next_shape['light_color']
                    pygame.draw.rect(self.screen, light_color, (pixelx, pixely, BLOCK_SIZE - 2, BLOCK_SIZE - 2), BORDER_THICKNESS)

    def draw_score(self):
        """Draw the score on the main screen (screen)."""
        score_text = L_FONT.render(f'Score: {self.tetris.get_score()}', True, WHITE)
        self.screen.blit(score_text, (GAME_WIDTH + RIGHT_SIDE_MARGIN, 150))

    def draw_game_components(self):
        self.draw_grid()
        self.draw_current_shape()
        self.draw_next_shape()
        self.draw_score()
