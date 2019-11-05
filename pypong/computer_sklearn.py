import random

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression


class Computer:

    def __init__(self):
        # features: y position of paddle center, y position of ball center
        training_data = [[50, 150], [400, 200], [100, 110], [210, 190]]

        # 0 = move up, 1 = move down
        target_values = [1, 0, 1, 0]

        self.model = LogisticRegression()
        self.model.fit(training_data, target_values)

        # prediction function used for linear regression
        print('f(paddle_center, ball_center) = {} + {} * paddle_center + {} * ball_center'.format(
            round(self.model.intercept_[0], 4),
            round(self.model.coef_[0][0], 4),
            round(self.model.coef_[0][1], 4)
        ))

        # uncomment to visualize the input and prediction data
        #self._visualize_data_relationship()

    def move(self, paddle, ball):
        paddle_center = paddle.y + paddle.height / 2
        ball_center = ball.position[1] + ball.height / 2

        prediction = self.model.predict([[paddle_center, ball_center]])
        print('input: [{}, {}], prediction: {}'.format(paddle_center, ball_center, prediction))

        if prediction == 0:
            paddle.move_up()

        if prediction == 1:
            paddle.move_down()

    def _visualize_data_relationship(self):
        random_inputs = []
        predictions = []

        for _ in range(0, 1000):
            y_paddle = random.randint(1, 300)
            y_ball = random.randint(1, 300)
            random_inputs.append([y_paddle, y_ball])

            predictions.append(self.model.predict([[y_paddle, y_ball]]))

        df = pd.DataFrame(random_inputs, columns=['y_center_paddle', 'y_center_ball'])
        df['action'] = predictions

        ax1 = df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='blue')
        df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='magenta',
                                   ax=ax1)

        plt.legend(labels=['Move UP', 'Move DOWN'])

        plt.title('Relationship between Y position of paddle center and Y position of ball center', size=24)
        plt.xlabel('Y position of paddle center', size=18)
        plt.ylabel('Y position of ball center', size=18)

        plt.show()
