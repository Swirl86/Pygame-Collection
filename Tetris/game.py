import random
import sys
import pygame
from particle import Particle
from tetris import Tetris
from constants import *
from utils import *

class Game:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.clock = pygame.time.Clock()
        self.tetris = Tetris()


    def reset_game(self):
        """Reset the game state to start a new game."""
        self.tetris.reset()
        self.clock = pygame.time.Clock()

    def draw_grid(self):
        """Draw the game grid on the game_surface."""
        draw_grid_background(self.game_surface)
        pygame.draw.rect(self.game_surface, DARKBLUE, (0, 0, GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE), BORDER_THICKNESS)

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
                                     (x * BLOCK_SIZE + 1, y * BLOCK_SIZE + 1, BLOCK_SIZE - 1, BLOCK_SIZE - 2), BORDER_THICKNESS)

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
                                    (pixelx, pixely, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

                    # Draw the light border around the Tetrimino block
                    pygame.draw.rect(self.game_surface, light_color,
                                    (pixelx, pixely, BLOCK_SIZE - 2, BLOCK_SIZE - 2), BORDER_THICKNESS)

    def draw_next_shape(self):
        """Draw the next Tetrimino shape on the right side of the game surface."""
        next_shape = self.tetris.get_next_shape_status()
        color = next_shape['color']
        shape = next_shape['shape']

        pygame.draw.rect(self.screen, BLACK, (NEXT_SHAPE_X, NEXT_SHAPE_Y, NEXT_SHAPE_WIDTH + 35, NEXT_SHAPE_HEIGHT + 35))
        pygame.draw.rect(self.screen, DARKBLUE, (NEXT_SHAPE_X, NEXT_SHAPE_Y, NEXT_SHAPE_WIDTH + 35, NEXT_SHAPE_HEIGHT + 35), 2)  # Border

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


    def clear_lines(self):
        """Clear completed lines and handle explosion effect."""
        lines_to_clear = self.tetris.get_lines_to_clear()

        for row_index in lines_to_clear:
            self.explode_line(row_index)

        self.tetris.remove_lines(lines_to_clear)
        self.tetris.score += len(lines_to_clear)

    def explode_line(self, row_index):
        """Create a simple explosion effect on the cleared row."""
        particles = self.get_particles(row_index)
        explosion_duration = 300
        explosion_start_time = pygame.time.get_ticks()

        while pygame.time.get_ticks() - explosion_start_time < explosion_duration:
            self.draw_game_components() # Redraw game components behind the explosion
            # Update and draw all particles
            for particle in particles:
                particle.update()
                particle.draw(self.game_surface)

            # Blit the game surface to the main screen and update display
            self.screen.blit(self.game_surface, (20, 20))
            pygame.display.flip()
            self.clock.tick(EXPLOSION_FPS)
            # Remove dead particles
            particles = [p for p in particles if p.is_alive()]

    def get_particles(self, row_index):
        particles = []
        for x in range(GRID_WIDTH):
            block_color = self.tetris.grid[row_index][x]
            if block_color != 0:
                dark_color = get_darken_color(block_color)
                for _ in range(random.randint(2, 10)):  # Create multiple particles per block
                    particle_x = (x * BLOCK_SIZE) + random.randint(-BLOCK_SIZE // 2, BLOCK_SIZE // 2)
                    particle_y = (row_index * BLOCK_SIZE) + random.randint(-BLOCK_SIZE // 2, BLOCK_SIZE // 2)
                    radius = random.randint(2, 6)
                    particles.append(Particle(particle_x, particle_y, dark_color, radius))
        return particles

    def draw_paused(self):
        draw_transparent_overlay(self.screen)
        text = XL_FONT.render("PAUSED", True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        self.screen.blit(text, text_rect)

        pygame.display.flip()

        waiting_for_click = True
        while waiting_for_click:
            self.checkForQuit()
            for _ in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP]):
                waiting_for_click = False


    def game_over(self):
        draw_transparent_overlay(self.screen)

        # Render the winner text and position it in the center
        text = XL_FONT.render("GAME OVER", True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        self.screen.blit(text, text_rect)

        border_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        border_rect.inflate_ip(20, 20)
        pygame.draw.rect(self.screen, WHITE, border_rect, 3)

        restart_text = M_FONT.render("Click to Restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()

        waiting_for_click = True
        while waiting_for_click:
            self.checkForQuit()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rect.collidepoint(event.pos):
                        waiting_for_click = False  # Exit the loop to reset the game

        self.reset_game()

    def terminate(_):
        pygame.quit()
        sys.exit()

    def checkForQuit(self):
        """Check for quit or escape key and handle game termination."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.terminate()
            pygame.event.post(event)


    def draw_game_components(self):
        self.draw_grid()
        self.draw_current_shape()
        self.draw_next_shape()
        self.draw_score()

    def run(self):
        """Main game loop."""
        game_paused = False
        while True:
            game_over, lines_to_clear = self.tetris.drop_shape()
            if game_over:
                self.game_over()

            draw_gradient_background(self.screen)
            self.draw_game_components()

            if lines_to_clear:
                self.clear_lines()

            # Blit game_surface onto screen, positioning the game grid within the larger window
            self.screen.blit(self.game_surface, (20, 20))  # Position the game grid with some margin

            pygame.display.flip()
            self.clock.tick(FPS)
            self.checkForQuit()

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        game_paused = not game_paused
                        if game_paused:
                            self.draw_paused()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if not self.tetris.check_collision((0, -1)):
                            self.tetris.current_pos[1] -= 1  # Move left
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if not self.tetris.check_collision((0, 1)):
                            self.tetris.current_pos[1] += 1  # Move right
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.tetris.drop_shape()  # TODO IMPL Make the shape drop faster
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.tetris.rotate_shape()
