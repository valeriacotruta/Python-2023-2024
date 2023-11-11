from exercise_1.Shape import Shape

class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__()
        self.edges = [height, width]

    def get_area(self):
        self.perimeter = self.get_perimeter()
        return self.edges[0]*self.edges[1]

    def get_perimeter(self):
        self.perimeter = sum(self.edges) * 2
        return self.perimeter
