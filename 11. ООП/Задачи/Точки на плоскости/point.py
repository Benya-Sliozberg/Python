from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
    def __str__(self):
        return f'({self.x},{self.y})'