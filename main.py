import math
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name + ": площадь = " + str(self.calculate_square()) + " периметр = " + str(self.calculate_perimeter())

    @abstractmethod
    def calculate_square(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def print(self):
        print(str(self))


class Line(Figure):

    def __init__(self, name: str, point1, point2):
        # p1 ------------ p2

        super().__init__(name)
        self.point1 = point1
        self.point2 = point2

    def calculate_square(self):
        return 0

    def calculate_perimeter(self):
        return round(abs((self.point2[1] - self.point1[1]) ** 2 + (self.point2[0] - self.point1[0]) ** 2) ** 0.5, 2)


class Rectangle(Figure):

    def __init__(self, name: str, point1, point2, point3, point4):

        # p1 ---12--- p2
        # |           |
        # 41          23
        # |           |
        # p4 ---34--- p3

        super().__init__(name)
        self.point2 = point2
        self.point1 = point1
        self.point3 = point3
        self.point4 = point4
        self.side12 = round(abs((self.point2[1] - self.point1[1]) ** 2 + (self.point2[0] - self.point1[0]) ** 2) ** 0.5, 2)
        self.side23 = round(abs((self.point3[1] - self.point2[1]) ** 2 + (self.point3[0] - self.point2[0]) ** 2) ** 0.5, 2)
        self.side34 = round(abs((self.point4[1] - self.point3[1]) ** 2 + (self.point4[0] - self.point3[0]) ** 2) ** 0.5, 2)
        self.side41 = round(abs((self.point1[1] - self.point4[1]) ** 2 + (self.point1[0] - self.point4[0]) ** 2) ** 0.5, 2)

    def calculate_perimeter(self):
        return self.side12 + self.side23 + self.side34 + self.side41

    def calculate_square(self):
        return self.side41 * self.side12


class Ellipse(Figure):
    def __init__(self, name: str, a, b, center):
        super().__init__(name)
        self.a = a
        self.b = b
        self.center = center

    def calculate_perimeter(self):
        return round(math.pi * 2 * ((self.a ** 2 + self.b ** 2 / 2) ** 0.5), 2)

    def calculate_square(self):
        return round(math.pi * self.a * self.b, 2)


def sort_perimeter(my_list: list):
    pos = 0
    i = 0
    minimum = my_list[pos]
    while pos != len(my_figures) - 1:
        if i == len(my_figures) - 1:
            break
        if my_figures[i].calculate_perimeter() < minimum.calculate_perimeter():
            minimum = my_list[i]
            my_list[pos], my_list[i] = minimum, my_list[pos]
            pos += 1
        i += 1
    return my_list


def sort_square(my_list: list):
    pos = 0
    i = 0
    minimum = my_list[pos]
    while pos != len(my_figures) - 1:
        if i == len(my_figures) - 1:
            break
        if my_figures[i].calculate_square() < minimum.calculate_square():
            minimum = my_list[i]
            my_list[pos], my_list[i] = minimum, my_list[pos]
            pos += 1
        i += 1
    return my_list


my_figures = [Ellipse('ellipse', 4, 5, (10, 10)), Line('line', (1, 2), (3, 4)), Rectangle('rectangle', (5, 5), (11, 5), (11, 1), (5, 1))]

print(*my_figures)

my_figures = sort_perimeter(my_figures)
print(*my_figures)

my_figures = sort_square(my_figures)
print(*my_figures)















