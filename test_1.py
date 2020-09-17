import csv
import time

import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import ParameterGrid

import LinearReg
import LogiReg
import MultiReg

k = 1

clf_reg_10 = tree.DecisionTreeClassifier(min_samples_leaf=10, min_samples_split=10, random_state=42, max_features=None)
clf_rand_10_3 = [RandomForestClassifier(n_estimators=10, min_samples_leaf=20, min_samples_split=20,
                                        max_features=None)] * k
# clf_rand_100_def = RandomForestClassifier()
# clf_rand_10_1 = RandomForestClassifier(n_estimators = 10, random_state=42, max_features=None)
# clf_rand_10_1 = RandomForestClassifier(n_estimators = 1, random_state=42, max_features=None, warm_start=True)
clf_rand_20_1 = [RandomForestClassifier(n_estimators=20, max_features=None)] * k
clf_rand_100_1 = [RandomForestClassifier(n_estimators=100, max_features=None)] * k

games = []
results = []

rows = []


def rows_extrac():
    with open(r'data/combine_data.csv', encoding="utf8", errors='ignore') as f:
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
        lst.append(float(row['h_shots_diff_h']))
        lst.append(float(row['h_shots_diff']))
        lst.append(float(row['h_shots_target_against']))
        lst.append(float(row['h_shots_target_against_h']))
        lst.append(float(row['h_shots_target_diff']))
        lst.append(float(row['h_shots_target_diff_h']))
        lst.append(float(row['h_red_cards']) / float(h_played))
        lst.append(float(row['h_red_cards_h']) / float(h_played_h))
        lst.append(float(row['h_red_cards_against']) / float(h_played))
        lst.append(float(row['h_red_cards_diff']))
        lst.append(float(row['h_red_cards_against_h']) / float(h_played_h))
        lst.append(float(row['h_red_cards_diff_h']))
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
        lst.append(float(row['a_shots_diff_a']))
        lst.append(float(row['a_shots_diff']))
        lst.append(float(row['a_shots_target_against']))
        lst.append(float(row['a_shots_target_against_a']))
        lst.append(float(row['a_shots_target_diff']))
        lst.append(float(row['a_shots_target_diff_a']))
        lst.append(float(row['a_red_cards']) / float(a_played))
        lst.append(float(row['a_red_cards_a']) / float(a_played_a))
        lst.append(float(row['a_red_cards_against']) / float(a_played))
        lst.append(float(row['a_red_cards_diff']))
        lst.append(float(row['a_red_cards_against_a']) / float(a_played_a))
        lst.append(float(row['a_red_cards_diff_a']))
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
        lst.append(round(np.random.random()))
        lst.append(round(np.random.random()*10))
        lst.append(round(np.random.random() * 100))
        lst.append(round(np.random.random() * 1000))
        lst.append(round(np.random.random() * 10000))
        lst.append(round(np.random.random() * 100000))

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


def normal_games():
    """global games
    max_feature = [0] * len(games[0])
    min_feature = [0] * len(games[0])
    for game in games:
        for i, feature in enumerate(game):
            max_feature[i] = max(max_feature[i], feature)
            min_feature[i] = min(min_feature[i], feature)
    for game in games:
        for i in range(len(game)):
            game[i] = (game[i] - min_feature[i]) / (max_feature[i] - min_feature[i])"""
    feature_distribut = [set() for k in range(108)]
    print(feature_distribut[0])
    for game in games:
        for i in range(len(game)):
            feature_distribut[i].add(game[i])
    #print(feature_distribut[0])
    print([len(f) for f in feature_distribut])





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
    lst.append(float(row['h_shots_diff_h']))
    lst.append(float(row['h_shots_diff']))
    lst.append(float(row['h_shots_target_against']))
    lst.append(float(row['h_shots_target_against_h']))
    lst.append(float(row['h_shots_target_diff']))
    lst.append(float(row['h_shots_target_diff_h']))
    lst.append(float(row['h_red_cards']) / float(h_played))
    lst.append(float(row['h_red_cards_h']) / float(h_played_h))
    lst.append(float(row['h_red_cards_against']) / float(h_played))
    lst.append(float(row['h_red_cards_diff']))
    lst.append(float(row['h_red_cards_against_h']) / float(h_played_h))
    lst.append(float(row['h_red_cards_diff_h']))
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
    lst.append(float(row['a_shots_diff_a']))
    lst.append(float(row['a_shots_diff']))
    lst.append(float(row['a_shots_target_against']))
    lst.append(float(row['a_shots_target_against_a']))
    lst.append(float(row['a_shots_target_diff']))
    lst.append(float(row['a_shots_target_diff_a']))
    lst.append(float(row['a_red_cards']) / float(a_played))
    lst.append(float(row['a_red_cards_a']) / float(a_played_a))
    lst.append(float(row['a_red_cards_against']) / float(a_played))
    lst.append(float(row['a_red_cards_diff']))
    lst.append(float(row['a_red_cards_against_a']) / float(a_played_a))
    lst.append(float(row['a_red_cards_diff_a']))
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


