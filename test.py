import csv
from sklearn import tree
import numpy
import graphviz
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import RFE
from sklearn.model_selection import ParameterSampler
from sklearn.model_selection import ParameterGrid
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import LogiReg, LinearReg, MultiReg
import random
import copy
import utils
from itertools import product

games = []
results = []

rows = []



def rows_extrac():
    with open(r'C:\Users\Idan\PycharmProjects\project_ai\combine_data.csv', encoding="utf8") as f:
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
        lst.append(float(row['h_shots_diff_h'])/ float(h_played_h))
        lst.append(float(row['h_shots_diff'])/ float(h_played))
        lst.append(float(row['h_shots_target_against'])/ float(h_played))
        lst.append(float(row['h_shots_target_against_h'])/ float(h_played_h))
        lst.append(float(row['h_shots_target_diff'])/ float(h_played))
        lst.append(float(row['h_shots_target_diff_h'])/ float(h_played_h))
        lst.append(float(row['h_red_cards']) / float(h_played))
        lst.append(float(row['h_red_cards_h']) / float(h_played_h))
        lst.append(float(row['h_red_cards_against']) / float(h_played))
        lst.append(float(row['h_red_cards_diff'])/ float(h_played))
        lst.append(float(row['h_red_cards_against_h']) / float(h_played_h))
        lst.append(float(row['h_red_cards_diff_h'])/ float(h_played))
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
        lst.append(float(row['a_shots_diff_a'])/ float(a_played_a))
        lst.append(float(row['a_shots_diff'])/ float(a_played))
        lst.append(float(row['a_shots_target_against'])/ float(a_played_a))
        lst.append(float(row['a_shots_target_against_a'])/ float(a_played_a))
        lst.append(float(row['a_shots_target_diff'])/ float(a_played))
        lst.append(float(row['a_shots_target_diff_a'])/ float(a_played_a))
        lst.append(float(row['a_red_cards']) / float(a_played))
        lst.append(float(row['a_red_cards_a']) / float(a_played_a))
        lst.append(float(row['a_red_cards_against']) / float(a_played))
        lst.append(float(row['a_red_cards_diff'])/ float(a_played))
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
    lst.append(float(row['h_shots_diff'])/ float(h_played))
    lst.append(float(row['h_shots_target_against'])/ float(h_played))
    lst.append(float(row['h_shots_target_against_h']) / float(h_played_h))
    lst.append(float(row['h_shots_target_diff'])/ float(h_played))
    lst.append(float(row['h_shots_target_diff_h']) / float(h_played_h))
    lst.append(float(row['h_red_cards']) / float(h_played))
    lst.append(float(row['h_red_cards_h']) / float(h_played_h))
    lst.append(float(row['h_red_cards_against']) / float(h_played))
    lst.append(float(row['h_red_cards_diff'])/ float(h_played))
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
    lst.append(float(row['a_shots_diff_a'])/ float(a_played_a))
    lst.append(float(row['a_shots_diff'])/ float(a_played))
    lst.append(float(row['a_shots_target_against'])/ float(a_played))
    lst.append(float(row['a_shots_target_against_a'])/ float(a_played_a))
    lst.append(float(row['a_shots_target_diff'])/ float(a_played))
    lst.append(float(row['a_shots_target_diff_a'])/ float(a_played_a))
    lst.append(float(row['a_red_cards']) / float(a_played))
    lst.append(float(row['a_red_cards_a']) / float(a_played_a))
    lst.append(float(row['a_red_cards_against']) / float(a_played))
    lst.append(float(row['a_red_cards_diff'])/ float(a_played))
    lst.append(float(row['a_red_cards_against_a']) / float(a_played_a))
    lst.append(float(row['a_red_cards_diff_a'])/ float(a_played_a))
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
    #return random.choice(options)
    best = []
    if odds == (0.0,0.0,0.0):
        return None
    #return random.choice(options)
    #return 'DRAW'
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


rets = []

def ret_calc(odds):
    #print(odds)
    sum = 0.0
    for odd in odds:
        sum += (1/odd)
    return 1/sum

def normal_games():
    global max_feature
    global min_feature
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

max_feature = []
min_feature = []



rows_extrac()
create_training_group()
normal_games()
clf =tree.DecisionTreeClassifier()
rfe = RFE(estimator=clf, n_features_to_select=91)
rfe.fit(games, results)
best_features = rfe.transform(games)
#rfe = utils.choose_features_from_clusters(tree.DecisionTreeClassifier(), games, results, 1.0)
#best_features = utils.transform(games, rfe)

