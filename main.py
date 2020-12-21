
class Figure:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name + ": " + str(self.calculate_square()) + " " + str(self.calculate_perimeter())

    def calculate_square(self):
        pass

    def calculate_perimeter(self):
        pass

    def print(self):
        print(str(self))

class Line(Figure):

    def __init__(self, point1, point2):
        self.
        pass

















