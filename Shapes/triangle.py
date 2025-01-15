import math
from .shape import Shape
from .point import Point
from .line import Line
class Triangle(Shape):
    def __init__(self, bottom_left, bottom_right, upper_vertex):
        super().__init__()
        self.is_regular = False
        self.vertices_.extend([bottom_left, bottom_right, upper_vertex])
        self.edges_.extend([
            Line(bottom_left, bottom_right),
            Line(bottom_right, upper_vertex),
            Line(upper_vertex, bottom_left)
        ])
    
    def perimeter(self):
        return sum(Line.length(edge) for edge in self.edges_)
