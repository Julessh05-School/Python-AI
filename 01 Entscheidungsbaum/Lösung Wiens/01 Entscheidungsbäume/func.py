import numpy as np


def gini(decisionCount, decisionAll) -> int:
    decisionUnique = np.size(decisionCount)
    summe = 0
    for i in range(decisionUnique):
        summe = summe + (decisionCount[i] / (decisionAll)) ** 2
    return 1 - summe
