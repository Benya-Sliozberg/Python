def is_palindrome(num):
    x = 0
    xer = num
    while num != 0:
        m = num % 10
        num = num // 10
        x = x * 10 + m
    return x == xer


a = int(input())
b = int(input())
for i in range(a, b + 1):
    if is_palindrome(i):
        print(i)