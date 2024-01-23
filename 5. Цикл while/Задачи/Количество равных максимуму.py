max = 1
count = 0
x = int(input())
while x != 0:
    x = int(input())
    if x > max:
        max = x
        count = 0
    if x == max:

        count += 1
print(count)
