from math import sqrt

class proba:
    def __init__(self, a,b):
        px=self.x = a
        py=self.y = b

    def dist(self, d2):
        dx= d2.x - self.x
        dy= d2.y - self.y
        return sqrt(dx*dx + dy*dy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y


def dist(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return sqrt(dx*dx + dy*dy)


