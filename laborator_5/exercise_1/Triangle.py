from functools import reduce

from exercise_1.Shape import Shape
import math as math


class Triangle(Shape):
    def __init__(self, *edges):
        super().__init__()
        self.edges = edges

    def get_area(self):
        self.perimeter = self.get_perimeter()
        semiperimeter = self.perimeter / 2
        result = reduce(lambda x, y: x * (semiperimeter - y), self.edges, 1)
        return "".join(str(math.sqrt((self.perimeter / 2) * result))[:4])

    def get_perimeter(self):
        self.perimeter = sum(self.edges)
        return self.perimeter
