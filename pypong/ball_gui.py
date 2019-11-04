import pygame


class BallGui:

    def __init__(self, ball):
        self.ball = ball
        self.font = pygame.font.Font('freesansbold.ttf', 18)

    def draw(self, surface):
        surface_width = pygame.display.get_surface().get_width()

        text = self.font.render('Ball Position: ({}, {})'.format(
            round(self.ball.position[0]),
            round(self.ball.position[1])
        ), True, (255, 255, 153))

        text_rect = text.get_rect(center=(surface_width / 2, 20))
        surface.blit(text, text_rect)

        text = self.font.render('Ball Acceleration: ({}, {})'.format(
            round(self.ball.acceleration[0], 2),
            round(self.ball.acceleration[1], 2)
        ), True, (255, 255, 153))

        text_rect = text.get_rect(center=(surface_width / 2, 40))
        surface.blit(text, text_rect)
