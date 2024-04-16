class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{{{self.x};{self.y}}}'

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

v1 = Vector(1, 3)
v2 = Vector(5, 9)
print(v1 + v2)