# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:45:38 2023

@author: 400284
"""

import numpy as np
import matplotlib.pyplot as plt

def plotPrint(w):
    plt.plot(Class1[:,0], Class1[:,1], '*')
    plt.plot(Class2[:,0], Class2[:,1], 'o')
    x1 = np.linspace(-5, 5, 2)
    x2 = ((w[0] * x1) / -w[1])
    plt.plot(x1, x2)
    plt.show()
    print(w)
    
alpha = 0
lernrate = 1
error = 1
w = np.array((1, 1))
Class1 = np.array([[-2.5, 10.2], [3.1, 16.3], [-0.5, 2.9], [-2.5, -3.4]])
Class2 = np.array([[0.5, -3.9], [1.6, -17.8], [4.5, -1.9], [-0.2, -11.2]])
DataClass1 = np.size(Class1, 0)
DataClass2 = np.size(Class2, 0)
plotPrint(w)

while(error > 0):
    error = 0
    for i in range(DataClass1):
        Output = np.dot(Class1[i,], w)
        if (Output <= alpha):
            w = w + lernrate * Class1[i,]
            error = error + 1
            plotPrint(w)
        
    for i in range(DataClass2):
        Output = np.dot(Class2[i,], w)
        if (Output > alpha):
            w = w - lernrate * Class2[i,]
            error = error + 1
            plotPrint(w)