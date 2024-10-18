import pygame
from tetris import Tetris
from constants import *
from utils import get_light_color

class Game:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.clock = pygame.time.Clock()
        self.tetris = Tetris()

    def draw_grid(self):
        """Draw the game grid on the game_surface."""
        self.game_surface.fill(BLACK)
        pygame.draw.rect(self.game_surface, WHITE, (0, 0, GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE), BORDER_THICKNESS)

        for y in range(len(self.tetris.grid)):
            for x in range(len(self.tetris.grid[y])):
                block_color = self.tetris.grid[y][x]
                if block_color != 0:  # Check for non-empty cells
                    # Draw the grid block
                    pygame.draw.rect(self.game_surface, block_color,
                                     (x * BLOCK_SIZE + 1, y * BLOCK_SIZE + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

                    # Draw the light border for the grid block
                    light_color = get_light_color(block_color)
                    pygame.draw.rect(self.game_surface, light_color,
                                     (x * BLOCK_SIZE + 1, y * BLOCK_SIZE + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2), BORDER_THICKNESS)

    def draw_current_shape(self):
        """Draw the current Tetrimino on the game_surface."""
        shape, position = self.tetris.get_current_shape_status()
        color = self.tetris.current_shape['color']
        light_color = self.tetris.current_shape['light_color']

        for y, row in enumerate(shape):
            for x, block in enumerate(row):
                if block:  # Only draw non-empty blocks
                    pixelx = (x + position[1]) * BLOCK_SIZE
                    pixely = (y + position[0]) * BLOCK_SIZE

                    # Draw the current Tetrimino block on game_surface
                    pygame.draw.rect(self.game_surface, color,
                                     (pixelx, pixely, BLOCK_SIZE, BLOCK_SIZE))

                    # Draw the light border around the Tetrimino block
                    pygame.draw.rect(self.game_surface, light_color,
                                     (pixelx, pixely, BLOCK_SIZE, BLOCK_SIZE), BORDER_THICKNESS)

    def draw_score(self):
        """Draw the score on the main screen (screen)."""
        score_text = M_FONT.render(f'Score: {self.tetris.get_score()}', True, WHITE)
        self.screen.blit(score_text, (GAME_WIDTH + 50, 50))  # Draw the score to the right of the game grid

    def run(self):
        """Main game loop."""
        running = True
        while running:
            self.screen.fill(BLACK)

            if self.tetris.drop_shape():
                print("Game Over!")  # TODO: Handle game over logic
                running = False

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
                        self.tetris.drop_shape()  # TODO: Make the shape drop faster
                    elif event.key == pygame.K_UP:
                        self.tetris.rotate_shape()

            # Draw all game components
            self.draw_grid()
            self.draw_current_shape()

            # Blit game_surface onto screen, positioning the game grid within the larger window
            self.screen.blit(self.game_surface, (20, 20))  # Position the game grid with some margin

            self.draw_score()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