def play(clf):
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
        game_test = normal_single_games(game_test)
        game_test = rfe.transform([game_test])
     #   game_test = utils.transform([game_test], rfe)
        #prediction = clf.calculate_prob_for_test_group([game_test])
        #prediction = tuple(predict[0] for predict in prediction)
        prediction = clf.predict_proba(game_test)
        #prediction = clf.predict_proba([game_test])
        # predictions = [1 / result for result in prediction[0]]
        #bet_chosen = choose_bet(odds, prediction)
        bet_chosen = choose_bet(odds, prediction[0])
        if not bet_chosen:
            continue
        balance -= 1
        bets += 1
       # print("league =", row['league'])
       #print("date =", row['date'])
       # print("bet =", bet_chosen)
     #   print("odds: ", odds)
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
          #  print("win = ", winning)
        #print("balance = ", balance)
    # print(balance / len(rows))
 #   print("balance = ", balance)
   # print(balance / (len(rows) - 20000))
    print("number of bets = ", bets )
    print("number of wins =", wins)
    #print(balance / ((24800-18000)/2))
    print("return = ", balance / bets )
    return balance / bets


def play_reg(clf):
    #print("importance =", clf.feature_importances_)
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
        game_test = normal_single_games(game_test)
        game_test = rfe.transform([game_test])
        prediction = clf.calculate_prob_for_test_group([game_test])
        prediction = tuple(predict[0] for predict in prediction)
        bet_chosen = choose_bet(odds, prediction)
        if not bet_chosen:
            continue
        balance -= 1
        bets += 1
       # print("league =", row['league'])
       #print("date =", row['date'])
       # print("bet =", bet_chosen)
     #   print("odds: ", odds)
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
    print("number of bets = ", bets )
    print("number of wins =", wins)
    print("return = ", balance / bets )
    return balance / bets


def choose_bet_random(odds):
    options = ['HOME', 'DRAW', 'AWAY']
    #return random.choice(options)
    best = []
    if odds == (0.0,0.0,0.0):
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
        #if odds != (0.0,0.0,0.0):
            #print("ret = ", ret_calc(odds))
        game_test = game_stats(row)
        game_test = normal_single_games(game_test)
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
    print("number of bets = ", bets)
    print("number of wins =", wins)
    print("return = ", balance / bets)
   # print("normal balanced = ", balance / ((24800-18000)/2))
    return balance / bets


def choose_bet_specific(odds, string):
    if odds == (0.0,0.0,0.0):
        return None
    return string

def choose_bet_favourite(odds):
    if odds == (0.0,0.0,0.0):
        return None
    options = ['HOME', 'DRAW', 'AWAY']
    bet = min(odds)
    ind = odds.index(bet)
    return options[ind]

def choose_bet_underdog(odds):
    if odds == (0.0,0.0,0.0):
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
        #prediction = clf.predict_proba([game_test])
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
    for i in range(45000,59000,2):
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
        #prediction = clf.predict_proba([game_test])
        # predictions = [1 / result for result in prediction[0]]
        bet_chosen = choose_bet_underdog(odds)
        if not bet_chosen:
            continue
        bets +=1
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
    for i in range(45000,59000,2):
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
        #prediction = clf.predict_proba([game_test])
        # predictions = [1 / result for result in prediction[0]]
        bet_chosen = choose_bet_favourite(odds)
        if not bet_chosen:
            continue
        bets +=1
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


def normal_single_games(game):
    global max_feature
    global min_feature
    normal_game = copy.deepcopy(game)
    for i in range(len(normal_game)):
        normal_game[i] = (normal_game[i] - min_feature[i]) / (max_feature[i] - min_feature[i])
    return normal_game
#estimators = list(range(10,115,15))


