n = int(input())
count = 0
dictionary = {}
while count != n:
    count += 1
    key, value = input().split()
    dictionary[key] = value
    dictionary[value] = key
findsin = input()
print(dictionary[findsin])