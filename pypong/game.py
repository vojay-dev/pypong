import numpy as np

from computer import Computer
from background import Background
from ball import Ball
from ball_gui import BallGui
from collision import *
from paddle import Paddle
from paddle_gui import PaddleGui


class Game:

    def __init__(self, paddle1computer=None, paddle2computer=None):
        self.paddle1computer = paddle1computer
        self.paddle2computer = paddle2computer

        self._setup()
        self._game_loop()

    def _setup(self):
        pygame.init()
        pygame.display.set_caption("pypong")

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.timer = 0

        self.background = Background()

        self.paddle1 = Paddle()
        self.paddle2 = Paddle(760, 'player2.png')
        self.ball = Ball()

        self.paddle1_gui = PaddleGui(self.paddle1)
        self.paddle2_gui = PaddleGui(self.paddle2, 700)
        self.ball_gui = BallGui(self.ball)

        self.game_over = False
        self.running = True

    def _game_loop(self):
        while self.running:
            self.clock.tick(60)
            self.timer += self.clock.get_time()

            self.screen.fill((0, 0, 0))

            self._handle_input()

            if not self.game_over:
                self._update_state()
                self._draw_objects()

            if self.paddle1.lives == 0:
                self._game_over('Player 2')

            if self.paddle2.lives == 0:
                self._game_over('Player 1')

            # refresh display
            pygame.display.flip()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_r:
                    self._setup()

        if pygame.key.get_pressed()[pygame.K_w]:
            self.paddle1.move_up()

        if pygame.key.get_pressed()[pygame.K_s]:
            self.paddle1.move_down()

        if pygame.key.get_pressed()[pygame.K_UP]:
            self.paddle2.move_up()

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.paddle2.move_down()

        # let computer move the paddles if activated
        if self.paddle1computer is not None:
            self.paddle1computer.move(self.paddle1, self.ball)

        if self.paddle2computer is not None:
            self.paddle2computer.move(self.paddle2, self.ball)

    def _update_state(self):
        if collision_screen_left(self.ball):
            self.paddle1.lives -= 1
            self.ball.reset()
            self.background.flash()

        if collision_screen_right(self.ball):
            self.paddle2.lives -= 1
            self.ball.reset()
            self.background.flash()

        if collision_screen_top(self.ball) or collision_screen_bottom(self.ball):
            self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([1, -1]))

        self.ball.position += self.ball.acceleration
        self.ball.acceleration_multiply(np.array([1 + self.timer / 100000000, 1]))

        if collision(self.paddle1, self.ball):
            self.ball.accelerate(acc_factor(self.paddle1, self.ball))
            self.background.flash((0, 255, 0), 100)

        if collision(self.paddle2, self.ball):
            self.ball.accelerate(acc_factor(self.paddle2, self.ball))
            self.background.flash((0, 255, 0), 100)

        self.background.update()

    def _draw_objects(self):
        self.background.draw(self.screen)

        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)

        self.ball.draw(self.screen)

        self.paddle1_gui.draw(self.screen)
        self.paddle2_gui.draw(self.screen)
        self.ball_gui.draw(self.screen)

    def _game_over(self, winner):
        self.game_over = True

        surface_width = pygame.display.get_surface().get_width()
        surface_height = pygame.display.get_surface().get_height()

        font = pygame.font.Font('freesansbold.ttf', 18)

        text = font.render('GAME OVER', True, (255, 255, 255))
        text_rect = text.get_rect(center=(surface_width / 2, surface_height / 2 - 40))
        self.screen.blit(text, text_rect)

        text = font.render('WINNER: {}'.format(winner), True, (153, 255, 153))
        text_rect = text.get_rect(center=(surface_width / 2, surface_height / 2))
        self.screen.blit(text, text_rect)

        text = font.render('Press "r" to restart or "esc" to quit', True, (192, 192, 192))
        text_rect = text.get_rect(center=(surface_width / 2, surface_height / 2 + 40))
        self.screen.blit(text, text_rect)


if __name__ == '__main__':
    # play against computer
    game = Game(paddle2computer=Computer())

    # play against human
    #game = Game()

    # computer vs computer
    #game = Game(paddle1computer=Computer(), paddle2computer=Computer())
