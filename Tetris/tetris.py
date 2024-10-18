import random
from constants import *
from utils import get_light_color

class Tetris:
    def __init__(self):
        self.reset()

    def reset(self):
        """Reset the game state to start a new game."""
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.score = 0
        self.reset_shape()

    def new_shape(self):
        """Generate a new random shape with a random color."""
        shape = random.choice(SHAPES)
        color_name = random.choice(list(COLORS.keys()))
        color = COLORS[color_name]
        light_color = LIGHT_COLORS[color_name]
        return {'shape': shape, 'color': color, 'light_color': light_color}

    def reset_shape(self):
        """Reset the current shape and check for collision."""
        self.current_shape = self.new_shape()
        self.current_pos = [0, GRID_WIDTH // 2 - 1]  # Reset position

        # Check for collision after resetting the shape
        if self.check_collision((0, 0)):
            return True  # Return True to indicate game over
        return False  # No collision, continue game

    def rotate_shape(self):
        """Rotate the current shape."""
        # Correctly rotate the shape while keeping its current color
        self.current_shape['shape'] = [list(row) for row in zip(*self.current_shape['shape'][::-1])]

    def check_collision(self, offset):
        """Check if the shape collides with the walls or filled blocks."""
        for y, row in enumerate(self.current_shape['shape']):
            for x, block in enumerate(row):
                if block:  # Check only if there is a block in the shape
                    grid_x = x + self.current_pos[1] + offset[1]
                    grid_y = y + self.current_pos[0] + offset[0]
                    # Check boundaries and grid collisions
                    if (grid_x < 0 or grid_x >= GRID_WIDTH or
                            grid_y >= GRID_HEIGHT or
                            (grid_y >= 0 and self.grid[grid_y][grid_x])):
                        return True
        return False

    def merge_shape(self):
        """Merge the current shape into the grid."""
        shape, position = self.get_current_shape_status()
        for y, row in enumerate(shape):
            for x, block in enumerate(row):
                if block:
                    # Use the color of the current shape
                    self.grid[y + position[0]][x + position[1]] = self.current_shape['color']

    def clear_lines(self):
        """Clear completed lines and update the score."""
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        for i in lines_to_clear:
            del self.grid[i]
            # Add a new empty row at the top
            self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        self.score += len(lines_to_clear)

    def drop_shape(self):
        """Drop the current shape down by one block."""
        if not self.check_collision((1, 0)):
            self.current_pos[0] += 1  # Move down
        else:
            self.merge_shape()  # Merge the shape if it can't drop
            self.clear_lines()  # Clear completed lines

            if self.reset_shape():  # Check for game over after resetting
                return True  # Indicate game over
        return False  # Continue the game

    def get_current_shape_status(self):
        """Return the current shape and its position."""
        return self.current_shape['shape'], self.current_pos

    def get_score(self):
        """Return the current score."""
        return self.score
