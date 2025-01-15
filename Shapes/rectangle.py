from .shape import Shape
from .point import Point
from .line import Line
class Rectangle(Shape):
    def __init__(self, bottom_left, upper_right):
        super().__init__()
        self.is_regular = False
        bottom_right = Point(upper_right.x_val, bottom_left.y_val)
        upper_left = Point(bottom_left.x_val, upper_right.y_val)
        self.vertices_.extend([bottom_left, upper_left, upper_right, bottom_right])
        self.edges_.extend([
            Line(bottom_left, upper_left),
            Line(upper_left, upper_right),
            Line(upper_right, bottom_right),
            Line(bottom_right, bottom_left)
        ])
    
    def area(self):
        return Line.length(self.edges_[0]) * Line.length(self.edges_[1])

    def perimeter(self):
        return (2 * Line.length(self.edges_[0])) + (2 * Line.length(self.edges_[1]))

    def inner_angles(self):
        self.inner_angles_ = [90] * 4
        return self.inner_angles_
