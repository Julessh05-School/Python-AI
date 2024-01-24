''' KNN = K-NÃ¤chster Nachbar '''

''' Import Bibliotheken '''
import math

import matplotlib.pyplot as plt
import numpy as np

''' Start data '''
k = 3

points = 30
posData1 = 10
posData2 = 20
spread = 4
dimension = 2

newPoint = [5, 5]
newPointLabel = "green"

labels = ["blue", "red"]

''' K-Naechster-Nachbar Algorithmus '''


def measureDistance(dataPoint, newPoint):
    return math.sqrt(((dataPoint[0] - newPoint[0]) ** 2) + ((dataPoint[1] - newPoint[1]) ** 2))


class Point:
    xKoord: float
    yKoord: float
    distance: float
    label: str

    def __init__(self, xKoord, yKoord, label, distance):
        self.xKoord = xKoord
        self.yKoord = yKoord
        self.label = label
        self.distance = distance


def generateData():
    data = np.random.normal(posData1, spread, (points, dimension))
    return data


# pointArray:list[Point] = [] ist gleich wie
pointArray: [Point] = []

data = generateData()

for i in range(points):
    color = i % 2
    distance = measureDistance(data[i], newPoint)
    pointArray.append(Point(data[i, 0], data[i, 1], labels[color], distance))

''' Plot '''
for i in range(points):
    plt.plot(pointArray[i].xKoord, pointArray[i].yKoord, '+', c=pointArray[i].label)
plt.plot(newPoint[0], newPoint[1], '*', c=newPointLabel)

''' Nearest '''

sortedArray: list[Point] = []

for z in range(k):
    count = 30
    currentPoint = pointArray[1]
    currentIndex = 0
    for i in range(count):
        if currentPoint.distance > pointArray[i].distance:
            currentPoint = pointArray[i]
            currentIndex = i
    sortedArray.append(currentPoint)
    del pointArray[currentIndex]
    count -= 1
