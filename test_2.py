import csv
import time

from sklearn import tree
import numpy as np
import graphviz
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import ParameterSampler
from sklearn.model_selection import ParameterGrid
from sklearn.inspection import permutation_importance

from collections import defaultdict
from scipy.stats import spearmanr
from scipy.cluster import hierarchy

k = 1000

clf_reg_10 = [tree.DecisionTreeClassifier(min_samples_leaf=10, min_samples_split=10, max_features=None,
                                          random_state=0)] * k
clf_rand_10_3 = [RandomForestClassifier(n_estimators=10, min_samples_leaf=3, min_samples_split=3,
                                        max_features=None, random_state=42)] * k
clf_rand_10_10 = [RandomForestClassifier(n_estimators=10, min_samples_leaf=10, min_samples_split=10,
                                         max_features=None, random_state=42)] * k
clf_rand_10_20 = [RandomForestClassifier(n_estimators=10, min_samples_leaf=20, min_samples_split=20,
                                         max_features=None, random_state=42)] * k
clf_rand_10 = [RandomForestClassifier(n_estimators=10,
                                      max_features=None, random_state=42)] * k
# clf_rand_100_def = RandomForestClassifier()
# clf_rand_10_1 = RandomForestClassifier(n_estimators = 10, random_state=42, max_features=None)
# clf_rand_10_1 = RandomForestClassifier(n_estimators = 1, random_state=42, max_features=None, warm_start=True)
clf_rand_20_1 = [RandomForestClassifier(n_estimators=20, max_features=None, random_state=42)] * k
clf_rand_100_1 = [RandomForestClassifier(n_estimators=100, max_features=None, random_state=42)] * k
# clf_rand_10_3 = RandomForestClassifier(n_estimators = 10, min_samples_leaf = 3, min_samples_split=3,
#                                  random_state=42, max_features=None)
# clf_rand_100_def = RandomForestClassifier()
# clf_rand_10_1 = RandomForestClassifier(n_estimators = 10, random_state=42, max_features=None)
# clf_rand_10_1 = RandomForestClassifier(n_estimators = 1, random_state=42, max_features=None, warm_start=True)
# clf_rand_20_1 = RandomForestClassifier(n_estimators=20, random_state=42, max_features=None )
# clf_rand_100_1 = RandomForestClassifier(n_estimators=100, random_state=42, max_features=None)

import LogiReg, LinearReg, MultiReg
import random
from itertools import product

games = []
results = []

rows = []


def average(arr_3_D):
    avg = [0] * 3
    for a in arr_3_D:
        avg[0] += a[0]
        avg[1] += a[1]
        avg[2] += a[2]
    avg[0] /= len(arr_3_D)
    avg[1] /= len(arr_3_D)
    avg[2] /= len(arr_3_D)
    return avg


def rows_extrac():
    with open(r'data\combine_data.csv', encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)


