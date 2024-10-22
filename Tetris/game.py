
import sys
import time
import pygame
from renderer import Renderer
from input_handler import InputHandler
from particle_manager import ParticleManager
from tetris import Tetris
from constants import *
from utils import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.clock = pygame.time.Clock()
        self.tetris = Tetris()
        self.renderer = Renderer(screen, self.game_surface, self.tetris)
        self.input_handler = InputHandler(self.tetris)
        self.particle_manager = ParticleManager(self.game_surface, self.renderer.draw_game_components)
        self.last_drop_time = pygame.time.get_ticks()

    def reset_game(self):
        """Reset the game state to start a new game."""
        self.tetris.reset()
        self.clock = pygame.time.Clock()
        self.last_drop_time = pygame.time.get_ticks()

    def clear_lines(self):
        """Clear completed lines and handle explosion effect."""
        lines_to_clear = self.tetris.get_lines_to_clear()

        for row_index in lines_to_clear:
            self.particle_manager.explode_line(row_index, self.tetris, self.screen, self.clock)

        self.tetris.remove_lines(lines_to_clear)
        self.tetris.score += len(lines_to_clear)

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

    def run(self):
        """Main game loop."""
        game_paused = False

        while True:
            self.current_time = pygame.time.get_ticks()

            # Use fast drop rate if fast dropping is active
            drop_rate = self.tetris.fast_drop_rate if self.tetris.is_fast_dropping else self.tetris.drop_rate

            # Check if it's time to drop the shape
            if self.current_time - self.last_drop_time > drop_rate:
                game_over, lines_to_clear = self.tetris.drop_shape()
                self.last_drop_time = self.current_time

                if game_over:
                    self.game_over()

                if lines_to_clear:
                    self.clear_lines()

            draw_gradient_background(self.screen)
            self.renderer.draw_game_components()

            # Blit game_surface onto screen
            self.screen.blit(self.game_surface, (20, 20))

            pygame.display.flip()
            self.clock.tick(FPS)
            self.checkForQuit()

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    self.input_handler.handle_keyup(event)
                    if event.key == pygame.K_p:
                        game_paused = not game_paused
                        if game_paused:
                            self.draw_paused()
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.tetris.set_fast_drop(False)
                elif event.type == pygame.KEYDOWN:
                    self.input_handler.handle_keydown(event)
            # Handle player input for movement
            keys = pygame.key.get_pressed()
            current_time = time.time()
            self.input_handler.handle_movement(keys, self.tetris.current_pos, current_time)