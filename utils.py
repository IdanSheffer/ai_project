from collections import defaultdict

from scipy.cluster import hierarchy
from scipy.stats import spearmanr


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
    for r in range(len(cluster_id_to_feature_ids)):
        i = r + 1
        a = [(importance[k], k) for k in cluster_id_to_feature_ids[i]]
        a = sorted(a, key=lambda x: x[0], reverse=True)
        cluster_id_to_feature_ids[i] = [k[1] for k in a]
        for j, f in enumerate(cluster_id_to_feature_ids[i]):
            if j > len(cluster_id_to_feature_ids[i]) * fraction:
                break
            selected_features.append(f)
    return selected_features


def transform(X, sel):
    new_X = [[row[f] for f in range(len(row)) if f in sel] for row in X]
    return new_X
