
from math import sqrt

"""Превращение функции в метод"""
class metod:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def rast(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx * dx + dy * dy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

a = metod(0, 0)
b = metod(3, 4)

print (a.rast(b))
print(a == b)
print(a == metod(0, 0))


"""Решение с помощью создания класса"""
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

def dist(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return sqrt(dx*dx + dy*dy)


print(dist(Point(0, 0), Point(3, 4)))


"""Обычное решение задачи"""
def distance(x1, y1, x2, y2):
    dx=x2-x1
    dy=y2-x1
    return sqrt(dx*dx + dy*dy)

print(distance(0,0, 3,4))