def create_training_group():
    global games, results
    games = []
    results = []
    i = 2
    # random.shuffle(rows)
    for row in rows:
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        lst = []
        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0':
            i += 1
            continue
        lst.append(float(row['h_won']) / float(h_played))
        lst.append(float(row['h_won_h']) / float(h_played_h))

        lst.append(float(row['h_drawn']) / float(h_played))
        lst.append(float(row['h_drawn_h']) / float(h_played_h))
        lst.append(float(row['h_lost']) / float(h_played))
        lst.append(float(row['h_lost_h']) / float(h_played_h))

        lst.append(float(row['h_points']) / float(h_played))

        lst.append(float(row['h_points_h']) / float(h_played_h))

        lst.append(float(row['h_scored']) / float(h_played))
        lst.append(float(row['h_scored_h']) / float(h_played_h))
        lst.append(float(row['h_conced']) / float(h_played))
        lst.append(float(row['h_conced_h']) / float(h_played_h))

        lst.append(float(row['h_clean']) / float(h_played))
        lst.append(float(row['h_clean_h']) / float(h_played_h))
        lst.append(float(row['h_fail']) / float(h_played))
        lst.append(float(row['h_fail_h']) / float(h_played_h))
        ####
        lst.append(float(row['h_goal_diff']) / 100)
        lst.append(float(row['h_goal_diff_h']) / 100)
        lst.append(float(row['h_shots']) / float(h_played))
        lst.append(float(row['h_shots_h']) / float(h_played_h))
        lst.append(float(row['h_shots_against']) / float(h_played))
        lst.append(float(row['h_shots_against_h']) / float(h_played_h))
        lst.append(float(row['h_shots_target']) / float(h_played))
        lst.append(float(row['h_shots_target_h']) / float(h_played_h))
        lst.append(float(row['h_shots_diff_h']) / float(h_played_h))
        lst.append(float(row['h_shots_diff']) / float(h_played))
        lst.append(float(row['h_shots_target_against']) / float(h_played))
        lst.append(float(row['h_shots_target_against_h']) / float(h_played_h))
        lst.append(float(row['h_shots_target_diff']) / float(h_played))
        lst.append(float(row['h_shots_target_diff_h']) / float(h_played_h))
        lst.append(float(row['h_red_cards']) / float(h_played))
        lst.append(float(row['h_red_cards_h']) / float(h_played_h))
        lst.append(float(row['h_red_cards_against']) / float(h_played))
        lst.append(float(row['h_red_cards_diff']) / float(h_played))
        lst.append(float(row['h_red_cards_against_h']) / float(h_played_h))
        lst.append(float(row['h_red_cards_diff_h']) / float(h_played))
        lst.append(float(row['h_elo']) / 2200)
        lst.append(float(row['h_fifa_rating']) / 100)
        lst.append(float(row['h_current_win_streak']))
        lst.append(float(row['h_current_no_lose_streak']))
        lst.append(float(row['h_current_lose_streak']))
        lst.append(float(row['h_current_no_win_streak']))
        lst.append(float(row['h_last_5_games_points']) / 5)
        lst.append(float(row['h_last_5_games_wins']) / 5)
        lst.append(float(row['h_last_5_games_loss']) / 5)
        lst.append(float(row['h_last_5_games_draw']) / 5)
        lst.append(float(row['h_last_5_games_scored']) / 5)
        lst.append(float(row['h_last_5_games_conced']) / 5)
        lst.append(float(row['h_last_5_games_goal_diff']) / 5)
        lst.append(float(row['h_last_5_games_clean']) / 5)
        lst.append(float(row['h_last_5_games_failed']) / 5)

        lst.append(float(row['a_won']) / float(a_played))
        lst.append(float(row['a_won_a']) / float(a_played_a))

        lst.append(float(row['a_drawn']) / float(a_played))
        lst.append(float(row['a_drawn_a']) / float(a_played_a))
        lst.append(float(row['a_lost']) / float(a_played))
        lst.append(float(row['a_lost_a']) / float(a_played_a))

        lst.append(float(row['a_points']) / float(a_played))

        lst.append(float(row['a_points_a']) / float(a_played_a))

        lst.append(float(row['a_scored']) / float(a_played))
        lst.append(float(row['a_scored_a']) / float(a_played_a))
        lst.append(float(row['a_conced']) / float(a_played))
        lst.append(float(row['a_conced_a']) / float(a_played_a))

        lst.append(float(row['a_clean']) / float(a_played))
        lst.append(float(row['a_clean_a']) / float(a_played_a))
        lst.append(float(row['a_fail']) / float(a_played))
        lst.append(float(row['a_fail_a']) / float(a_played_a))
        ####
        lst.append(float(row['a_goal_diff']) / 100)
        lst.append(float(row['a_goal_diff_a']) / 100)
        lst.append(float(row['a_shots']) / float(a_played))
        lst.append(float(row['a_shots_a']) / float(a_played_a))
        lst.append(float(row['a_shots_against']) / float(a_played))
        lst.append(float(row['a_shots_against_a']) / float(a_played_a))
        lst.append(float(row['a_shots_target']) / float(a_played))
        lst.append(float(row['a_shots_target_a']) / float(a_played_a))
        lst.append(float(row['a_shots_diff_a']) / float(a_played_a))
        lst.append(float(row['a_shots_diff']) / float(a_played))
        lst.append(float(row['a_shots_target_against']) / float(a_played_a))
        lst.append(float(row['a_shots_target_against_a']) / float(a_played_a))
        lst.append(float(row['a_shots_target_diff']) / float(a_played))
        lst.append(float(row['a_shots_target_diff_a']) / float(a_played_a))
        lst.append(float(row['a_red_cards']) / float(a_played))
        lst.append(float(row['a_red_cards_a']) / float(a_played_a))
        lst.append(float(row['a_red_cards_against']) / float(a_played))
        lst.append(float(row['a_red_cards_diff']) / float(a_played))
        lst.append(float(row['a_red_cards_against_a']) / float(a_played_a))
        lst.append(float(row['a_red_cards_diff_a']) / float(a_played_a))
        lst.append(float(row['a_elo']) / 2200)
        lst.append(float(row['a_fifa_rating']) / 100)
        lst.append(float(row['a_current_win_streak']))
        lst.append(float(row['a_current_no_lose_streak']))
        lst.append(float(row['a_current_lose_streak']))
        lst.append(float(row['a_current_no_win_streak']))
        lst.append(float(row['a_last_5_games_points']) / 5)
        lst.append(float(row['a_last_5_games_wins']) / 5)
        lst.append(float(row['a_last_5_games_loss']) / 5)
        lst.append(float(row['a_last_5_games_draw']) / 5)
        lst.append(float(row['a_last_5_games_scored']) / 5)
        lst.append(float(row['a_last_5_games_conced']) / 5)
        lst.append(float(row['a_last_5_games_goal_diff']) / 5)
        lst.append(float(row['a_last_5_games_clean']) / 5)
        lst.append(float(row['a_last_5_games_failed']) / 5)
        # lst.append(round(np.random.random()))
        # lst.append(round(np.random.random()*10))
        # lst.append(round(np.random.random() * 100))
        # lst.append(round(np.random.random() * 1000))
        # lst.append(round(np.random.random() * 10000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        #
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        #
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        #
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        # lst.append(round(np.random.random() * 100000))
        #
        # lst.append(round(np.random.normal(0,0.1,1)[0] * 100000000))
        # lst.append(round(np.random.normal(0,0.1,1)[0] * 100000000))
        # lst.append(round(np.random.normal(0,0.1,1)[0] * 100000000))
        # lst.append(round(np.random.normal(0,0.1,1)[0] * 100000000))
        # lst.append(round(np.random.normal(0,0.1,1)[0] * 100000000))
        #
        # lst.append(round(np.random.normal(0,0.1,1)[0] * 100000000))
        # lst.append(round(np.random.normal(0,0.1,1)[0] * 100000000))
        # lst.append(round(np.random.normal(0,0.1,1)[0] * 100000000))
        # lst.append(round(np.random.normal(0,0.1,1)[0] * 100000000))
        # lst.append(round(np.random.normal(0,0.1,1)[0] * 100000000))

        if i == 18000:
            break
        games.append(lst)
        if row['RESULT'] == "HOME":
            results.append(0.0)
        if row['RESULT'] == "DRAW":
            results.append(1.0)
        if row['RESULT'] == "AWAY":
            results.append(2.0)
        i += 1


