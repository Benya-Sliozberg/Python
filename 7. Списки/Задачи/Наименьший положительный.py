min = 1000
arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] < min and arr[i] > 0:
        min = arr[i]
print(min)