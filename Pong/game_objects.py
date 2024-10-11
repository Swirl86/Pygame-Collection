import pygame
from constants import *
from utils import keep_within_bounds

class Ball:
    def __init__(self):
        self.rect = BALL_RECT
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y
        self.min_speed = BALL_MIN_SPEED

    def movement(self, player_paddle, opponent_paddle):
        # Update the ball's position based on its speed
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Keep the ball within the screen bounds, considering the scoreboard height
        keep_within_bounds(self.rect, SCOREBOARD_HEIGHT, HEIGHT)

        # Bounce the ball off the top and bottom walls
        if self.rect.top <= SCOREBOARD_HEIGHT or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1  # Reverse the vertical direction

        # Check for collision with player or opponent paddles
        if self.rect.colliderect(player_paddle.rect) or self.rect.colliderect(opponent_paddle.rect):
            # Adjust ball position to prevent it from getting stuck inside the paddle
            if self.rect.colliderect(player_paddle.rect):
                self.rect.right = player_paddle.rect.left  # Move the ball to the left of the player paddle
            elif self.rect.colliderect(opponent_paddle.rect):
                self.rect.left = opponent_paddle.rect.right  # Move the ball to the right of the opponent paddle

            # Reverse the horizontal direction of the ball
            self.speed_x *= -1

            # Ensure that the speed in the X direction does not become too low
            if abs(self.speed_x) < self.min_speed:
                self.speed_x = self.min_speed if self.speed_x > 0 else -self.min_speed

        # Check if the ball goes past the left or right boundaries of the screen
        if self.rect.left <= 0:
            return 'opponent'  # Opponent scores a point
        if self.rect.right >= WIDTH:
            return 'player'    # Player scores a point

        return None  # No score occurred

    def restart(self):
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed_x *= -1  # Change direction after a point

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)  # Draw the ball on the screen

class Paddle:
    def __init__(self, x, y, color):
        self.initial_x = x
        self.initial_y = y
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 0
        self.color = color

    def move(self, speed):
        self.rect.y += speed

        # Prevent the paddle from moving off-screen
        keep_within_bounds(self.rect, SCOREBOARD_HEIGHT, HEIGHT)


    """Reset the paddle's position."""
    def restart(self):
        self.rect.x = self.initial_x
        self.rect.y = self.initial_y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)  # Draw the paddle on the screen
