import pygame


class PaddleGui:

    def __init__(self, paddle, x=20):
        self.paddle = paddle
        self.x = x
        self.font = pygame.font.Font('freesansbold.ttf', 18)

    def draw(self, surface):
        text = self.font.render('Lives: {}'.format(self.paddle.lives), True, (102, 255, 153))
        surface.blit(text, (self.x, 10))

        text = self.font.render('Y: {}'.format(self.paddle.y), True, (153, 204, 255))
        surface.blit(text, (self.x, 30))
