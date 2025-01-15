class Point:
    def __init__(self, x_val=0.0, y_val=0.0):
        self.x_val = float(x_val)
        self.y_val = float(y_val)
    
    def distance_to(self, other_point:"Point"):
        return ((self.x_val - other_point.x_val)**2 + (self.y_val - other_point.y_val)**2)**0.5
