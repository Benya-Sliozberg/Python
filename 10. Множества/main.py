s1 = {2, 3, 4, 9}
s2 = {1, 2, 3, 4, 5, 6, 7, 8}

print(s1)
print(s2)
print(f'Объединение: {s1.union(s2)}')
print(f'Пересечение: {s1.intersection(s2)}')
print(f'Разность: {s1.difference(s2)}')
print(f'Симметрическая разность: {s1.symmetric_difference(s2)}')
