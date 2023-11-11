# Create a class hierarchy for shapes, starting with a base class Shape.
# Then, create subclasses like Circle, Rectangle, and Triangle.
# Implement methods to calculate area and perimeter for each shape.

import exercise_1 as ex_1

triangle = ex_1.Triangle(4, 5, 6)
print("Perimeter of triangle: ", triangle.get_perimeter())
print("Area of triangle: ", triangle.get_area())

circle = ex_1.Circle(1)
print("Perimeter of circle: ", circle.get_perimeter())
print("Area of circle: ", circle.get_area())


rectangle = ex_1.Rectangle(4, 6)
print("Perimeter of rectangle: ", rectangle.get_perimeter())
print("Area of rectangle: ", rectangle.get_area())