def odds_func(row):
    home_odds = float(row['home_odd'])
    draw_odds = float(row['draw_odd'])
    away_odds = float(row['away_odd'])
    return home_odds, draw_odds, away_odds


def game_stats(row):
    h_played = row['h_played']
    h_played_h = row['h_played_h']
    a_played = row['a_played']
    a_played_a = row['a_played_a']
    lst = []
    lst.append(float(row['h_won']) / float(h_played))
    lst.append(float(row['h_won_h']) / float(h_played_h))

    lst.append(float(row['h_drawn']) / float(h_played))
    lst.append(float(row['h_drawn_h']) / float(h_played_h))
    lst.append(float(row['h_lost']) / float(h_played))
    lst.append(float(row['h_lost_h']) / float(h_played_h))

    lst.append(float(row['h_points']) / float(h_played))

    lst.append(float(row['h_points_h']) / float(h_played_h))

    lst.append(float(row['h_scored']) / float(h_played))
    lst.append(float(row['h_scored_h']) / float(h_played_h))
    lst.append(float(row['h_conced']) / float(h_played))
    lst.append(float(row['h_conced_h']) / float(h_played_h))

    lst.append(float(row['h_clean']) / float(h_played))
    lst.append(float(row['h_clean_h']) / float(h_played_h))
    lst.append(float(row['h_fail']) / float(h_played))
    lst.append(float(row['h_fail_h']) / float(h_played_h))

    # 'h_hit_woodwork': 0, 'h_hit_woodwork_h': 0,
    # 'h_hit_woodwork_against': 0, 'h_hit_woodwork_diff': 0,

    lst.append(float(row['h_goal_diff']) / 100)
    lst.append(float(row['h_goal_diff_h']) / 100)
    lst.append(float(row['h_shots']) / float(h_played))
    lst.append(float(row['h_shots_h']) / float(h_played_h))
    lst.append(float(row['h_shots_against']) / float(h_played))
    lst.append(float(row['h_shots_against_h']) / float(h_played_h))
    lst.append(float(row['h_shots_target']) / float(h_played))
    lst.append(float(row['h_shots_target_h']) / float(h_played_h))
    lst.append(float(row['h_shots_diff_h']) / float(h_played_h))
    lst.append(float(row['h_shots_diff']) / float(h_played))
    lst.append(float(row['h_shots_target_against']) / float(h_played))
    lst.append(float(row['h_shots_target_against_h']) / float(h_played_h))
    lst.append(float(row['h_shots_target_diff']) / float(h_played))
    lst.append(float(row['h_shots_target_diff_h']) / float(h_played_h))
    lst.append(float(row['h_red_cards']) / float(h_played))
    lst.append(float(row['h_red_cards_h']) / float(h_played_h))
    lst.append(float(row['h_red_cards_against']) / float(h_played))
    lst.append(float(row['h_red_cards_diff']) / float(h_played))
    lst.append(float(row['h_red_cards_against_h']) / float(h_played_h))
    lst.append(float(row['h_red_cards_diff_h']) / float(h_played_h))
    lst.append(float(row['h_elo']) / 2200)
    lst.append(float(row['h_fifa_rating']) / 100)
    lst.append(float(row['h_current_win_streak']))
    lst.append(float(row['h_current_no_lose_streak']))
    lst.append(float(row['h_current_lose_streak']))
    lst.append(float(row['h_current_no_win_streak']))
    lst.append(float(row['h_last_5_games_points']) / 5)
    lst.append(float(row['h_last_5_games_wins']) / 5)
    lst.append(float(row['h_last_5_games_loss']) / 5)
    lst.append(float(row['h_last_5_games_draw']) / 5)
    lst.append(float(row['h_last_5_games_scored']) / 5)
    lst.append(float(row['h_last_5_games_conced']) / 5)
    lst.append(float(row['h_last_5_games_goal_diff']) / 5)
    lst.append(float(row['h_last_5_games_clean']) / 5)
    lst.append(float(row['h_last_5_games_failed']) / 5)

    lst.append(float(row['a_won']) / float(a_played))
    lst.append(float(row['a_won_a']) / float(a_played_a))

    lst.append(float(row['a_drawn']) / float(a_played))
    lst.append(float(row['a_drawn_a']) / float(a_played_a))

    lst.append(float(row['a_lost']) / float(a_played))
    lst.append(float(row['a_lost_a']) / float(a_played_a))

    lst.append(float(row['a_points']) / float(a_played))
    lst.append(float(row['a_points_a']) / float(a_played_a))

    lst.append(float(row['a_scored']) / float(a_played))
    lst.append(float(row['a_scored_a']) / float(a_played_a))
    lst.append(float(row['a_conced']) / float(a_played))
    lst.append(float(row['a_conced_a']) / float(a_played_a))

    lst.append(float(row['a_clean']) / float(a_played))
    lst.append(float(row['a_clean_a']) / float(a_played_a))
    lst.append(float(row['a_fail']) / float(a_played))
    lst.append(float(row['a_fail_a']) / float(a_played_a))

    lst.append(float(row['a_goal_diff']) / 100)
    lst.append(float(row['a_goal_diff_a']) / 100)
    lst.append(float(row['a_shots']) / float(a_played))
    lst.append(float(row['a_shots_a']) / float(a_played_a))
    lst.append(float(row['a_shots_against']) / float(a_played))
    lst.append(float(row['a_shots_against_a']) / float(a_played_a))
    lst.append(float(row['a_shots_target']) / float(a_played))
    lst.append(float(row['a_shots_target_a']) / float(a_played_a))
    lst.append(float(row['a_shots_diff_a']) / float(a_played_a))
    lst.append(float(row['a_shots_diff']) / float(a_played))
    lst.append(float(row['a_shots_target_against']) / float(a_played))
    lst.append(float(row['a_shots_target_against_a']) / float(a_played_a))
    lst.append(float(row['a_shots_target_diff']) / float(a_played))
    lst.append(float(row['a_shots_target_diff_a']) / float(a_played_a))
    lst.append(float(row['a_red_cards']) / float(a_played))
    lst.append(float(row['a_red_cards_a']) / float(a_played_a))
    lst.append(float(row['a_red_cards_against']) / float(a_played))
    lst.append(float(row['a_red_cards_diff']) / float(a_played))
    lst.append(float(row['a_red_cards_against_a']) / float(a_played_a))
    lst.append(float(row['a_red_cards_diff_a']) / float(a_played_a))
    lst.append(float(row['a_elo']) / 2200)
    lst.append(float(row['a_fifa_rating']) / 100)
    lst.append(float(row['a_current_win_streak']))
    lst.append(float(row['a_current_no_lose_streak']))
    lst.append(float(row['a_current_lose_streak']))
    lst.append(float(row['a_current_no_win_streak']))
    lst.append(float(row['a_last_5_games_points']) / 5)
    lst.append(float(row['a_last_5_games_wins']) / 5)
    lst.append(float(row['a_last_5_games_loss']) / 5)
    lst.append(float(row['a_last_5_games_draw']) / 5)
    lst.append(float(row['a_last_5_games_scored']) / 5)
    lst.append(float(row['a_last_5_games_conced']) / 5)
    lst.append(float(row['a_last_5_games_goal_diff']) / 5)
    lst.append(float(row['a_last_5_games_clean']) / 5)
    lst.append(float(row['a_last_5_games_failed']) / 5)

    return lst


