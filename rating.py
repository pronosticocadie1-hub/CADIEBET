from collections import defaultdict

def update_ratings(df):

    ratings = defaultdict(lambda: 1500)

    for _, r in df.iterrows():

        h, a = r["home"], r["away"]

        if r["gh"] > r["ga"]:
            s_h, s_a = 1, 0
        elif r["gh"] < r["ga"]:
            s_h, s_a = 0, 1
        else:
            s_h, s_a = 0.5, 0.5

        exp_h = 1 / (1 + 10 ** ((ratings[a] - ratings[h]) / 400))

        ratings[h] += 20 * (s_h - exp_h)
        ratings[a] += 20 * (s_a - (1 - exp_h))

    return ratings
