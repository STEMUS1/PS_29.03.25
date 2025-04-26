import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):

        if not isinstance(other, Point2D):
            raise ValueError("Аргумент должен быть экземпляром класса Point2D")

        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):

        return f"x:{self.x} y:{self.y}"


point1 = Point2D(1, 2)
point2 = Point2D(4, 6)

print(point1)
print(point2)
print(point1.distance_to(point2))