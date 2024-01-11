from random import randint
from math import sqrt
import matplotlib.pyplot as plt


def knn():
    k: int = int(input("k (uneven works best): "))
    points: list[Point] = []
    for i in range(10):
        points.append(Point(randint(1, 100), randint(1, 100), "blue"))
        points.append(Point(randint(1, 100), randint(1, 100), "red"))
    new_point: Point = Point(randint(1, 10), randint(1, 10))
    array_points_blue: list[list[int]] = []
    array_points_red: list[list[int]] = []
    for point in points:
        if point.color == "blue":
            array_points_blue.append([point.x, point.y])
        if point.color == "red":
            array_points_red.append([point.x, point.y])
    plt.plot([i[0] for i in array_points_blue], [i[1] for i in array_points_blue], '*', color="blue")
    plt.plot([i[0] for i in array_points_red], [i[1] for i in array_points_red], '*', color="red")
    plt.plot(new_point.x, new_point.y, '*', color="green")
    plt.show()
    list_of_points: list[Point] = []
    for point in points:
        distance = sqrt(abs(point.x - new_point.x) ** 2 + abs(point.y - new_point.y) ** 2)
        point.distance = distance
        if len(list_of_points) < k:
            list_of_points.append(point)
        else:
            list_of_points.sort(key=lambda x: x.distance)
            smallest_distance: int = list_of_points[0].distance
            if smallest_distance > point.distance:
                list_of_points[-1] = point
    count_blue: int = sum(point.color == "blue" for point in list_of_points)
    count_red: int = sum(point.color == "red" for point in list_of_points)
    print(f'blue: {count_blue}, red: {count_red}')
    if count_red > count_blue:
        print("The new point is red")
    elif count_red < count_blue:
        print("The new point is blue")
    else:
        print("The new point cannot be colored, because there are as many red as there are blue points. Please "
              "choose another value for k")


class Point:
    x: int
    y: int
    distance: int
    color: str

    def __init__(self, x: int, y: int, color: str = ""):
        self.x = x
        self.y = y
        self.color = color
