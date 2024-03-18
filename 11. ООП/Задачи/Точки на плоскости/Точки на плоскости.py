from random import randint
from point import Point

n = int(input())
points = []
count = 0

while count < n:
    points.append(Point(randint(0, 100), randint(0, 100)))
    count += 1

max_distance = 0
i1 = 0
j1 = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if max_distance < points[i].distance(points[j]):
            max_distance = points[i].distance(points[j])
            i1 = points[i]
            j1 = points[j]

print(max_distance, i1, j1)
