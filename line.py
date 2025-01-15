from .point import Point

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point
    
    def length(self):
        self.len_ = round(Point.distance_to(self.start_point, self.end_point), 2)
        return self.len_
