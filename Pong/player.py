from constants import PLAYER_SPEED
from game_objects import Paddle

class Player:
    def __init__(self, x, y, color):
        self.paddle = Paddle(x, y, color)
        self.start_values()

    def start_values(self):
        self.speed = PLAYER_SPEED
        self.score = 0

    def increase_score(self):
            self.score += 1

    def move_paddle(self):
        self.paddle.rect.y += self.speed

    def draw_paddle(self, screen):
        self.paddle.draw(screen)

    def restart(self):
        self.start_values()
        self.paddle.restart()
