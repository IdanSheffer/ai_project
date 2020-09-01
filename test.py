import csv
from sklearn import tree
import numpy
import graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
#clf_rand_10_3 = RandomForestClassifier(n_estimators = 10, min_samples_leaf = 3, min_samples_split=3,
#                                  random_state=42, max_features=None)
#clf_rand_100_def = RandomForestClassifier()
#clf_rand_10_1 = RandomForestClassifier(n_estimators = 10, random_state=42, max_features=None)
#clf_rand_10_1 = RandomForestClassifier(n_estimators = 1, random_state=42, max_features=None, warm_start=True)
#clf_rand_20_1 = RandomForestClassifier(n_estimators=20, random_state=42, max_features=None )
#clf_rand_100_1 = RandomForestClassifier(n_estimators=100, random_state=42, max_features=None)

import random
from itertools import product

games = []
results = []

rows = []

def rows_extrac():
    with open(r'C:\Users\Idan\PycharmProjects\project_ai\Soccer_Data.csv', encoding="utf8") as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            rows.append(row)
            if (float(row['home_odd']) < 0.0) or (float(row['draw_odd']) <0.0) or (float(row['away_odd']) < 0.0):
                counter +=1
        #print("kaki")

def create_training_group():
    global games, results
    games = []
    results = []
    i = 2
    #random.shuffle(rows)
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
        lst.append(float(row['h_clean']) / 100)
        lst.append(float(row['h_clean_h']) / 100)
        lst.append(float(row['h_fail']) / 100)
        lst.append(float(row['h_fail_h']) / 100)

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
        lst.append(float(row['a_clean']) / 100)
        lst.append(float(row['a_clean_a']) / 100)
        lst.append(float(row['a_fail']) / 100)
        lst.append(float(row['a_fail_a']) / 100)
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
    lst.append(float(row['h_clean']) / 100)
    lst.append(float(row['h_clean_h']) / 100)
    lst.append(float(row['h_fail']) / 100)
    lst.append(float(row['h_fail_h']) / 100)

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
    lst.append(float(row['a_clean']) / 100)
    lst.append(float(row['a_clean_a']) / 100)
    lst.append(float(row['a_fail']) / 100)
    lst.append(float(row['a_fail_a']) / 100)
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


random_results = []

def play(clf):
    #print("importance =", clf.feature_importances_)
  #  global row, game_test
    balance = 0.0
    bets = 0
    wins = 0
    for i in range(18000, 24800, 2):
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
        prediction = clf.predict_proba([game_test])
        # predictions = [1 / result for result in prediction[0]]
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
   # print("balance = ", balance)
   # print(balance / (len(rows) - 20000))
    print("number of bets = ", bets )
    print("number of wins =", wins)
    print(balance / ((24800-18000)/2))
    return (balance / ((24800-18000)/2))


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
        bet_chosen = choose_bet_random(odds)
        if not bet_chosen:
            continue
        balance -= 1
        if bet(row, bet_chosen):
            winning = win(odds, bet_chosen)
            balance += winning
         #   print("win = ", winning)
       # print("balance = ", balance)
    # print(balance / len(rows))
    #print("balance = ", balance)
   # print(balance / (len(rows) - 20000))
    return balance / (len(rows) - 20000)


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
        bet_chosen = choose_bet_underdog(odds)
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

def play_favourite():
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
        bet_chosen = choose_bet_favourite(odds)
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


#random_profits = []
# home_profits = []
# draw_profits = []
# away_profits = []
# favour_profits = []
# underdog_profits = []


estimators = list(range(10,21)) + list(range(20,110,10))
min_samples_leaf_lst = list(range(1,11))
max_depth = list(range(10,28, 2)) + [None]
criteria = ['gini', 'entropy']
max_features = [None, 'sqrt']
profits = dict()





rows_extrac()
create_training_group()
for i in product(min_samples_leaf_lst, max_depth, criteria, max_features, estimators):
    print(i)
   # clf_reg = RandomForestClassifier()
   # clf_reg.fit(games, results)
    if i[0] != 1:
        clf_reg = RandomForestClassifier(n_estimators=i[4], min_samples_leaf=i[0], min_samples_split=i[0],
                                         random_state=42, max_depth=i[1], criterion=i[2], max_features=i[3])
    else:
        clf_reg = RandomForestClassifier(n_estimators= i[4], random_state=42,
        max_depth= i[1], criterion=i[2], max_features = i[3])
    clf_reg.fit(games, results)
    params = tuple(i)
    profits[params] = play(clf_reg)
sort_orders = sorted(profits.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
    print(i[0], i[1])


# rows_extrac()
# create_training_group()
# clf_reg_10.fit(games, results)
#clf_rand_10_3.fit(games, results)
#clf_rand_20_1.fit(games, results)
#clf_rand_100_1.fit(games, results)
#for i in range(18001,21000):
# print("regular 10")
# print(play(clf_reg_10))
# print("depth =", clf_reg_10.get_depth())
# print("random 10_3")
# print(play(clf_rand_10_3))
# print("random 20_1")
# print(play(clf_rand_20_1))
# print("random 100_1")
# print(play(clf_rand_100_1))
