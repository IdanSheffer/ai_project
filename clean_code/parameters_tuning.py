
# For each classifier the code print a list of combinations of parameters sorted according to the profit
# You have to copy the relevant code to the end of clean_code.py file


# Parameters for simple tree

min_samples_leaf_lst = list(range(3, 51))
max_depth = [None] + list(range(10, 41))
criteria = ['gini', 'entropy']
weigths = [{0.0: 2.15865, 1.0: 3.84336, 2.0: 3.61584}]
max_features = ['sqrt', 'log2']
profits = dict()
params = {'min_samples_leaf': min_samples_leaf_lst,
          'criterion': criteria, 'class_weight': weigths, 'max_depth': max_depth,
          'max_features': max_features}
params_list = list(ParameterSampler(params, 500))
best_params = dict()

j = 0
for comb in params_list:
    clf = tree.DecisionTreeClassifier(min_samples_leaf=comb['min_samples_leaf'],
                                           min_samples_split=comb['min_samples_leaf'],
                                           max_depth=comb['max_depth'],
                                           criterion='entropy',
                                           class_weight=weigths[0], random_state=42)
    clf.fit(best_features, results)
    params_tuple = (comb['n_estimators'],
                    comb['min_samples_leaf'], comb['max_depth'], comb['criterion'], comb['max_features'] )
    best_params[params_tuple] = play(clf)
    j += 1


