from .rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, bottom_left, upper_right):
        super().__init__(bottom_left, upper_right)
        self.is_regular = True

    def area(self):
        return super().area()

    def inner_angles(self):
        return super().inner_angles()
