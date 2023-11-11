from exercise_1.Shape import Shape
import math as math


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.perimeter = 0
        self.radius = radius

    def get_area(self):
        return "".join(str(math.pi * self.radius ** 2)[:3])

    def get_perimeter(self):
        return "".join(str(2 * math.pi * self.radius)[:3])
