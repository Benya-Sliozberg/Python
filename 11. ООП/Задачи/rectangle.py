class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimetr(self):
        return self.width * 2 + self.height * 2


rec = Rectangle(12, 5)
print(rec.perimetr())
print(rec.area())
