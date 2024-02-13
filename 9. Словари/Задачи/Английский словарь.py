dct = {}
num = int(input())
c = 0
while c < num:
    line = input().split()
    dct[line[0]] = line[1:]
    c += 1
for i in dct:
    for j in dct[i]:
        print(j, ' - ', i)