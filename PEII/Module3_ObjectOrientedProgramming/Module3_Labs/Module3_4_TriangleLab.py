# triangle class
import math


# Point class used to define vertices
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot((self.__x - x), (self.__y - y))

    def distance_from_point(self, point):
        return math.hypot((point.gety() - self.__y),
                          (point.getx() - self.__x))


# Triangle class
class Triangle:
    def __init__(self, vert1, vert2, vert3):
        self.__vert_a = vert1
        self.__vert_b = vert2
        self.__vert_c = vert3

    def perimeter(self):
        return (self.__vert_a.distance_from_point(self.__vert_b) +
                (self.__vert_b.distance_from_point(self.__vert_c)) +
                (self.__vert_c.distance_from_point(self.__vert_a)))


# test data
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
