# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:45:38 2023

@author: Julian Schumacher
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_print(w_input):
    plt.plot(Class1[:, 1], Class1[:, 2], '*')
    plt.plot(Class2[:, 1], Class2[:, 2], 'o')
    x = np.linspace(-5, 5, 2)
    y = (-(w_input[0] + w_input[1] * x) / w_input[2])
    plt.plot(x, y)
    plt.show()
    print('Epochen:', epoch, 'Iteration:', iteration, 'Gewichte:', w_input)


alpha = 0
lernrate = 1
error = 1
iteration = 0  # Anzahl der Trainingsdurchläufe
epoch = 0  # Anzahl der Durchläufe mit dem gesamten Datensatz
w = np.array((1, 1, 1))
Class1 = np.array([[1, 2.5, 10.2], [1, 3.1, 16.3], [1, -0.5, 2.9], [1, -2.5, -3.4]])
Class2 = np.array([[1, 0.5, -3.9], [1, 1.6, -17.8], [1, 4.5, -1.9], [1, -0.2, -11.2]])
DataClass1 = np.size(Class1, 0)
DataClass2 = np.size(Class2, 0)
plot_print(w)

while error > 0:
    error = 0
    epoch += 1
    iteration = 0
    for i in range(DataClass1):
        Output = np.dot(Class1[i,], w)
        if Output <= alpha:
            w = w + lernrate * Class1[i,]
            error = error + 1
            iteration = iteration + 1
            plot_print(w)

    for i in range(DataClass2):
        Output = np.dot(Class2[i,], w)
        if Output > alpha:
            w = w - lernrate * Class2[i,]
            error = error + 1
            iteration = iteration + 1
            plot_print(w)
