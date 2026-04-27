import numpy as np

def simulate(xg_h, xg_a):

    n = 30000

    res = {"H":0,"D":0,"A":0}

    for _ in range(n):

        gh = np.random.poisson(xg_h)
        ga = np.random.poisson(xg_a)

        if gh > ga:
            res["H"] += 1
        elif gh < ga:
            res["A"] += 1
        else:
            res["D"] += 1

    for k in res:
        res[k] /= n

    return res