def choose_bet(odds, predict):
    options = ['HOME', 'DRAW', 'AWAY']
    # return random.choice(options)
    best = []
    if odds == (0.0, 0.0, 0.0):
        return None
    # return random.choice(options)
    # return 'DRAW'
    if odds[0] * predict[0] > 1.0:
        best.append((odds[0] * predict[0], "HOME"))
    if odds[1] * predict[1] > 1.0:
        best.append((odds[1] * predict[1], "DRAW"))
    if odds[2] * predict[2] > 1.0:
        best.append((odds[2] * predict[2], "AWAY"))
    if len(best) == 0:
        return None
    best.sort()
    best.reverse()
    return best[0][1]


def bet(row, bet_chosen):
    return bet_chosen == row['RESULT']


def win(odds, choice):
    if choice == 'HOME':
        return odds[0]
    if choice == 'DRAW':
        return odds[1]
    if choice == 'AWAY':
        return odds[2]


x_test = []
y_test = []
odds = []


def check_odds(odds):
    return odds[0] <= 0 or odds[1] <= 0 or odds[2] <= 0


def create_test_group():
    global x_test, y_test, odds
    for i in range(18001, 25769, 2):
        # for i in range(len(rows)):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if row['home_odd'] == '':
            continue
        odds.append(odds_func(row))

        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0' or check_odds(odds):
            continue

        x_test.append(game_stats(row))
        if row['RESULT'] == "HOME":
            y_test.append(0.0)
        if row['RESULT'] == "DRAW":
            y_test.append(1.0)
        if row['RESULT'] == "AWAY":
            y_test.append(2.0)


rets = []


def ret_calc(odds):
    # print(odds)
    sum = 0.0
    for odd in odds:
        sum += (1 / odd)
    return 1 / sum


rows_extrac()
create_training_group()


# create_test_group()
def transform(X, sel):
    new_X = [[row[f] for f in sel] for row in X]
    return new_X


def play(clf, sel=None):
    balance = 0.0
    bets = 0
    wins = 0
    for i in range(18001, 25769, 2):
        # for i in range(len(rows)):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0':
            continue
        odds = odds_func(row)
        if odds[0] == 0.0 or odds[1] == 0.0 or odds[2] == 0.0:
            continue
        ret = ret_calc(odds)
        rets.append(ret)
        game_test = game_stats(row)
        # game_test = normal_single_games(game_test)
        if sel != None:
            game_test = transform([game_test], sel)
        # prediction = clf.calculate_prob_for_test_group([game_test])
        # prediction = tuple(predict[0] for predict in prediction)
        prediction = clf.predict_proba([game_test])
        # prediction = clf.predict_proba([game_test])
        # predictions = [1 / result for result in prediction[0]]
        # bet_chosen = choose_bet(odds, prediction)
        bet_chosen = choose_bet(odds, prediction[0])
        if not bet_chosen:
            continue
        balance -= 1
        bets += 1
        # print("league =", row['league'])
        # print("date =", row['date'])
        # print("bet =", bet_chosen)
        #   print("odds: ", odds)
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
        #  print("win = ", winning)
        # print("balance = ", balance)
    # print(balance / len(rows))
    #   print("balance = ", balance)
    # print(balance / (len(rows) - 20000))
    # print("number of bets = ", bets )
    # print("number of wins =", wins)
    # print(balance / ((24800-18000)/2))
    # print("return = ", balance / bets )
    return balance / bets


