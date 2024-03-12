from math import sqrt
from random import randint

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)

n = int(input())
points = []
count = 0
while count < n:
    points.append(Point(randint(0,100), randint(0,100)))
    count += 1
max = 0
i1=0
j1=0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if max < points[i].distance(points[j]):
            max = points[i].distance(points[j])
            i1 = points[i]
            j1 = points[j]
t1 = []
t2 = []

t1.append(i1.x)
t1.append(i1.y)
t2.append(j1.x)
t2.append(j1.y)
print(max,tuple(t1),tuple(t2))