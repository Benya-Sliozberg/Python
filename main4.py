'''
a = [1, 2, 4, 6, 8, 10, 12, 141, 16, 17]
if a == sorted(a):
    print('Список отсортирован')
else:
    print('Не отсортирован')
'''
'''
import math
a = [(2, 7), (2, 6), (1, 8), (4, 9)]
maxpr = -1000
minpr = 1000
for i in a:
    if math.prod(i) > maxpr:
        maxpr = math.prod(i)
    if math.prod(i) < minpr:
        minpr = math.prod(i)
print(minpr, maxpr)
'''
'''
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
b = []
for i in L:
    if i:
        b.append(i) 

print(b)
'''

'''
def f(strs):
    min_length = min([len(word) for word in strs])
    for i in range(min_length):
        chars = set([word[i] for word in strs])

        if len(chars) > 1:
            return strs[0][:i]
    return strs[0][:min_length]


strs = ["pqrefgh", "pqrsfgh"]
print(f(strs))
'''

def is_key_present(key):
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    if key in d:
        return True
    return False


print(is_key_present(1))