def play_reg(clf):
    # print("importance =", clf.feature_importances_)
    #  global row, game_test
    balance = 0.0
    bets = 0
    wins = 0
    for i in range(18001, 25769, 2):
        # for i in range(len(rows)):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0':
            continue
        odds = odds_func(row)
        if odds[0] == 0.0 or odds[1] == 0.0 or odds[2] == 0.0:
            continue
        # ret = ret_calc(odds)
        # rets.append(ret)
        game_test = game_stats(row)
        # game_test = normal_single_games(game_test)
        # game_test = rfe.transform([game_test])
        prediction = clf.calculate_prob_for_test_group([game_test])
        prediction = tuple(predict[0] for predict in prediction)
        bet_chosen = choose_bet(odds, prediction)
        if not bet_chosen:
            continue
        balance -= 1
        bets += 1
        # print("league =", row['league'])
        # print("date =", row['date'])
        # print("bet =", bet_chosen)
        #   print("odds: ", odds)
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
    print("number of bets = ", bets)
    print("number of wins =", wins)
    print("return = ", balance / bets)
    return balance / bets


def choose_bet_random(odds):
    options = ['HOME', 'DRAW', 'AWAY']
    # return random.choice(options)
    best = []
    if odds == (0.0, 0.0, 0.0):
        return None
    return random.choice(options)


def play_random():
    # print("importance =", clf.feature_importances_)
    # global row, game_test
    balance = 0.0
    bets = 0
    wins = 0
    for i in range(18001, 25769, 2):
        # for i in range(len(rows)):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0':
            continue
        odds = odds_func(row)
        if odds[0] == 0.0 or odds[1] == 0.0 or odds[2] == 0.0:
            continue
        # if odds != (0.0,0.0,0.0):
        # print("ret = ", ret_calc(odds))
        game_test = game_stats(row)
        bet_chosen = choose_bet_random(odds)
        if not bet_chosen:
            continue
        balance -= 1
        bets += 1
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
    #     print("win = ", winning)
    #  print("balance = ", balance)
    # print(balance / len(rows))
    # print("balance = ", balance)
    # print(balance / (len(rows) - 20000))
    # print("number of bets = ", bets)
    # print("number of wins =", wins)
    # print("balance = ", balance)
    # print("normal balanced = ", balance / ((24800-18000)/2))
    return balance / bets


def choose_bet_specific(odds, string):
    if odds == (0.0, 0.0, 0.0):
        return None
    return string


def choose_bet_favourite(odds):
    if odds == (0.0, 0.0, 0.0):
        return None
    options = ['HOME', 'DRAW', 'AWAY']
    bet = min(odds)
    ind = odds.index(bet)
    return options[ind]


def choose_bet_underdog(odds):
    if odds == (0.0, 0.0, 0.0):
        return None
    options = ['HOME', 'DRAW', 'AWAY']
    bet = max(odds)
    ind = odds.index(bet)
    return options[ind]


def play_specific(string):
    # print("importance =", clf.feature_importances_)
    # global row, game_test
    balance = 0.0
    for i in range(20000, len(rows)):
        # for i in range(len(rows)):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0':
            continue
        odds = odds_func(row)
        game_test = game_stats(row)
        # prediction = clf.predict_proba([game_test])
        # predictions = [1 / result for result in prediction[0]]
        bet_chosen = choose_bet_specific(odds, string)
        if not bet_chosen:
            continue
        balance -= 1
        #  print("league =", row['league'])
        #  print("date =", row['date'])
        #   print("bet =", bet_chosen)
        #  print("odds: ", odds)
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
        #   print("win = ", winning)
    # print("balance = ", balance)
    # print(balance / len(rows))
    # print("balance = ", balance)
    print(balance / (len(rows) - 20000))
    return balance / (len(rows) - 20000)


def play_underdog():
    # print("importance =", clf.feature_importances_)
    # global row, game_test
    bets = 0
    wins = 0
    balance = 0.0
    for i in range(45000, 59000, 2):
        # for i in range(len(rows)):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0':
            continue
        odds = odds_func(row)
        if odds[0] == 0.0 or odds[1] == 0.0 or odds[2] == 0.0:
            continue
        game_test = game_stats(row)
        # prediction = clf.predict_proba([game_test])
        # predictions = [1 / result for result in prediction[0]]
        bet_chosen = choose_bet_underdog(odds)
        if not bet_chosen:
            continue
        bets += 1
        balance -= 1
        #  print("league =", row['league'])
        #  print("date =", row['date'])
        #   print("bet =", bet_chosen)
        #  print("odds: ", odds)
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
        #   print("win = ", winning)
    # print("balance = ", balance)
    # print(balance / len(rows))
    # print("balance = ", balance)
    print("number of bets = ", bets)
    print("number of wins = ", wins)
    return (balance / bets)


def play_favourite():
    # print("importance =", clf.feature_importances_)
    # global row, game_test
    bets = 0
    wins = 0
    balance = 0.0
    for i in range(45000, 59000, 2):
        # for i in range(len(rows)):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0':
            continue
        odds = odds_func(row)
        if odds[0] == 0.0 or odds[1] == 0.0 or odds[2] == 0.0:
            continue
        game_test = game_stats(row)
        # prediction = clf.predict_proba([game_test])
        # predictions = [1 / result for result in prediction[0]]
        bet_chosen = choose_bet_favourite(odds)
        if not bet_chosen:
            continue
        bets += 1
        balance -= 1
        #  print("league =", row['league'])
        #  print("date =", row['date'])
        #   print("bet =", bet_chosen)
        #  print("odds: ", odds)
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
        #   print("win = ", winning)
    # print("balance = ", balance)
    print("number of bets = ", bets)
    print("number of wins = ", wins)
    return (balance / bets)


