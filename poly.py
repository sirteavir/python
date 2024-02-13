import math


class shape:
     def calculate_area(self):
        pass
class Rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
class Circle(shape):
      def __init__(self,radius):
         self.radius = radius
      def calculate_area(self):
        return math.pi * (self.radius ** 2)
def calculate_total_area(shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.calculate_area()
        return total_area
mycircle = Circle(9)
myrectangle = Rectangle(5,7)

print(f"Area of circle is {mycircle.calculate_area()}"
          f"Area of rectangle is {myrectangle.calculate_area()}")