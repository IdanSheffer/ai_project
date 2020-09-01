from sklearn.linear_model import LinearRegression
import math


class LinearRegSoccerGame:
    # create classifier for home and away
    # x - features list per game
    # y - 0 1 2 == home draw away
    def __init__(self, x, y):
        self.clf = LinearRegression().fit(x, y)
        self.X = x
        self.Y = y

    # return the probabilities per game in test group
    # x - test group
    def take_the_more_prob(self, x):
        bet = [round(k) for k in self.clf.predict(x)]

        return

    def calculate_prob_for_test_group(self, x):
        home = []
        draw = []
        away = []
        for k in self.clf.predict(x):
            if k == 0.0:
                home.append(1)
                draw.append(0)
                away.append(0)
            elif k == 1.0:
                home.append(0)
                draw.append(1)
                away.append(0)
            elif k == 2.0:
                home.append(0)
                draw.append(0)
                away.append(1)
            else:
                h = 1 / k
                d = 1 / abs(1 - k)
                a = 1 / abs(2 - k)
                norm_ = h + d + a
                home.append(h / norm_)
                draw.append(d / norm_)
                away.append(a / norm_)
        return home, draw, away

    # return in how much games the result with more probability is equal to the real result
    # 1 return parameter: number of games
    # 2 return parameter: number of the probability right
    # 3 return parameter:  the two above
    """def take_the_more_prob(self, x, cost_per_game, real_results):
        odd = [[1, 1, 1]] * x.__len__()
        return self.profit_according_to_odd_bet(x, cost_per_game, odd, real_results)"""

    # return the profit according to odd
    # input parameters:
    # x - test group
    # cost_per_game - as is
    # odd_bet - per game have 3 cols: home_odd, away_odd, draw_odd
    # real_result - per game one of the values: "HOME", "AWAY", "DRAW"
"""
    # 1 return parameter: cost for betting
    # 2 return parameter: profit
    # 3 return parameter: ratio between the two above
    def profit_according_to_odd_bet(self, x, cost_per_game, odd_bet, real_results):
        home, away, draw = self.calculate_prob_for_test_group(x)
        pay = 0
        profit = 0
        for h, a, d, odd, y in zip(home, away, draw, odd_bet, real_results):
            x_h = h * odd[0]
            x_a = a * odd[1]
            x_d = d * odd[2]
            if x_h > x_d and x_h > x_a:
                pay += cost_per_game
                if y == 'HOME':
                    profit += odd[0] * cost_per_game
            if x_a > x_d and x_a > x_h:
                pay += cost_per_game
                if y == 'AWAY':
                    profit += odd[1] * cost_per_game
            if x_d > x_h and x_d > x_a:
                pay += cost_per_game
                if y == 'DRAW':
                    profit += odd[2] * cost_per_game
        return pay, profit, profit - pay
"""