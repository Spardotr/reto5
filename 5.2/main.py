from shapes import Rectangle, Square, Scalene, Isosceles, TriRectangle

if __name__ == "__main__":
    scalene = Scalene(base=3, height=4, side1=3, side2=4, side3=5)
    square = Square(side=4)
    isosceles = Isosceles(base=3, height=4, side=5)

    print(square.__str__())
    print(scalene.__str__())
    print(isosceles.__str__())
