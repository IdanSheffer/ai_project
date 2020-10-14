import csv
from sklearn import tree
import numpy
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import RFE
from sklearn.model_selection import ParameterSampler
from sklearn.model_selection import ParameterGrid
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import LogiReg, LinearReg, MultiReg
import random
import copy
from itertools import product

games = []
results = []

rows = []


# The function get the data from the file: combine_data.csv
# Add the path on your machine
def rows_extrac():
    with open(r'new_combine_data.csv', encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

# The function crate the training group
# It takes the first 18000 games, except to games in the start of season
# The traiמing group  features will be available in 'games' global variable
# The classification will be available in 'result' global variable

def create_training_group():
    global games, results
    games = []
    results = []
    i = 2
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


# The function get the odds betting for specific game
def odds_func(row):
    home_odds = float(row['home_odd'])
    draw_odds = float(row['draw_odd'])
    away_odds = float(row['away_odd'])
    return home_odds, draw_odds, away_odds

# The function get the features for specific game
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

    return lst

# The function calculate the most lucrative betting according to the precents we get from the classifier

def choose_bet(odds, predict):
    options = ['HOME', 'DRAW', 'AWAY']
    best = []
    if odds == (0.0,0.0,0.0):
        return None
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

# The function check if the selected bet match the game result
def bet(row, bet_chosen):
    return bet_chosen == row['RESULT']

# The function return the profit of good bet
def win(odds, choice):
    if choice == 'HOME':
        return odds[0]
    if choice == 'DRAW':
        return odds[1]
    if choice == 'AWAY':
        return odds[2]


rets = []

def ret_calc(odds):

    sum = 0.0
    for odd in odds:
        sum += (1/odd)
    return 1/sum

# The function normalize the features according to the training group

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

# clf for the RFE features selection
# For tree-based algorithms use the DecisionTreeClassifier
# For Regressions use the LinearRegression()
clf = tree.DecisionTreeClassifier(random_state=42)
#clf = LinearRegression()


# Number of all features in the first features method of presentation is: 102
num_of_features = '102'
# The options are: 102 ,91, 76, 51, 25

rfe = RFE(estimator=clf, n_features_to_select=102)
if num_of_features == '102':
    rfe = RFE(estimator=clf, n_features_to_select=102)
elif num_of_features == '91':
    rfe = RFE(estimator=clf, n_features_to_select=91)
elif num_of_features == '76':
    rfe = RFE(estimator=clf, n_features_to_select=76)
elif num_of_features == '51':
    rfe = RFE(estimator=clf, n_features_to_select=51)
elif num_of_features == '25':
    rfe = RFE(estimator=clf, n_features_to_select=25)


rfe.fit(games, results)
best_features = rfe.transform(games)

# The function get tree-based classifier and play on the validation group
# Use for parameters tuning
# It return the total profit
# It print the number of correct guesses

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
        prediction = clf.predict_proba(game_test)
        bet_chosen = choose_bet(odds, prediction[0])
        if not bet_chosen:
            continue
        balance -= 1
        bets += 1
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
    print("number of bets = ", bets )
    print("number of wins =", wins)
    print("return = ", balance / bets )
    return balance / bets

# The function get regression-based classifier and play on the validation group
# Use for parameters tuning
# It return the total profit
# It print the number of correct guesses

def play_reg(clf):
    balance = 0.0
    bets = 0
    wins = 0
    for i in range(18001, 25769, 2):
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
        game_test = normal_single_games(game_test)
        game_test = rfe.transform([game_test])
        prediction = clf.calculate_prob_for_test_group([game_test])
        prediction = tuple(predict[0] for predict in prediction)
        bet_chosen = choose_bet(odds, prediction)
        if not bet_chosen:
            continue
        balance -= 1
        bets += 1
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
    print("number of bets = ", bets )
    print("number of wins =", wins)
    print("return = ", balance / bets )
    return balance / bets

# The function choose random bet for random play

def choose_bet_random(odds):
    options = ['HOME', 'DRAW', 'AWAY']
    if odds == (0.0,0.0,0.0):
        return None
    return random.choice(options)



# The function get tree-based classifier and play random on the validation group/test group (start from 18001,
# start from 18000) respectively
# Use for estimate the average loss for "Stupid gambler"
# It return the total profit (Negative useally)
# It print the number of correct guesses

def play_random():
    balance = 0.0
    bets = 0
    wins = 0
    for i in range(18001, 25769, 2):
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
        bet_chosen = choose_bet_random(odds)
        if not bet_chosen:
            continue
        balance -= 1
        bets += 1
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
    print("number of bets = ", bets)
    print("number of wins =", wins)
    print("return = ", balance / bets)
    return balance / bets


def choose_bet_specific(odds, string):
    if odds == (0.0,0.0,0.0):
        return None
    return string

# The function choose the favorite result according to the odds of the game
def choose_bet_favourite(odds):
    if odds == (0.0,0.0,0.0):
        return None
    options = ['HOME', 'DRAW', 'AWAY']
    bet = min(odds)
    ind = odds.index(bet)
    return options[ind]


# The function choose the unlikely result according to the odds of the game
def choose_bet_underdog(odds):
    if odds == (0.0,0.0,0.0):
        return None
    options = ['HOME', 'DRAW', 'AWAY']
    bet = max(odds)
    ind = odds.index(bet)
    return options[ind]

# The function get tree-based classifier and play on the validation group/test group
# (start from 18001, start from 18000) respectively
# Use for estimate the average loss for "Stupid gambler"
# It return the total profit (Negative useally)
# It print the number of correct guesses

def play_specific(string):
    balance = 0.0
    for i in range(18001, 25769, 2):
        row = rows[i]
        h_played = row['h_played']
        h_played_h = row['h_played_h']
        a_played = row['a_played']
        a_played_a = row['a_played_a']
        if a_played == '0' or h_played == '0' or h_played_h == '0' or a_played_a == '0':
            continue
        odds = odds_func(row)
        bet_chosen = choose_bet_specific(odds, string)
        if not bet_chosen:
            continue
        balance -= 1
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
    print("number of bets = ", bets)
    print("number of wins =", wins)
    print("return = ", balance / bets)
    return balance / (len(rows) - 20000)

# The function get tree-based classifier and play on the validation group/test group
# (start from 18001, start from 18000) respectively
# Use for estimate the average loss for betting on the unlikely result
# It return the total profit (Negative useally)
# It print the number of correct guesses

def play_underdog():
    bets = 0
    wins = 0
    balance = 0.0
    for i in range(18001, 25769, 2):

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
        bet_chosen = choose_bet_underdog(odds)
        if not bet_chosen:
            continue
        bets +=1
        balance -= 1
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
    print("number of bets = ", bets)
    print("number of wins = ", wins)
    return (balance / bets)

def play_favourite():
    bets = 0
    wins = 0
    balance = 0.0
    for i in range(18001, 25769, 2):
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
        bet_chosen = choose_bet_favourite(odds)
        if not bet_chosen:
            continue
        bets +=1
        balance -= 1
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
    print("number of bets = ", bets)
    print("number of wins = ", wins)
    return (balance / bets)


# This function normalize a single game of the validation group /test group
def normal_single_games(game):
    global max_feature
    global min_feature
    normal_game = copy.deepcopy(game)
    for i in range(len(normal_game)):
        normal_game[i] = (normal_game[i] - min_feature[i]) / (max_feature[i] - min_feature[i])
    return normal_game


# The function get tree-based classifier and play on the test group
# Use for parameters tuning
# It return the total profit
# It print the number of correct guesses

def play_test(clf):
    balance = 0.0
    bets = 0
    wins = 0
    x = []
    y = []
    for i in range(18000, 25769, 2):
        if i == 18394:
            continue
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
        prediction = clf.predict_proba(game_test)
        bet_chosen = choose_bet(odds, prediction[0])
        if not bet_chosen:
            continue
        balance -= 1
        bets += 1
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
        x.append(bets)
        y.append(balance / bets)
    print("number of bets = ", bets)
    print("number of wins =", wins)
    print("return = ", balance / bets)
    return balance / bets, x, y

# The function get regression-based classifier and play on the test group
# Use for parameters tuning
# It return the total profit
# It print the number of correct guesses

def play_reg_test(clf):
    balance = 0.0
    bets = 0
    wins = 0
    for i in range(18000, 25769, 2):
        if i == 18394:
            continue
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
        game_test = normal_single_games(game_test)
        game_test = rfe.transform([game_test])
        prediction = clf.calculate_prob_for_test_group(game_test)
        prediction = tuple(predict[0] for predict in prediction)
        bet_chosen = choose_bet(odds, prediction)
        if not bet_chosen:
            continue
        balance -= 1
        bets += 1
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
            wins += 1
    print("number of bets = ", bets)
    print("number of wins =", wins)
    print("return = ", balance / bets)
    return balance / bets



weigths = {0.0:2.15865, 1.0:3.84336, 2.0:3.61584}
