import csv
from sklearn import tree
import numpy as np
import graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import LogiReg, LinearReg, MultiReg
import time

k = 1

clf_reg_10 = tree.DecisionTreeClassifier(min_samples_leaf=10, min_samples_split=10, random_state=42, max_features=None)
clf_rand_10_3 = [RandomForestClassifier(n_estimators=10, min_samples_leaf=20, min_samples_split=20,
                                        max_features=None)] * k
# clf_rand_100_def = RandomForestClassifier()
# clf_rand_10_1 = RandomForestClassifier(n_estimators = 10, random_state=42, max_features=None)
# clf_rand_10_1 = RandomForestClassifier(n_estimators = 1, random_state=42, max_features=None, warm_start=True)
clf_rand_20_1 = [RandomForestClassifier(n_estimators=20, max_features=None)] * k
clf_rand_100_1 = [RandomForestClassifier(n_estimators=100, max_features=None)] * k

import random

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
        lst.append(float(row['a_shots']) / float(h_played))
        lst.append(float(row['a_shots_a']) / float(h_played_h))
        lst.append(float(row['a_shots_against']) / float(h_played))
        lst.append(float(row['a_shots_against_a']) / float(h_played_h))
        lst.append(float(row['a_shots_target']) / float(h_played))
        lst.append(float(row['a_shots_target_a']) / float(h_played_h))
        lst.append(float(row['a_shots_diff_a']))
        lst.append(float(row['a_shots_diff']))
        lst.append(float(row['a_shots_target_against']))
        lst.append(float(row['a_shots_target_against_a']))
        lst.append(float(row['a_shots_target_diff']))
        lst.append(float(row['a_shots_target_diff_a']))
        lst.append(float(row['a_red_cards']) / float(h_played))
        lst.append(float(row['a_red_cards_a']) / float(h_played_h))
        lst.append(float(row['a_red_cards_against']) / float(h_played))
        lst.append(float(row['a_red_cards_diff']))
        lst.append(float(row['a_red_cards_against_a']) / float(h_played_h))
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
    lst.append(float(row['a_shots']) / float(h_played))
    lst.append(float(row['a_shots_a']) / float(h_played_h))
    lst.append(float(row['a_shots_against']) / float(h_played))
    lst.append(float(row['a_shots_against_a']) / float(h_played_h))
    lst.append(float(row['a_shots_target']) / float(h_played))
    lst.append(float(row['a_shots_target_a']) / float(h_played_h))
    lst.append(float(row['a_shots_diff_a']))
    lst.append(float(row['a_shots_diff']))
    lst.append(float(row['a_shots_target_against']))
    lst.append(float(row['a_shots_target_against_a']))
    lst.append(float(row['a_shots_target_diff']))
    lst.append(float(row['a_shots_target_diff_a']))
    lst.append(float(row['a_red_cards']) / float(h_played))
    lst.append(float(row['a_red_cards_a']) / float(h_played_h))
    lst.append(float(row['a_red_cards_against']) / float(h_played))
    lst.append(float(row['a_red_cards_diff']))
    lst.append(float(row['a_red_cards_against_a']) / float(h_played_h))
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


rows_extrac()
create_training_group()

for max_f in range(96):
    start = time.time()
    for i in range(k):
        #clf_reg_10.fit(games, results)
        clf_rand_10_3[i].max_features = max_f + 1
        #clf_rand_20_1[i].max_features = max_f + 1
        #clf_rand_100_1[i].max_features = max_f + 1

        clf_rand_10_3[i].fit(games, results)
        #clf_rand_20_1[i].fit(games, results)
        #clf_rand_100_1[i].fit(games, results)
    end = time.time()
    print("Fitting Forest with ***", max_f, "*** features per split  take:", (end-start)/60)
    #print("regular 10")
    #print(play(clf_reg_10))

    print("random 10_3")
    start = time.time()
    print(play(clf_rand_10_3, k))
    end = time.time()
    print("clf_rand_10_3 take:", (end-start)/60)

    """start = time.time()
    print("random 20_1")
    print(play(clf_rand_20_1, k))
    end = time.time()
    print("clf_rand_20_1 take:", (end-start)/60)

    start = time.time()
    print("random 100_1")
    print(play(clf_rand_100_1, k))
    end = time.time()
    print("clf_rand_100_1 take:", (end-start)/60)"""
    print("**************************************************")
"""
clf_logiReg = LogiReg.LogiRegSoccerGame(games, results)
clf_linearReg = LinearReg.LinearRegSoccerGame(games, results)
clf_multiReg = MultiReg.MultiRegSoccerGame(games, results)

# for i in range(18001,21000):
print("Logistic reg")
print(play_reg(clf_logiReg))
print("Linear reg")
print(play_reg(clf_linearReg))
print("Multi reg")
print(play_reg(clf_multiReg))
"""
print("random")
print(play_random())
