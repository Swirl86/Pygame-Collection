import random
from constants import *

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
        self.current_shape = self.next_shape if hasattr(self, 'next_shape') else self.new_shape()
        self.current_pos = [0, GRID_WIDTH // 2 - 1]  # Reset position
        self.next_shape = self.new_shape()  # Generate the next shape

        if self.check_collision((0, 0)):
            return True  # Return True to indicate game over
        return False  # No collision, continue game

    def rotate_shape(self):
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

    def get_lines_to_clear(self):
        """Return a list of completed lines that should be cleared."""
        return [i for i, row in enumerate(self.grid) if all(row)]

    def remove_lines(self, lines_to_clear):
        """Remove the lines from the grid after the explosion effect."""
        for i in lines_to_clear:
            del self.grid[i]
            # Add a new empty row at the top
            self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])

    def drop_shape(self):
        """Drop the current shape down by one block."""
        if not self.check_collision((1, 0)):
            self.current_pos[0] += 1
        else:
            self.merge_shape()  # Merge the shape if it can't drop
            lines_to_clear = self.get_lines_to_clear()  # Get completed lines

            if self.reset_shape():  # Check for game over after resetting
                return True, []  # Game over, no lines to clear
            return False, lines_to_clear  # Return the state and lines to clear
        return False, []  # Not game over, no lines to clear

    def get_current_shape_status(self):
        return self.current_shape['shape'], self.current_pos

    def get_next_shape_status(self):
        return self.next_shape

    def get_score(self):
        return self.score
