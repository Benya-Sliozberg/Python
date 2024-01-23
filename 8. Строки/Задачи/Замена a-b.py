'''
line = input()
result = ''
count = 0
#line = line.replace('a', 'b')
for c in line:
    if c == 'a':
        result += 'b'
        count += 1
    else:
        result += c
print(result)
print(count)
'''
'''
line = input()
line = line.replace('A','B')
line = line.replace('B','A')
line = line.replace('a','b')
line = line.replace('b','a')
print(line)
'''

line = input()
result = ''
count = 0
for x in line:
    if x == 'a':
        result += 'b'
        count += 1
    elif x == 'b':
        result += 'a'
        count += 1
    elif x == 'A':
        result += 'B'
        count += 1
    elif x == 'B':
        result += 'A'
        count += 1
    else:
        result += x
print(result)
print(count)