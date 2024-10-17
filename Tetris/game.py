import pygame
from tetris import Tetris
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.tetris = Tetris()

    def draw_grid(self):
        """Draw the game grid."""
        pygame.draw.rect(self.screen, WHITE, (0, 0, GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE), 2)  # Outer border

        for y in range(len(self.tetris.grid)):
            for x in range(len(self.tetris.grid[y])):
                if self.tetris.grid[y][x] != 0:  # Check for non-empty cells
                    pygame.draw.rect(self.screen, self.tetris.grid[y][x],
                                 (x * BLOCK_SIZE + 1, y * BLOCK_SIZE + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2))
                    pygame.draw.rect(self.screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def draw_current_shape(self):
        """Draw the current Tetrimino shape on the grid."""
        shape, position = self.tetris.get_current_shape_status()
        color = self.tetris.current_shape['color']
        for y, row in enumerate(shape):
            for x, block in enumerate(row):
                if block:  # Only draw non-empty blocks
                    pygame.draw.rect(self.screen, color,
                                    ((x + position[1]) * BLOCK_SIZE,
                                    (y + position[0]) * BLOCK_SIZE,
                                    BLOCK_SIZE, BLOCK_SIZE))

    def draw_score(self):
        """Draw the score on the screen."""
        score_text = M_FONT.render(f'Score: {self.tetris.get_score()}', True, WHITE)
        self.screen.blit(score_text, (10, 10))  # Draw the score at the top-left corner

    def run(self):
        """Main game loop."""
        running = True
        while running:
            self.screen.fill(BLACK)
            self.tetris.drop_shape()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if not self.tetris.check_collision((0, -1)):
                            self.tetris.current_pos[1] -= 1  # Move left
                    elif event.key == pygame.K_RIGHT:
                        if not self.tetris.check_collision((0, 1)):
                            self.tetris.current_pos[1] += 1  # Move right
                    elif event.key == pygame.K_DOWN:
                        self.tetris.drop_shape()  # Move down faster
                    elif event.key == pygame.K_UP:
                        self.tetris.rotate_shape()

            self.draw_grid()
            self.draw_current_shape()
            self.draw_score()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
