# Для быстрого создания массива, заполненного определёнными значениями
# используют генераторы
import random

arr = [0 for i in range(10)]
print(arr)

arr = [i for i in range(10)]
print(arr)

arr = [random.randint(-10, 10) for i in range(10)]
print(arr)