features = ['h_won'
,'h_won_h'
,'h_drawn'
,'h_drawn_h'
,'h_lost'
,'h_lost_h'
,'h_points'
,'h_points_h'
,'h_scored'
,'h_scored_h'
,'h_conced'
,'h_conced_h'
,'h_clean'
,'h_clean_h'
,'h_fail'
,'h_fail_h'
,'h_goal_diff'
,'h_goal_diff_h'
,'h_shots'
,'h_shots_h'
,'h_shots_against'
,'h_shots_against_h'
,'h_shots_target'
,'h_shots_target_h'
,'h_shots_diff_h'
,'h_shots_diff'
,'h_shots_target_against'
,'h_shots_target_against_h'
,'h_shots_target_diff'
,'h_shots_target_diff_h'
,'h_red_cards'
,'h_red_cards_h'
,'h_red_cards_against'
,'h_red_cards_diff'
,'h_red_cards_against_h'
,'h_red_cards_diff_h'
,'h_elo'
,'h_fifa_rating'
,'h_current_win_streak'
,'h_current_no_lose_streak'
,'h_current_lose_streak'
,'h_current_no_win_streak'
,'h_last_5_games_points'
,'h_last_5_games_wins'
,'h_last_5_games_loss'
,'h_last_5_games_draw'
,'h_last_5_games_scored'
,'h_last_5_games_conced'
,'h_last_5_games_goal_diff'
,'h_last_5_games_clean'
,'h_last_5_games_failed'
,'a_won'
,'a_won_a'
,'a_drawn'
,'a_drawn_a'
,'a_lost'
,'a_lost_a'
,'a_points'
,'a_points_a'
,'a_scored'
,'a_scored_a'
,'a_conced'
,'a_conced_a'
,'a_clean'
,'a_clean_a'
,'a_fail'
,'a_fail_a'
,'a_goal_diff'
,'a_goal_diff_a'
,'a_shots'
,'a_shots_a'
,'a_shots_against'
,'a_shots_against_a'
,'a_shots_target'
,'a_shots_target_a'
,'a_shots_diff_a'
,'a_shots_diff'
,'a_shots_target_against'
,'a_shots_target_against_a'
,'a_shots_target_diff'
,'a_shots_target_diff_a'
,'a_red_cards'
,'a_red_cards_a'
,'a_red_cards_against'
,'a_red_cards_diff'
,'a_red_cards_against_a'
,'a_red_cards_diff_a'
,'a_elo'
,'a_fifa_rating'
,'a_current_win_streak'
,'a_current_no_lose_streak'
,'a_current_lose_streak'
,'a_current_no_win_streak'
,'a_last_5_games_points'
,'a_last_5_games_wins'
,'a_last_5_games_loss'
,'a_last_5_games_draw'
,'a_last_5_games_scored'
,'a_last_5_games_conced'
,'a_last_5_games_goal_diff'
,'a_last_5_games_clean'
,'a_last_5_games_failed']

estimators = list(range(10,150))
min_samples_leaf_lst = list(range(3,51))
max_depth = [None] + list(range(10,41))
criteria = ['gini', 'entropy']
weigths = [{0.0:2.15865, 1.0:3.84336, 2.0:3.61584}]
max_features = ['sqrt', 'log2']
profits = dict()

params = {'min_samples_leaf' : min_samples_leaf_lst,
          #'min_samples_split' : min_samples_leaf_lst,
          'criterion' : criteria, 'class_weight' : weigths, 'max_depth' : max_depth,
          'max_features' : max_features, 'n_estimators' : estimators}
params_list = list(ParameterSampler(params, 500))
best_params = dict()

j = 0
for comb in params_list:
    clf = ExtraTreesClassifier(min_samples_leaf = comb['min_samples_leaf'], min_samples_split=comb['min_samples_leaf'],
    max_depth = comb['max_depth'], criterion= comb['criterion'], class_weight= comb['class_weight'],
                                 max_features=comb['max_features'], n_estimators=comb['n_estimators'],
                                      random_state=42, bootstrap=False)
    #clf.fit(games, results)
    clf.fit(best_features, results)
    if comb['class_weight']  == {0.0:1, 1.0:1, 2.0:1}:
        is_weighted = 'umweighted'
    else:
        is_weighted = 'weighted'
    params_tuple = (comb['n_estimators'],
                    comb['min_samples_leaf'], comb['max_depth'], comb['criterion'], is_weighted, comb['max_features'] )
    print(j)
    print(params_tuple)
    best_params[params_tuple] = play(clf)
    j += 1


sort_orders = sorted(best_params.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
      print(i[0], i[1])

# clf_logiReg = LogiReg.LogiRegSoccerGame(games, results)
# clf.fit(games, results)
#clf_linearReg = LinearReg.LinearRegSoccerGame(games, results)
#clf_multiReg = MultiReg.MultiRegSoccerGame(games, results)
# print("Logistic reg")
# print(play_reg(clf_logiReg))
#print("Linear reg")
#print(play_reg(clf_linearReg))
#print("Multi reg")
#print(play_reg(clf_multiReg))
# random_results = []
# for i in range(1000):
#      random_results.append(play_random())
# print((sum(random_results)) / (len(random_results)) )