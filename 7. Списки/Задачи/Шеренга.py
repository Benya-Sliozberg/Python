count = 1
arr = list(map(int, input().split()))
x = int(input())
for i in range(len(arr)):
    if arr[i] > x:
        count += 1
print(count)
