from math import sqrt
from random import randint

import matplotlib.pyplot as plt


def knn():
    k: int = int(input("k (uneven number works best): "))
    points: list[Point] = []
    for i in range(10):
        points.append(Point(randint(1, 100), randint(1, 100), "blue"))
        points.append(Point(randint(1, 100), randint(1, 100), "red"))
    new_point: Point = Point(randint(1, 100), randint(1, 100))
    array_points_blue: list[Point] = []
    array_points_red: list[Point] = []
    for point in points:
        if point.color == "blue":
            array_points_blue.append(point)
        if point.color == "red":
            array_points_red.append(point)
    plt.scatter([point.x for point in array_points_blue], [point.y for point in array_points_blue], color="blue")
    plt.scatter([point.x for point in array_points_red], [point.y for point in array_points_red], color="red")
    plt.scatter(new_point.x, new_point.y, color="green")
    plt.show()
    list_of_points: list[Point] = []
    for point in points:
        distance = sqrt((point.x - new_point.x) ** 2 + (point.y - new_point.y) ** 2)
        point.distance = distance
        if len(list_of_points) < k:
            list_of_points.append(point)
        else:
            list_of_points.sort(key=lambda x: x.distance)
            biggest_distance: int = list_of_points[-1].distance
            if biggest_distance > point.distance:
                list_of_points[-1] = point
    for point in list_of_points:
        if point in array_points_blue:
            plt.scatter(point.x, point.y, color="blue")
        elif point in array_points_red:
            plt.scatter(point.x, point.y, color="red")
        else:
            print("point isn't red or blue")
    count_blue: int = sum(point.color == "blue" for point in list_of_points)
    count_red: int = sum(point.color == "red" for point in list_of_points)
    # Scattering the new point in another color to enable User to identify it
    if count_red > count_blue:
        print("The new point is red")
        plt.scatter(new_point.x, new_point.y, color="pink")
    elif count_red < count_blue:
        print("The new point is blue")
        plt.scatter(new_point.x, new_point.y, color="cyan")
    else:
        print("The new point cannot be colored, because there are as many red as there are blue points. Please "
              "choose another value for k")
    plt.show()


class Point:
    x: int
    y: int
    distance: int
    color: str

    def __init__(self, x: int, y: int, color: str = ""):
        self.x = x
        self.y = y
        self.color = color
