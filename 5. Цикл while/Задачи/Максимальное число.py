max = 0
count = 1
x = int(input())
old = x
while x != 0:
    x = int(input())
    if old == x:
        count += 1

    if old != x:
        if count > max:
            max = count
        count = 1
    old = x
print(max)