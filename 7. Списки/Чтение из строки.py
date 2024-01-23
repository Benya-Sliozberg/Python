# Преобразование строки чисел в массив чисел
# 1 2 3 4 5 6 7 8 9
# split() - функция, разделяющая строку на части по пробелам
# map(func, array) - функция, применяющая к каждому элементу массива array функцию func
# list() - преобразует в список
arr = list(map(int, input().split()))
print(arr)

# Вариант с помощью цикла
arr = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
print(arr)