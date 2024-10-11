from constants import MAX_SCORE, TIMER_SECONDS
import winner_texts

class GameLogic:
    def __init__(self):
        self.winner_text = ""
        self.game_over = False
        self.timer_seconds = TIMER_SECONDS

    def reset_values(self):
        """Reset the game state to initial values."""
        self.winner_text = ""
        self.game_over = False
        self.timer_seconds = TIMER_SECONDS

    def check_game_timer(self):
        if self.timer_seconds > 0:
            self.timer_seconds -= 1 / 60  # Decrease timer by 1 second (at 60 FPS)
        else:
            self.game_over = True

    def check_for_winner(self, player_score, opponent_score):
        if player_score == MAX_SCORE:
            self.game_over = True
            self.winner_text = winner_texts.player_wins
        elif opponent_score == MAX_SCORE:
            self.game_over = True
            self.winner_text = winner_texts.opponent_wins
        elif self.timer_seconds <= 0:  # Check if the time has run out
            self.game_over = True
            self.winner_text = winner_texts.tie
