import random
import pygame


def acc_factor(paddle, ball):
    ball_center = ball.position[1] + ball.height / 2
    paddle_center = paddle.y + paddle.height / 2

    distance = ball_center - paddle_center

    if distance == 0:
        distance = random.randint(10, 100)

    return distance / 10


def collision_screen_left(ball):
    return ball.position[0] <= 0


def collision_screen_right(ball):
    surface_width = pygame.display.get_surface().get_width()
    return ball.position[0] + ball.width >= surface_width


def collision_screen_top(ball):
    return ball.position[1] <= 0


def collision_screen_bottom(ball):
    surface_height = pygame.display.get_surface().get_height()
    return ball.position[1] + ball.height >= surface_height


def collision(paddle, ball):
    return aabb_collision(
        paddle.x,
        paddle.y,
        paddle.width,
        paddle.height,
        ball.position[0],
        ball.position[1],
        ball.width,
        ball.height
    )


def aabb_collision(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    collision_x = a_x + a_width >= b_x and b_x + b_width >= a_x
    collision_y = a_y + a_height >= b_y and b_y + b_height >= a_y

    return collision_x and collision_y
