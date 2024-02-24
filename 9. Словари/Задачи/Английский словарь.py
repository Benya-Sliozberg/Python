dct = {}
num = int(input())
c = 0
while c < num:
    line = input().split(' - ')
    words = line[1].split(', ')
    for i in words:
        if i not in dct:

            dct[i] = [line[0]]
        else:
            dct[i].append(line[0])

    c += 1
for i in dct:
    print(i, '-', ', '.join(dct[i]))