random_results = []


def calculate_odds_ratios(odd):
    a = 1 / odd[0] + 1 / odd[1] + 1 / odd[2]
    return (1 / odd[0]) / a, (1 / odd[1]) / a, (1 / odd[2]) / a


def check_odds(odds):
    return odds[0] <= 0 or odds[1] <= 0 or odds[2] <= 0


def oclide_distance(a, b):
    return sum([(i - j) ** 2 for i, j in zip(a, b)])


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


def play(clf, k):
    max_distance = 0
    avg = 0
    var = 0
    count = 0
    for i in range(18001, 25769, 2):
        # for i in range(len(rows)):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if row['home_odd'] == '':
            continue
        odds = odds_func(row)

        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0' or check_odds(odds):
            continue

        game_test = game_stats(row)
        prediction = [clf[j].predict_proba([game_test])[0] for j in range(k)]
        prediction_2 = average(prediction)
        odds_ratio = calculate_odds_ratios(odds)
        dist = oclide_distance(prediction_2, odds_ratio)
        max_distance = max(max_distance, dist)
        avg += dist
        var += dist ** 2
        count += 1
    avg /= count
    var = var / count - avg ** 2
    return max_distance, avg, var


def play_reg(clf):
    max_distance = 0
    avg = 0
    var = 0
    count = 0
    for i in range(18001, 25769, 2):
        # for i in range(len(rows)):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if row['home_odd'] == '':
            continue
        odds = odds_func(row)
        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0' or check_odds(odds):
            continue

        game_test = game_stats(row)
        home, draw, away = clf.calculate_prob_for_test_group([game_test])
        odds_ratio = calculate_odds_ratios(odds)
        dist = oclide_distance([home[0], draw[0], away[0]], odds_ratio)
        # print([home[0], draw[0], away[0]])
        # print(dist)
        max_distance = max(max_distance, dist)
        avg += dist
        var += dist ** 2
        count += 1
    avg /= count
    var = var / count - avg ** 2
    return max_distance, avg, var


def play_random():
    max_distance = 0
    avg = 0
    var = 0
    count = 0
    for i in range(18001, 25769, 2):
        # for i in range(len(rows)):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if row['home_odd'] == '':
            continue
        odds = odds_func(row)
        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0' or check_odds(odds):
            continue
        odds_ratio = calculate_odds_ratios(odds)
        dist = oclide_distance([1 / 3, 1 / 3, 1 / 3], odds_ratio)
        max_distance = max(max_distance, dist)
        avg += dist
        var += dist ** 2
        count += 1
    avg /= count
    var = var / count - avg ** 2
    return max_distance, avg, var


def play_random_2():
    max_distance = 0
    avg = 0
    var = 0
    count = 0
    for i in range(18001, 25769, 2):
        # for i in range(len(rows)):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if row['home_odd'] == '':
            continue
        odds = odds_func(row)
        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0' or check_odds(odds):
            continue
        odds_ratio = calculate_odds_ratios(odds)
        a = np.random.random()
        b = np.random.random() * (1 - a)
        dist = oclide_distance([a, b, 1 - a - b], odds_ratio)
        max_distance = max(max_distance, dist)
        avg += dist
        var += dist ** 2
        count += 1
    avg /= count
    var = var / count - avg ** 2
    return max_distance, avg, var