# random_profits = []
# home_profits = []
# draw_profits = []
# away_profits = []
# favour_profits = []
# underdog_profits = []


def normal_games():
    global games
    max_feature = [0] * len(games[0])
    min_feature = [0] * len(games[0])
    for game in games:
        for i, feature in enumerate(game):
            max_feature[i] = max(max_feature[i], feature)
            min_feature[i] = min(min_feature[i], feature)
    for game in games:
        for i in range(len(game)):
            game[i] = (game[i] - min_feature[i]) / (max_feature[i] - min_feature[i])


# estimators = list(range(10,115,15))

features_dict = {
    0: 'h_won / h_played',
    1: 'h_won_h / h_played_h',
    2: 'h_drawn / h_played',
    3: 'h_drawn_h / h_played_h',
    4: 'h_lost / h_played',
    5: 'h_lost_h / h_played_h',
    6: 'h_points / h_played',

    7: 'h_points_h / h_played_h',

    8: 'h_scored / h_played',
    9: 'h_scored_h / h_played_h',
    10: 'h_conced / h_played',
    11: 'h_conced_h / h_played_h',

    12: 'h_clean / h_played',
    13: 'h_clean_h / h_played_h',
    14: 'h_fail / h_played',
    15: 'h_fail_h / h_played_h',

    # 'h_hit_woodwork': 0, 'h_hit_woodwork_h': 0,
    # 'h_hit_woodwork_against': 0, 'h_hit_woodwork_diff': 0,

    16: 'h_goal_diff / 100',
    17: 'h_goal_diff_h / 100',
    18: 'h_shots / h_played',
    19: 'h_shots_h / h_played_h',
    20: 'h_shots_against / h_played',
    21: 'h_shots_against_h / h_played_h',
    22: 'h_shots_target / h_played',
    23: 'h_shots_target_h / h_played_h',
    24: 'h_shots_diff_h',
    25: 'h_shots_diff',
    26: 'h_shots_target_against',
    27: 'h_shots_target_against_h',
    28: 'h_shots_target_diff',
    29: 'h_shots_target_diff_h',

    30: 'h_red_cards / h_played',
    31: 'h_red_cards_h / h_played_h',
    32: 'h_red_cards_against / h_played',
    33: 'h_red_cards_diff',
    34: 'h_red_cards_against_h / h_played_h',
    35: 'h_red_cards_diff_h',
    36: 'h_elo / 2200',
    37: 'h_fifa_rating / 100',
    38: 'h_current_win_streak',
    39: 'h_current_no_lose_streak',
    40: 'h_current_lose_streak',
    41: 'h_current_no_win_streak',
    42: 'h_last_5_games_points / 5',
    43: 'h_last_5_games_wins / 5',
    44: 'h_last_5_games_loss / 5',
    45: 'h_last_5_games_draw / 5',
    46: 'h_last_5_games_scored / 5',
    47: 'h_last_5_games_conced / 5',
    48: 'h_last_5_games_goal_diff / 5',
    49: 'h_last_5_games_clean / 5',
    50: 'h_last_5_games_failed / 5',

    51: 'a_won / a_played',
    52: 'a_won_a / a_played_a',

    53: 'a_drawn / a_played',
    54: 'a_drawn_a / a_played_a',

    55: 'a_lost / a_played',
    56: 'a_lost_a / a_played_a',

    57: 'a_points / a_played',
    58: 'a_points_a / a_played_a',

    59: 'a_scored / a_played',
    60: 'a_scored_a / a_played_a',
    61: 'a_conced / a_played',
    62: 'a_conced_a / a_played_a',

    63: 'a_clean / a_played',
    64: 'a_clean_a / a_played_a',
    65: 'a_fail / a_played',
    66: 'a_fail_a / a_played_a',

    67: 'a_goal_diff / 100',
    68: 'a_goal_diff_a / 100',
    69: 'a_shots / a_played',
    70: 'a_shots_a / a_played_a',
    71: 'a_shots_against / a_played',
    72: 'a_shots_against_a / a_played_a',
    73: 'a_shots_target / a_played',
    74: 'a_shots_target_a / a_played_a',
    75: 'a_shots_diff_a',
    76: 'a_shots_diff',
    77: 'a_shots_target_against',
    78: 'a_shots_target_against_a',
    79: 'a_shots_target_diff',
    80: 'a_shots_target_diff_a',
    81: 'a_red_cards / a_played',
    82: 'a_red_cards_a / a_played_a',
    83: 'a_red_cards_against / a_played',
    84: 'a_red_cards_diff',
    85: 'a_red_cards_against_a / a_played_a',
    86: 'a_red_cards_diff_a',
    87: 'a_elo / 2200',
    88: 'a_fifa_rating / 100',
    89: 'a_current_win_streak',
    90: 'a_current_no_lose_streak',
    91: 'a_current_lose_streak',
    92: 'a_current_no_win_streak',
    93: 'a_last_5_games_points / 5',
    94: 'a_last_5_games_wins / 5',
    95: 'a_last_5_games_loss / 5',
    96: 'a_last_5_games_draw / 5',
    97: 'a_last_5_games_scored / 5',
    98: 'a_last_5_games_conced / 5',
    99: 'a_last_5_games_goal_diff / 5',
    100: 'a_last_5_games_clean / 5',
    101: 'a_last_5_games_failed / 5'
}

