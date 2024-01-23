x, y = list(map(int, input().split()))
def div_sum(num):
    s = 0
    for i in range(1, num + 1):
        if num % i == 0:
            s += i

    return s
if div_sum(x) == div_sum(y):
    print('YES')
else:
    print('NO')
