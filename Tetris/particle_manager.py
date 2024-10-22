
import random
from particle import Particle
from constants import *
from utils import *

class ParticleManager:
    def __init__(self, game_surface, draw_game_components):
        self.game_surface = game_surface
        self.draw_game_components = draw_game_components

    def explode_line(self, row_index, tetris, screen, clock):
        """Create a simple explosion effect on the cleared row."""
        particles = self.get_particles(row_index, tetris)
        explosion_duration = 300
        explosion_start_time = pygame.time.get_ticks()

        while pygame.time.get_ticks() - explosion_start_time < explosion_duration:
            # Redraw game components behind the explosion
            self.draw_game_components()

            # Update and draw all particles
            for particle in particles:
                particle.update()
                particle.draw(self.game_surface)

            # Blit the game surface to the main screen and update display
            screen.blit(self.game_surface, (20, 20))
            pygame.display.flip()
            clock.tick(EXPLOSION_FPS)

            # Remove dead particles
            particles = [p for p in particles if p.is_alive()]

    def get_particles(self, row_index, tetris):
        particles = []
        for x in range(GRID_WIDTH):
            block_color = tetris.grid[row_index][x]
            if block_color != 0:
                dark_color = get_darken_color(block_color)
                for _ in range(random.randint(2, 10)):  # Create multiple particles per block
                    particle_x = (x * BLOCK_SIZE) + random.randint(-BLOCK_SIZE // 2, BLOCK_SIZE // 2)
                    particle_y = (row_index * BLOCK_SIZE) + random.randint(-BLOCK_SIZE // 2, BLOCK_SIZE // 2)
                    radius = random.randint(2, 6)
                    particles.append(Particle(particle_x, particle_y, dark_color, radius))
        return particles