features = ['h_won'
    , 'h_won_h'
    , 'h_drawn'
    , 'h_drawn_h'
    , 'h_lost'
    , 'h_lost_h'
    , 'h_points'
    , 'h_points_h'
    , 'h_scored'
    , 'h_scored_h'
    , 'h_conced'
    , 'h_conced_h'
    , 'h_clean'
    , 'h_clean_h'
    , 'h_fail'
    , 'h_fail_h'
    , 'h_goal_diff'
    , 'h_goal_diff_h'
    , 'h_shots'
    , 'h_shots_h'
    , 'h_shots_against'
    , 'h_shots_against_h'
    , 'h_shots_target'
    , 'h_shots_target_h'
    , 'h_shots_diff_h'
    , 'h_shots_diff'
    , 'h_shots_target_against'
    , 'h_shots_target_against_h'
    , 'h_shots_target_diff'
    , 'h_shots_target_diff_h'
    , 'h_red_cards'
    , 'h_red_cards_h'
    , 'h_red_cards_against'
    , 'h_red_cards_diff'
    , 'h_red_cards_against_h'
    , 'h_red_cards_diff_h'
    , 'h_elo'
    , 'h_fifa_rating'
    , 'h_current_win_streak'
    , 'h_current_no_lose_streak'
    , 'h_current_lose_streak'
    , 'h_current_no_win_streak'
    , 'h_last_5_games_points'
    , 'h_last_5_games_wins'
    , 'h_last_5_games_loss'
    , 'h_last_5_games_draw'
    , 'h_last_5_games_scored'
    , 'h_last_5_games_conced'
    , 'h_last_5_games_goal_diff'
    , 'h_last_5_games_clean'
    , 'h_last_5_games_failed'
    , 'a_won'
    , 'a_won_a'
    , 'a_drawn'
    , 'a_drawn_a'
    , 'a_lost'
    , 'a_lost_a'
    , 'a_points'
    , 'a_points_a'
    , 'a_scored'
    , 'a_scored_a'
    , 'a_conced'
    , 'a_conced_a'
    , 'a_clean'
    , 'a_clean_a'
    , 'a_fail'
    , 'a_fail_a'
    , 'a_goal_diff'
    , 'a_goal_diff_a'
    , 'a_shots'
    , 'a_shots_a'
    , 'a_shots_against'
    , 'a_shots_against_a'
    , 'a_shots_target'
    , 'a_shots_target_a'
    , 'a_shots_diff_a'
    , 'a_shots_diff'
    , 'a_shots_target_against'
    , 'a_shots_target_against_a'
    , 'a_shots_target_diff'
    , 'a_shots_target_diff_a'
    , 'a_red_cards'
    , 'a_red_cards_a'
    , 'a_red_cards_against'
    , 'a_red_cards_diff'
    , 'a_red_cards_against_a'
    , 'a_red_cards_diff_a'
    , 'a_elo'
    , 'a_fifa_rating'
    , 'a_current_win_streak'
    , 'a_current_no_lose_streak'
    , 'a_current_lose_streak'
    , 'a_current_no_win_streak'
    , 'a_last_5_games_points'
    , 'a_last_5_games_wins'
    , 'a_last_5_games_loss'
    , 'a_last_5_games_draw'
    , 'a_last_5_games_scored'
    , 'a_last_5_games_conced'
    , 'a_last_5_games_goal_diff'
    , 'a_last_5_games_clean'
    , 'a_last_5_games_failed'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'

    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
    , 'random'
            ]

clf_tree_1 = tree.DecisionTreeClassifier(random_state=42)
clf_tree_2 = tree.DecisionTreeClassifier(random_state=42, min_samples_split=10, min_samples_leaf=10)
clf_forest_1 = RandomForestClassifier(random_state=42, n_estimators=10)
clf_forest_2 = RandomForestClassifier(random_state=42, n_estimators=10, min_samples_split=10, min_samples_leaf=10)
clf_forest_3 = RandomForestClassifier(random_state=42, n_estimators=50)

"""
for k in [20, 40, 60, 80]:
    print(k)
    start = time.time()
    # clf_tree_1.fit(games, results)
    # clf_tree_2.fit(games, results)
    # clf_forest_1.fit(games, results)
    # clf_forest_2.fit(games, results)
    rfe_tree_1 = RFE(estimator=clf_tree_1, n_features_to_select=k).fit(games, results)
    print(time.time() - start)
    rfe_tree_2 = RFE(estimator=clf_tree_2, n_features_to_select=k).fit(games, results)
    print(time.time() - start)
    rfe_forest_1 = RFE(estimator=clf_forest_1, n_features_to_select=k).fit(games, results)
    print(time.time() - start)
    rfe_forest_2 = RFE(estimator=clf_forest_2, n_features_to_select=k).fit(games, results)
    print(time.time() - start)

    #a = permutation_importance(estimator=clf_tree_1, X=games, y=results, n_repeats=102)
    #print(a.importance_mean_)
    print(play(clf_tree_1, rfe_tree_1))
    print(play(clf_tree_2, rfe_tree_2))
    print(play(clf_forest_1, rfe_forest_1))
    print(play(clf_forest_2, rfe_forest_2))
    print('****************************************')

print(sum([play_random() for i in range(10)])/10)"""


