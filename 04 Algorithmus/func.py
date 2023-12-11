import math

import numpy as np
import matplotlib.pyplot as plt

#
# 1D Plotting
#


def plotten_1d():
    # Generierung von Beispiel Daten
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
    data_len = len(data)

    # Generierung von Initial Zentren
    center = np.array([10, 20])
    show_1d_plot(data, center)

    # Zuordnung der Datenpunkte zu den Zentren
    label = data * 0

    for _ in range(3):
        sum1 = 0
        sum2 = 0
        count1 = 0
        count2 = 0
        diff1 = abs(data - center[0])
        diff2 = abs(data - center[1])

        for j in range(data_len):
            if diff1[j] < diff2[j]:
                label[j] = 1
                sum1 += data[j]
                count1 += 1
            else:
                label[j] = 2
                sum2 += data[j]
                count2 += 1

        center[0] = sum1 / count1
        center[1] = sum2 / count2
        show_1d_plot(data, center)


def show_1d_plot(data: [int], center: [int]):
    plt.scatter(data, data * 0)  # Daten
    plt.scatter(center, center * 0, c='red', s=200)  # Zentren
    plt.title('1D K-MEANS Clustering')
    plt.show()


#
# 2D Plotting
#


def plotten_2d():
    data: [[int]] = []
    data_x: [int] = []
    data_y: [int] = []
    center: [[int]] = [[10, 10], [20, 20]]
    for i in range(100):
        data_x.append(np.random.normal(10, 50, 1))
        data_y.append(np.random.normal(10, 50, 1))
        data.append([data_x[i - 1], data_y[i - 1]])

    for _ in range(10):
        for j in range(len(data)):
            diff_1_x: float = abs(data[j][0] - center[0][0])
            diff_1_y: float = abs(data[j][1] - center[0][1])
            diff_2_x: float = abs(data[j][0] - center[1][0])
            diff_2_y: float = abs(data[j][1] - center[1][1])
            # Diff 1 Calculation
            diff_1: float = math.sqrt(math.pow(diff_1_x, 2) + math.pow(diff_1_y, 2))
            # Diff 2 Calculation
            diff_2: float = math.sqrt(math.pow(diff_2_x, 2) + math.pow(diff_2_y, 2))

    show_2d_plot(data, center)


def show_2d_plot(data: [[int]], center: [[int]]):
    for i in range(len(data)):
        plt.plot(data[i][0], data[i][1], '*', c='blue')

    for i in range(len(center)):
        plt.plot(center[i][0], center[i][0], 'x', c='red')
    plt.title('2D K-MEANS Clustering')
    plt.show()