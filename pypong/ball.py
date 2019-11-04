import pygame
import numpy as np

from asset import get_assets_dir


class Ball:

    def __init__(self):
        self.width = 20
        self.height = 20

        self.position = self._initial_position()
        self.acceleration = np.array([5, 1])

        self.image = pygame.image.load(
            '{}/ball.png'.format(get_assets_dir())
        ).convert_alpha()

    def accelerate(self, factor):
        self.acceleration = np.multiply(self.acceleration, np.array([-1, 1]))
        self.acceleration[1] = factor

    def acceleration_multiply(self, vector):
        self.acceleration = np.multiply(self.acceleration, vector)

    def draw(self, surface):
        surface.blit(self.image, (self.position[0], self.position[1]))

    def reset(self):
        self.position = self._initial_position()
        self.acceleration = np.array([5, 1])

    def _initial_position(self):
        # place ball in the middle
        surface_width = pygame.display.get_surface().get_width()
        surface_height = pygame.display.get_surface().get_height()

        return np.array([
            surface_width / 2 - self.width / 2,
            surface_height / 2 - self.height / 2
        ])