def score_function(estimator, X, y, odd=None):
    prob = estimator.predict_proba(X, y)
    best = []
    balance = wins = bets = 0
    for p, o, result in zip(prob, odd, y):
        if o[0] * p[0] > 1.0:
            best.append((o[0] * p[0], o[0], "HOME"))
        if o[1] * p[1] > 1.0:
            best.append((o[1] * p[1], o[0], "DRAW"))
        if o[2] * p[2] > 1.0:
            best.append((o[2] * p[2], o[0], "AWAY"))
        best.sort()
        best.reverse()
        choosen_bet = best[0][2]
        balance -= 1
        bets += 1
        if choosen_bet == y:
            balance += best[0][1]
            wins += 1
        return balance / bets


def shuffle_selected_cols(arr, selected):
    shuf = [x.copy() for x in arr]
    for i in selected:
        for k in range(4 * len(shuf)):
            a = round(np.random.random() * (len(shuf) - 1))
            b = round(np.random.random() * (len(shuf) - 1))
            tmp = shuf[a][i]
            check_1 = shuf[a][i] = shuf[b][i]
            check_2 = shuf[b][i] = tmp
    return shuf


def permutation_cal(clf, X, y, clusters=None):
    if clusters is None:
        return permutation_importance(estimator=clf, random_state=42, X=x_test, y=y_test, scoring=score_function,
                                      n_repeats=20)

    permutation_importance_return = [0] * len(X[0])

    for k in range(len(clusters)):
        l = k + 1
        # print(clusters[l])
        new_X = shuffle_selected_cols(X, clusters[l])

        a = play(clf.fit(X, y))
        b = play(clf.fit(new_X, y))
        for i in clusters[l]:
            # print(a-b)
            permutation_importance_return[i] = a - b

    return permutation_importance_return


# corr = spearmanr(games).correlation

# regular_permutation_tree = permutation_importance(estimator=clf_tree_2, random_state=42, X=x_test, y=y_test, scoring=score_function, n_repeats=20)
# regular_permutation_forest = permutation_importance(estimator=clf_forest_1, random_state=42, X=x_test, y=y_test, scoring=score_function, n_repeats=20)
# print(regular_permutation_tree.importance_mean)
# exit(0)

# corr_linkage = hierarchy.ward(corr)
# for k in [5, 4, 3, 2, 1]:
#     cluster_ids = hierarchy.fcluster(corr_linkage, 3, criterion='distance')
#     cluster_id_to_feature_ids = defaultdict(list)
#
#     for idx, cluster_id in enumerate(cluster_ids):
#         cluster_id_to_feature_ids[cluster_id].append(idx)
#     print(cluster_id_to_feature_ids)
#     print(cluster_id_to_feature_ids.__len__())
#     clf_tree_1.fit(games, results)
#     print(clf_tree_1.feature_importances_[0])
#     clf_tree_2.fit(games, results)
#     print(clf_tree_2.feature_importances_[0])
#     clf_forest_1.fit(games, results)
#     print(clf_forest_1.feature_importances_[0])
#     clf_forest_2.fit(games, results)
#     print(clf_forest_2.feature_importances_[0])
#     clf_forest_3.fit(games, results)
#     print(clf_forest_3.feature_importances_)
#     print(k)

# re = permutation_cal(clf_tree_2, games, results, cluster_id_to_feature_ids)
# print('tree_10_samples')
# print([i for i, a in enumerate(re) if a > 0])
# print([round(a, 4) + round(b, 2) for i, a, b in enumerate(zip(re, regular_permutation_tree)) if a > 0])
# print([i for i, a in enumerate(re) if a > 0.01])
# print([i for i, a in enumerate(re) if a > 0.02])
# print([i for i, a in enumerate(re) if a > 0.03])
# print([i for i, a in enumerate(re) if a > 0.04])
# #print([features_dict[i] for i, a in enumerate(re) if a > 0])
#
# print('forest_10_trees')
# re = permutation_cal(clf_forest_1, games, results, cluster_id_to_feature_ids)
# print([i for i, a in enumerate(re) if a > 0])
# print([round(a, 4) for i, a in enumerate(re) if a > 0])
# print([i for i, a in enumerate(re) if a > 0.01])
# print([i for i, a in enumerate(re) if a > 0.02])
# print([i for i, a in enumerate(re) if a > 0.03])
# print([i for i, a in enumerate(re) if a > 0.04])
# #print([features_dict[i] for i, a in enumerate(re) if a > 0])


def choose_features_from_clusters(estimator, X, y, fraction=0.5, distance_split=3):
    corr = spearmanr(X).correlation
    corr_linkage = hierarchy.ward(corr)

    cluster_ids = hierarchy.fcluster(corr_linkage, distance_split, criterion='distance')
    cluster_id_to_feature_ids = defaultdict(list)

    for idx, cluster_id in enumerate(cluster_ids):
        cluster_id_to_feature_ids[cluster_id].append(idx)
    estimator.fit(X, y)
    importance = estimator.feature_importances_
    selected_features = []
    for i in range(len(cluster_id_to_feature_ids)):
        a = [(importance[k], k) for k in cluster_id_to_feature_ids[i]]
        a = sorted(a, key=lambda x: x[0], reverse=True)
        cluster_id_to_feature_ids[i] = [k[1] for k in a]
        for j, f in enumerate(cluster_id_to_feature_ids[i]):
            if j > len(cluster_id_to_feature_ids[i]) * fraction:
                break
            selected_features.append(f)
    return selected_features





selected_features_ = choose_features_from_clusters(clf_forest_1, games, results, fraction=0.9)
games_ = transform(games, selected_features_)
print(games_[0].__len__())
print(games[0])
