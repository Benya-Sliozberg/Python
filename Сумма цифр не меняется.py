x, y = list(map(int, input().split()))


def sum_digits(num):
    h = 0
    while num > 0:
        h += num % 10
        num = num // 10
    return h


for i in range(x, y):
    sum = sum_digits(i * 2)
    f = True
    for c in range(2, 10):
        if sum_digits(i * c) != sum:
            f = False
    if f:
        print(i)
