import sys
import pygame
from constants import *
from game_logic import GameLogic
from game_objects import Ball
from opponent import Opponent
from player import Player
from utils import *

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.logic = GameLogic()
        self.ball = Ball()

        # Create paddles with initial position and color
        self.player = Player(WIDTH - 20, HEIGHT / 2 - 70, RED)
        self.opponent = Opponent(10, HEIGHT / 2 - 70, GREEN)

        self.start_positions()

    def start_positions(self):
        """Reset the positions of the ball and paddles."""
        self.ball.restart()
        self.player.restart()
        self.opponent.restart()

    def reset_game(self):
        """Reset the game state and positions for a new game."""
        self.logic.reset_values()
        self.start_positions()

    def draw_game_elements(self):
        """Clear the screen and draw everything"""
        self.screen.fill(BLACK)
        self.draw_scoreboard_frame()
        self.draw_midline()
        self.display_score()
        self.ball.draw(self.screen)
        self.player.draw_paddle(self.screen)
        self.opponent.draw_paddle(self.screen)

        if self.logic.game_over:
            self.display_winner()

        pygame.display.flip()

    def draw_scoreboard_frame(self):
        pygame.draw.rect(self.screen, WHITE, FRAME_RECT, 2)

    def draw_midline(self):
        mid_x = WIDTH // 2  # Calculate the x position for the middle line
        line_length = 10  # Length of each dash
        space_length = 5  # Space between dashes
        y_start = SCOREBOARD_HEIGHT  # Starting y position of the line
        y_end = HEIGHT  # Ending y position of the line

        for y in range(y_start, y_end, line_length + space_length):
            pygame.draw.line(self.screen, WHITE, (mid_x, y), (mid_x, y + line_length), 2)

    def display_score(self):
        player_text = FONT.render(f"{self.player.score}", True, WHITE)
        opponent_text = FONT.render(f"{self.opponent.score}", True, WHITE)
        pong_text = FONT.render("PYGAME PONG", True, WHITE)
        timer_text = S_FONT.render(f"Time: {int(self.logic.timer_seconds) // 60}:{int(self.logic.timer_seconds) % 60:02d}", True, WHITE)
        fps_text = XS_FONT.render(f"FPS:  {int(self.clock.get_fps())}", True, WHITE)

        """Display positions for the scores and title"""
        self.screen.blit(player_text, (WIDTH - 100, 20))  # Player score (right)
        self.screen.blit(opponent_text, (100, 20))  # Opponent score (left)
        self.screen.blit(pong_text, (WIDTH // 2 - pong_text.get_width() // 2, 10))  # Title in the center
        self.screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 40))  # Timer below the title
        self.screen.blit(fps_text, (10, 10))  # Draw FPS text at the top-left corner

    def display_winner(self):
        # Draw the background
        draw_transparent_overlay(self.screen)
        draw_gradient_lines(self.screen)

        # Render the winner text and position it in the center
        text = PIXEL_FONT.render(self.logic.winner_text, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))  # Center the text
        self.screen.blit(text, text_rect)

        # Create a border for the winner text
        border_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        border_rect.inflate_ip(20, 20)  # Add some padding to the border
        pygame.draw.rect(self.screen, WHITE, border_rect, 3)  # Draw the border

        # Render and position the restart text
        restart_text = M_FONT.render("Click to Restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))  # Center the button text
        self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()  # Update the display

        waiting_for_click = True
        while waiting_for_click:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Exit the game if the window is closed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rect.collidepoint(event.pos):
                        waiting_for_click = False  # Exit the loop to reset the game

        self.reset_game()

    def handle_event(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.speed = -7  # Set speed for upward movement
                if event.key == pygame.K_DOWN:
                    self.player.speed = 7    # Set speed for downward movement
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.player.speed = 0    # Stop the paddle when key is released

    def update_game_state(self):
            """Move the player paddle based on speed"""
            self.player.move_paddle()

            # Prevent the player paddle from moving off-screen and inside the scoreboard
            keep_within_bounds(self.player.paddle.rect, SCOREBOARD_HEIGHT, HEIGHT)

            # Handle ball movement and check for collisions or scoring events
            scored = self.ball.movement(self.player.paddle, self.opponent.paddle)

            # Check if the ball scored and update the winner if needed
            if scored:
                if scored == 'player':
                    self.opponent.increase_score()
                elif scored == 'opponent':
                    self.player.increase_score()
                self.ball.restart()  # Reset ball position after scoring
                self.logic.check_for_winner(self.player.score, self.opponent.score)

            self.opponent.move_paddle(self.ball)

            self.logic.check_game_timer()