rows_extrac()
create_training_group()

# clf_reg_10.fit(games, results)
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
    101: 'a_last_5_games_failed / 5',
    102: 'random_1',
    103: 'random_10',
    104: 'random_100',
    105: 'random_1000',
    106: 'random_10000',
    107: 'random_100000'
}

normal_games()
clf_tree = RandomForestClassifier(n_estimators=10)
best_features = dict()
clf_tree.fit(games, results)
start = time.time()
result = permutation_importance(clf_tree, games, results, n_repeats=2000,
                                random_state=0)
print(time.time() - start)


best = result.importances_mean
#best = clf.feature_importances_
for i in range(len(features_dict)):
    best_features[features_dict[i]] = best[i]

sort_orders = sorted(best_features.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
    print(i[0], i[1])







clf_rand_100 = RandomForestClassifier()
# print("**************************************************")

# clf_logiReg = LogiReg.LogiRegSoccerGame(games, results)
# clf_linearReg = LinearReg.LinearRegSoccerGame(games, results)
# clf_multiReg = MultiReg.MultiRegSoccerGame(games, results)
# #
# # # for i in range(18001,21000):
# print("Logistic reg")
# print(play_reg(clf_logiReg))
# print("Linear reg")
# print(play_reg(clf_linearReg))
# print("Multi reg")
# print(play_reg(clf_multiReg))
#
# #print(games[0])
# normal_games()
# #print(games[0])
# best_features = dict()
# clf = tree.DecisionTreeClassifier(random_state=0)
# clf.fit(games, results)
#
# result = permutation_importance(clf, games, results, n_repeats=1000,
#                                 random_state=0)
# #print(result.importances_mean)
#
# best = result.importances_mean
# #best = clf.feature_importances_
# for i in range(len(features_dict)):
#     best_features[features_dict[i]] = best[i]
#
# sort_orders = sorted(best_features.items(), key=lambda x: x[1], reverse=True)
# for i in sort_orders:
#     print(i[0], i[1])
#
#
# print("##########################################################################")
#
# print("random_1/3")
# print(play_random())
# #
# print("random_random")
# print(play_random_2())
# print("**************************************************")
# clf = LogisticRegression().fit(games, results)
# rfe = RFE(estimator=clf, n_features_to_select=5)
# rfe.fit(games, results)
# chosen = rfe.get_support()
# selected = []
# k = 0
# for i in range(len(features_dict)):
#     if chosen[i]:
#         k += 1
#         print(k, features_dict[i])
#

# weigths = [{0.0:1, 1.0:1, 2.0:1}, {0.0:2.15865, 1.0:3.84336, 2.0:3.61584}]
#
# #normal_games()
# c = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# fit = [True, False]
# l1_ratio = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# penalty = ['l1', 'l2']
# # estimators_ada = list(range(10,101))
# params = {'c' : c, 'fit_intercept': fit,
#           'class_weight': weigths, 'penalty': penalty}
# params_list = list(ParameterGrid(params))
# best_params = dict()
#
#
#
# j = 0
# for comb in params_list:
#     clf = clf_linearReg = MultiReg.MultiRegSoccerGame(games, results, comb)
#     #clf.fit(games, results)
#     #clf.fit(best_features, results)
#     if comb['class_weight'] == {0.0: 1, 1.0: 1, 2.0: 1}:
#          is_weighted = 'umweighted'
#     else:
#          is_weighted = 'weighted'
#     params_tuple = (comb['c'], comb['fit_intercept'], comb['penalty'], is_weighted)
#     print(j)
#     print(params_tuple)
#     best_params[params_tuple] = play_reg(clf)
#     j += 1
#
#
# sort_orders = sorted(best_params.items(), key=lambda x: x[1][1], reverse=True)
# for i in sort_orders:
#       print(i[0], i[1])