from sklearn.linear_model import LogisticRegression
import math

class MultiRegSoccerGame:
    # create classifier for home and away
    # x - features list per game
    # y_h - home win or not
    # y_a - away win or not
    def __init__(self, x, y, params):
        self.clf = LogisticRegression(solver= 'liblinear', random_state=42, max_iter=1000, C=params['c'],
                                      fit_intercept=params['fit_intercept'], penalty=params['penalty'],
                                      class_weight=params['class_weight']).fit(x, y)
        self.X = x
        self.Y = y

    # return the probabilities per game in test group
    # x - test group
    def calculate_prob_for_test_group(self, x):
        run_test = self.clf.predict_proba(x)
        home = [k[0] for k in run_test]
        draw = [k[1] for k in run_test]
        away = [k[2] for k in run_test]
        return home, draw, away
"""
    # return in how much games the result with more probability is equal to the real result
    # 1 return parameter: number of games
    # 2 return parameter: number of the probability right
    # 3 return parameter:  the two above
    def take_the_more_prob(self, x, cost_per_game, real_results):
        odd = [[1, 1, 1]] * x.__len__()
        return self.profit_according_to_odd_bet(x, cost_per_game, odd, real_results)

    # return the profit according to odd
    # input parameters:
    # x - test group
    # cost_per_game - as is
    # odd_bet - per game have 3 cols: home_odd, away_odd, draw_odd
    # real_result - per game one of the values: "HOME", "AWAY", "DRAW"

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
        return pay, profit, profit - pay"""

