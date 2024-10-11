import pygame
from constants import *
from game_objects import Ball
from opponent import Opponent
from player import Player
from utils import keep_within_bounds
from winner_texts import winner_texts

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.ball = Ball()

        # Create paddles with initial position and color
        self.player = Player(WIDTH - 20, HEIGHT / 2 - 70, RED)
        self.opponent = Opponent(10, HEIGHT / 2 - 70, GREEN)

        self.start_game_values()

    def start_game_values(self):
        """Initialize or reset the game state."""
        self.winner_text = ""
        self.game_over = False
        self.timer_seconds = TIMER_SECONDS

        self.reset_positions()

    def reset_positions(self):
        """Reset the positions of the ball and paddles."""
        self.ball.restart()
        self.player.restart()
        self.opponent.restart()

    def reset_game(self):
        """Reset the game state and positions for a new game."""
        self.start_game_values()

    def draw_game_elements(self):
        """Clear the screen and draw everything"""
        self.screen.fill(BLACK)
        self.draw_scoreboard_frame()
        self.draw_midline()
        self.display_score()
        self.ball.draw(self.screen)
        self.player.draw_paddle(self.screen)
        self.opponent.draw_paddle(self.screen)

        if self.game_over:
            self.display_winner()

        pygame.display.flip()

    def draw_scoreboard_frame(self):
        pygame.draw.rect(self.screen, WHITE, FRAME_RECT, 2)

    def draw_midline(self):
        mid_x = WIDTH // 2  # Calculate the x position for the middle line
        pygame.draw.line(self.screen, WHITE, (mid_x, SCOREBOARD_HEIGHT), (mid_x, HEIGHT), 2)

    def display_score(self):
        player_text = FONT.render(f"{self.player.score}", True, WHITE)
        opponent_text = FONT.render(f"{self.opponent.score}", True, WHITE)
        pong_text = FONT.render("PYGAME PONG", True, WHITE)
        timer_text = TIMER_FONT.render(f"Time: {int(self.timer_seconds) // 60}:{int(self.timer_seconds) % 60:02d}", True, WHITE)
        fps_text = XS_FONT.render(f"FPS:  {int(self.clock.get_fps())}", True, WHITE)

        """Display positions for the scores and title"""
        self.screen.blit(player_text, (WIDTH - 100, 20))  # Player score (right)
        self.screen.blit(opponent_text, (100, 20))  # Opponent score (left)
        self.screen.blit(pong_text, (WIDTH // 2 - pong_text.get_width() // 2, 10))  # Title in the center
        self.screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 40))  # Timer below the title
        self.screen.blit(fps_text, (10, 10))  # Draw FPS text at the top-left corner

    def display_winner(self):
        text = WINNER_FONT.render(self.winner_text, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))  # Center the text
        self.screen.blit(text, text_rect)

        restart_text = RESTART_FONT.render("Click to Restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))  # Center the button text
        self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()  # Update the display

        waiting_for_click = True
        while waiting_for_click:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
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

    def check_game_timer(self):
        if self.timer_seconds > 0:
            self.timer_seconds -= 1 / 60  # Decrease timer by 1 second (at 60 FPS)
        else:
            self.check_for_winner()  # Check for winner when time runs out

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
            self.check_for_winner()

        self.opponent.move_paddle(self.ball)

        self.check_game_timer()

    def check_for_winner(self):
        if self.player.score == 11:
            self.game_over = True
            self.winner_text = winner_texts.player_wins
        elif self.opponent.score == 11:
            self.game_over = True
            self.winner_text = winner_texts.opponent_wins
        elif self.timer_seconds <= 0:  # Check if the time has run out
            self.game_over = True
            self.winner_text = winner_texts.tie
