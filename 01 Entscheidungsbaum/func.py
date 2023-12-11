# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 07:47:17 2023

@author: Julian Schumacher
"""

import numpy as np


def detectDecisions():
    weekend = np.genfromtxt("weekend.csv", delimiter=",", dtype=str)
    gini_complete = []
    file : list[list[str]] = weekend.reshape(-1, 4)
    for i in range(0, len(file[0]) - 1):
        decisionsForCondition = file[1:, i]  # Create List containing all the different possibilities (possibly multiple times)
        differentPossibilitiesSet = set(decisionsForCondition) # Create List which only contains unique values
        differentPossibilities = list(differentPossibilitiesSet)
        for j in range(0, len(differentPossibilities)):
            giniForPossibility = calGiniForCon(file[0][i], differentPossibilities[j], file)
            gini_complete.append(giniForPossibility)
    giniGesamt = 1 - sum(gini_complete)
    print(f'Gini Koeffizient gesamt: {giniGesamt}')


def calGiniForCon(heading: str, value: str, file: list[list[str]]):
    listToIndex : list[str] = list(file[0]) # Get Header Row
    index : int = listToIndex.index(heading) # Get Index of Decision to respect
    occurencesOfCon : int = 0
    for i in range(1, len(file)):
        if file[i][index] == value : occurencesOfCon += 1
    giniForCon = 1 - (occurencesOfCon / len(file) - 1)**2
    print(f'Gini Koeffizient für {heading} mit Wert {value}: {giniForCon}')
    return giniForCon