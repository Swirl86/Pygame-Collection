import time
import pygame

class InputHandler:
    def __init__(self, tetris):
        self.tetris = tetris
        self.last_side_move = time.time()

    def handle_keydown(self, event):
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.tetris.set_fast_drop(True)
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.tetris.rotate_shape()

    def handle_keyup(self, event):
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.tetris.set_fast_drop(False)

    def handle_movement(self, keys, current_pos, current_time, side_move_delay=0.1):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and current_time - self.last_side_move > side_move_delay:
            if not self.tetris.check_collision((0, -1)):
                current_pos[1] -= 1  # Move left
            self.last_side_move = time.time()
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and current_time - self.last_side_move > side_move_delay:
            if not self.tetris.check_collision((0, 1)):
                current_pos[1] += 1  # Move right
            self.last_side_move = time.time()
