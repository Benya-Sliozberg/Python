'''
def Is_Prime(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    return is_prime



N = int(input())
x = 2
count = 0


while count < N:
    if Is_Prime(x):
        count += 1
        print(x)
    x += 1
'''
