import pygame

from asset import get_assets_dir


class Background:

    def __init__(self):
        self.image = pygame.image.load(
            '{}/background.jpg'.format(get_assets_dir())
        ).convert_alpha()

        surface_width = pygame.display.get_surface().get_width()
        surface_height = pygame.display.get_surface().get_height()

        self._flash = pygame.Surface((surface_width, surface_height), pygame.SRCALPHA)
        self._flash_alpha = 0
        self._flash_color = (255, 0, 0)

    def update(self):
        self._flash_alpha = max(0, self._flash_alpha - 10)

    def draw(self, surface):
        surface.blit(self.image, (0, 0))

        self._flash.fill((self._flash_color[0], self._flash_color[1], self._flash_color[2], self._flash_alpha))
        surface.blit(self._flash, (0, 0))

    def flash(self, color=(255, 0, 0), alpha=150):
        self._flash_color = color
        self._flash_alpha = alpha