sort_orders = sorted(best_params.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
      print(i[0], i[1])



# Parameters for random forest
estimators = list(range(10, 150))
min_samples_leaf_lst = list(range(3, 51))
max_depth = [None] + list(range(10, 41))
criteria = ['gini', 'entropy']
weigths = [{0.0: 2.15865, 1.0: 3.84336, 2.0: 3.61584}]
max_features = ['sqrt', 'log2']
profits = dict()

params = {'min_samples_leaf': min_samples_leaf_lst,
          'criterion': criteria, 'class_weight': weigths, 'max_depth': max_depth,
          'max_features': max_features, 'n_estimators': estimators}
params_list = list(ParameterSampler(params, 500))
best_params = dict()

j = 0
for comb in params_list:
    clf = RandomForestClassifier(n_estimators=params['n_estimators'], min_samples_leaf=comb['min_samples_leaf'],
                                           min_samples_split=comb['min_samples_leaf'],
                                           max_depth=comb['max_depth'],
                                           criterion='entropy',
                                           class_weight=weigths[0], random_state=42)
    clf.fit(best_features, results)
    params_tuple = (comb['n_estimators'],
                    comb['min_samples_leaf'], comb['max_depth'], comb['criterion'], comb['max_features'])
    best_params[params_tuple] = play(clf)
    j += 1


sort_orders = sorted(best_params.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
      print(i[0], i[1])


# Parameters for extra forest
estimators = list(range(10, 150))
min_samples_leaf_lst = list(range(3, 51))
max_depth = [None] + list(range(10, 41))
criteria = ['gini', 'entropy']
weigths = [{0.0: 2.15865, 1.0: 3.84336, 2.0: 3.61584}]
max_features = ['sqrt', 'log2']
profits = dict()

params = {'min_samples_leaf': min_samples_leaf_lst,
          # 'min_samples_split' : min_samples_leaf_lst,
          'criterion': criteria, 'class_weight': weigths, 'max_depth': max_depth,
          'max_features': max_features, 'n_estimators': estimators}
params_list = list(ParameterSampler(params, 1000))
best_params = dict()

j = 0
for comb in params_list:
    clf = RandomForestClassifier(min_samples_leaf=comb['min_samples_leaf'], min_samples_split=comb['min_samples_leaf'],
                                 max_depth=comb['max_depth'], criterion=comb['criterion'],
                                 class_weight=comb['class_weight'],
                                 max_features=comb['max_features'], n_estimators=comb['n_estimators'],
                                 random_state=42, bootstrap=True)
    # clf.fit(games, results)
    clf.fit(best_features, results)
    if comb['class_weight'] == {0.0: 1, 1.0: 1, 2.0: 1}:
        is_weighted = 'umweighted'
    else:
        is_weighted = 'weighted'
    params_tuple = (comb['n_estimators'],
                    comb['min_samples_leaf'], comb['max_depth'], comb['criterion'], is_weighted, comb['max_features'])
    best_params[params_tuple] = play(clf)
    j += 1

sort_orders = sorted(best_params.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
      print(i[0], i[1])
# Parameters for gradiant Zero, None, tree

estimators = list(range(10,100, 10))
min_samples_leaf_lst = list(range(3,51))
max_depth = [None] + list(range(10,41))
learning_rate = [0.02, 0.04, 0.06, 0.08, 0.1]
subsample = (0.5, 0.75, 1.0)
max_features = ['log2']
profits = dict()

params = {'learning_rate': learning_rate, 'n_estimators' : estimators, 'subsample': subsample, 'max_depth': max_depth,
          'max_features' : max_features, 'min_samples_leaf' : min_samples_leaf_lst}
params_list = list(ParameterSampler(params, 500))
best_params = dict()

j = 0
for comb in params_list:
    params_tuple = (comb['n_estimators'],
                    comb['min_samples_leaf'], comb['max_depth'], comb['learning_rate'],
                    comb['subsample'], comb['max_features'])
    print(j)
    print(params_tuple)
    j += 1
    # This is the best tree found with 54 features
    clf_tree = tree.DecisionTreeClassifier(random_state=42, min_samples_leaf=6, min_samples_split=6, max_depth=12,
                                       criterion='entropy', class_weight=weigths[0])

    clf_zero =GradientBoostingClassifier(min_samples_leaf=comb['min_samples_leaf'],
                                    min_samples_split=comb['min_samples_leaf'],
                                    max_depth=comb['max_depth'],
                                    max_features=comb['max_features'], n_estimators=comb['n_estimators'],
                                    learning_rate=comb['learning_rate'], subsample=comb['subsample'],
                                      random_state=42, init='zero')
    clf_none = GradientBoostingClassifier(min_samples_leaf=comb['min_samples_leaf'],
                                     min_samples_split=comb['min_samples_leaf'],
                                     max_depth=comb['max_depth'], max_features=comb['max_features'],
                                     n_estimators=comb['n_estimators'],
                                     learning_rate=comb['learning_rate'], subsample=comb['subsample'],
                                     random_state=42, init=None)
    clf_tree = GradientBoostingClassifier(min_samples_leaf=comb['min_samples_leaf'],
                                     min_samples_split=comb['min_samples_leaf'],
                                     max_depth=comb['max_depth'], max_features=comb['max_features'],
                                     n_estimators=comb['n_estimators'],
                                     learning_rate=comb['learning_rate'], subsample=comb['subsample'],
                                     random_state=42, init=clf_tree)
    clf.fit(best_features, results)
    best_params[params_tuple] = play(clf)

sort_orders = sorted(best_params.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
      print(i[0], i[1])

# Parameters for simple elastic net

# Parameters for simple Ridge

alpha = np.linspace(0.1, 1.5, 15)
fit = [True, False]
norm = [True, False]
l1 = np.linspace(0.1, 1.5, 15)
solver = ['sparse_cg', 'cholesky', 'svd', 'lsqr', 'sag', 'saga']
params = {'alpha': alpha, 'fit_intercept': fit, 'norm': norm, 'l1': l1}
params_list = list(ParameterGrid(params))
best_params = dict()

j = 0
for comb in params_list:
    clf = clf_linearReg = Ridge()(best_features_54, results, comb)

    params_tuple = (comb['alpha'], comb['l1'], comb['fit_intercept'], comb['norm'])
    print(j)
    print(params_tuple)
    best_params[params_tuple] = play_reg(clf, rfe_54)
    j += 1

sort_orders = sorted(best_params.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
    print(i[0], i[1])


# Parameters for linear regression
fit = [True, False]
norm = [True, False]

params = {'alpha': alpha, 'fit_intercept': fit, 'norm': norm, 'l1': l1}
params_list = list(ParameterGrid(params))
best_params = dict()

j = 0
for comb in params_list:
    clf = clf_linearReg = LinearReg.LinearRegSoccerGame(best_features_54, results, comb)

    params_tuple = (comb['alpha'], comb['l1'], comb['fit_intercept'], comb['norm'])
    print(j)
    print(params_tuple)
    best_params[params_tuple] = play_reg(clf, rfe_54)
    j += 1

sort_orders = sorted(best_params.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
    print(i[0], i[1])


# Parameters for multi regression lbfgs
# Parameters for multi regression liblinear
# Parameters for multi regression newton-cg
# Parameters for multi regression sag
# Parameters for multi regression saga

# Parameters for logistic regression lbfgs
# Parameters for logistic regression liblinear
# Parameters for logistic regression newton-cg
# Parameters for logistic regression sag
# Parameters for logistic regression saga

