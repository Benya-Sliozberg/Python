n = int(input())
c = 0
dct = {}

while c < n:
    line = input().split()
    dct[line[0]] = line[1:]
    c += 1
c = 0
m = int(input())

while c < m:
    line = input()
    for i in dct:
        if line in dct[i]:
            print(i)
            break
    c += 1



