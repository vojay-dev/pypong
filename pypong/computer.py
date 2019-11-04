class Computer:

    def move(self, paddle, ball):
        paddle_center = paddle.y + paddle.height / 2
        ball_center = ball.position[1] + ball.height / 2

        distance = abs(paddle_center - ball_center)

        if distance > 20 and paddle_center > ball_center:
            paddle.move_up()

        if distance > 20 and paddle_center < ball_center:
            paddle.move_down()
