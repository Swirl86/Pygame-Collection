import random
import pygame

class Particle:
    def __init__(self, x, y, color, radius):
        """Initialize the particle with position, color, and radius."""
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.lifetime = random.randint(30, 60)

    def update(self):
        """Update particle position and shrink radius over time."""
        self.lifetime -= 1
        if self.radius > 0:
            self.radius -= 0.1  # Slowly shrink the particle's size

    def is_alive(self):
        """Check if the particle is still alive."""
        return self.lifetime > 0 and self.radius > 0

    def draw(self, surface):
        """Draw the particle on the given surface."""
        if self.is_alive():
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))
