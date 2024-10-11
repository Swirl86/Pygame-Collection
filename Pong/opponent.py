import random
from constants import *
from game_objects import Paddle
from utils import keep_within_bounds

class Opponent:
    def __init__(self, x, y, color):
        self.paddle = Paddle(x, y, color)
        self.start_values()

    def start_values(self):
        self.speed = OPPONENT_SPEED
        self.score = 0

    def increase_score(self):
            self.score += 1

    def move_paddle(self, ball):
        """Simple function to move the opponent paddle"""
        ai_reaction = random.random()

        if ai_reaction < REACTION_SPEED:
            return  # The opponent misses the ball

        # Move the opponent paddle only when the ball is on the opponent's side
        if ball.speed_x < 0:  # Ball is moving towards the opponent
            if ball.rect.centery < self.paddle.rect.centery:
                self.paddle.move(-self.speed)  # Move up
            elif ball.rect.centery > self.paddle.rect.centery:
                self.paddle.move(self.speed)  # Move down

        # Prevent opponent from moving out of the screen
        keep_within_bounds(self.paddle.rect, SCOREBOARD_HEIGHT, HEIGHT)

    def draw_paddle(self, screen):
        self.paddle.draw(screen)

    def restart(self):
        self.start_values()
        self.paddle.restart()