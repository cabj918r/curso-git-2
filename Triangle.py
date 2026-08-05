import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())

class Triangle:
    def __init__(self, vertice1: Point, vertice2: Point, vertice3: Point) -> None:
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3

    def perimeter(self) -> float:
        perimetro = (
            self.vertice1.distance_from_point(self.vertice2)
            + self.vertice2.distance_from_point(self.vertice3)
            + self.vertice3.distance_from_point(self.vertice1)
        )
        return perimetro


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
