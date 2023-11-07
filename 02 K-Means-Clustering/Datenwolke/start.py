''' Import Bibliotheken '''
import numpy as np
import random
import matplotlib.pyplot as plt
from math import sqrt

''' Daten generieren '''
points = 100
posData1 = 10
posData2 = 50
spread = 13
dimension = 2
data1 = np.random.normal(posData1,spread,(points,dimension))
data2 = np.random.normal(posData2,spread,(points,dimension))
data  = np.concatenate((data1, data2))

''' Plot '''
dataPoints = np.size(data,0)
plt.plot(data[:,0],data[:,1],'*')
plt.show()

''' K-Means-Clustering Algorithmus '''
k = 2
kVector = np.zeros((2, 2))
kVector[0, 0] = random.randint(10,50)
kVector[0, 1] = random.randint(10,50)
kVector[1, 0] = random.randint(10,50)
kVector[1, 1] = random.randint(10,50)

# Own clustering algorithm

randomKPointOne = random.choice(data)
randomKPointTwo = random.choice(data)
while (randomKPointOne[0] == randomKPointTwo[0] and randomKPointOne[1] == randomKPointTwo[1]):
    randomKPointTwo = random.choice(data)

clusterOne = []
clusterTwo = []

sumDistanceToPointOne = 0
sumDistanceToPointTwo = 0

stillNeedsWorking = True
while(stillNeedsWorking):
    for point in data:
        distanceToPointOne = sqrt((abs(randomKPointOne[0] - point[0])**2) + (abs(randomKPointOne[1] - point[1]))**2)
        distanceToPointTwo = sqrt((abs(randomKPointTwo[0] - point[0])**2) + (abs(randomKPointTwo[1] - point[1]))**2)
        if distanceToPointOne > distanceToPointTwo:
            clusterOne.append(point)
        elif distanceToPointOne < distanceToPointTwo:
            clusterTwo.append(point)
        else:
            continue
    stillNeedsWorking = False
    
    sumDistanceToPointOne += distanceToPointOne
    sumDistanceToPointTwo += distanceToPointTwo
    
    
    
plt.plot(clusterOne, "*", color='red')
plt.plot(clusterTwo, "*", color='blue')
plt.show()