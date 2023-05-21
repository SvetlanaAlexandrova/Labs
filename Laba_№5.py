from abc import ABC, abstractmethod
from math import sqrt
from shapely import area as p_area, length as p_length, Polygon

# асбтрактный класс - Figure
class Figure(ABC):
    @property
    def area(self):
        return p_area(Polygon(self.coords))

    @property
    def perimeter(self):
        return p_length(Polygon(self.coords))

class Poly(Figure):
    def __init__(self, coords):
        self.coords = coords
        print('Фигура с координатами:', *self.coords)

    @property
    def area(self):
        return super().area

    @property
    def perimeter(self):
        return super().perimeter

    def info(self):
        print('Многоугольник с координатами', *self.coords)
        print('Периметр:', self.perimeter)
        print('Площадь:', self.area)

# класс - Triangle
class Triangle(Figure):

    def __init__(self, coords):
        self.coords = coords
        self.__a, self.__b, self.__c = 0, 0, 0
        self.__isValidTriangle()

    def __isValidTriangle(self):
        if len(self.coords) != 3 or not (all(x >= 0 and y >= 0 for (x, y) in self.coords)):
            raise FigureExceptions
        else:
            x1, y1 = self.coords[0][0], self.coords[0][1]
            x2, y2 = self.coords[1][0], self.coords[1][1]
            x3, y3 = self.coords[2][0], self.coords[2][1]
            a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
            c = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
            if not (a + b > c and a + c > b and b + c > a):
                raise TriangleExceptions
            else:
                self.__a, self.__b, self.__c = a, b, c

    @property
    def area(self):
        p = self.perimeter / 2
        area = sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))
        return round(area, 3)
    @property
    def perimeter(self):
        return self.__a + self.__b + self.__c

    def triangleType(self):  # если стороны не равны между собой - треугольник разносторонний
        if self.__a != self.__b and self.__b != self.__c and self.__c != self.__a:
            return False
        else:
            return True

    def info(self):
        print('Треугольник с координатами', *self.coords)
        print('Периметр:', self.perimeter)
        print('Площадь:', self.area)
        print('Является равносторонним или равнобедренным:', self.triangleType())

    def trianglesOverlap(self, other):  # метод из библиотеки shapely
        t1 = Polygon(self.coords)
        t2 = Polygon(other.coords)
        return t1.intersects(t2)


# класс - Quadrilateral
class Quadrilateral(Figure):

    def __init__(self, coords):
        self.coords = coords

        self.__isValidQuad()

    def __isValidQuad(self):
        if len(self.coords) != 4 or not (all(x >= 0 and y >= 0 for (x, y) in self.coords)):
            raise FigureExceptions
        elif len(set(self.coords)) != 4:
            raise QuadExceptions
        else:
            quad = Polygon(self.coords)
            if not quad.is_valid:
                raise QuadExceptions

    @property
    def area(self):  #из библиотеки shapely
        quad = Polygon(self.coords)
        return round(p_area(quad), 3)

    @property
    def perimeter(self):  #из библиотеки shapely
        quad = Polygon(self.coords)
        return round(p_length(quad), 3)

    def quadType(self):
        x1, y1 = self.coords[0][0], self.coords[0][1]
        x2, y2 = self.coords[1][0], self.coords[1][1]
        x3, y3 = self.coords[2][0], self.coords[2][1]
        x4, y4 = self.coords[3][0], self.coords[3][1]
        a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        c = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        d = sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
        if a == c and d == b:
            return True
        else:
            return False

    def info(self):
        print('Четырехугольник с координатами', *self.coords)
        print('Периметр:', self.perimeter)
        print('Площадь:', self.area)
        print('Является параллелограммом:', self.quadType())

# исключения
class FigureExceptions(Exception):
    def __init__(self, message='Ошибка в координатах фигуры'):
        self.message = message

    def __str__(self):
        return self.message


class TriangleExceptions(Exception):
    def __init__(self, message='Несуществующий треугольник'):
        self.message = message

    def __str__(self):
        return self.message


class QuadExceptions(Exception):
    def __init__(self, message='Несуществующий четырехугольник'):
        self.message = message

    def __str__(self):
        return self.message

tr1 = Triangle([(0, 0), (0, 4), (6, 7)])
tr1.info()
print()

tr2 = Triangle([(0, 0), (4, 0), (2, 8)])
tr2.info()
print('Пересечение с треугольником: ', tr1.coords, end=' ')
print(tr2.trianglesOverlap(tr1))
print()

tr3 = Triangle([(10, 0), (10, 10), (15, 5)])
tr3.info()
print('Пересечение с треугольником', tr2.coords, end=' ')
print(tr3.trianglesOverlap(tr2))
print()

qu1 = Quadrilateral([(0, 0), (1, 2), (5, 7), (3, 1)])
qu1.info()
print()

qu2 = Quadrilateral([(0, 0), (1, 1), (2, 1), (1, 0)])
qu2.info()
print()

qu3 = Quadrilateral([(0, 0), (0, 5), (5, 5), (5, 0)])
qu3.info()
print()

test1 = Poly([(0, 0), (0, 5), (5, 5), (5, 0)])
test1.info()
print()

test2 = Poly([(0, 0), (0, 4), (6, 7)])
test2.info()
print()

test3 = Poly([(0, 1), (1, 2), (2, 3), (2, 1), (1, 0)])
test3.info()
print()