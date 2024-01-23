N = input()
K = int(input())
M = int(input())
def to_any(num, N, K, M):
    num = list(num)
    num = num[0:K]
    newnum = ''
    stepen = 0
    result = 0
    end = []
    for i in num:
        newnum += i

    for j in reversed(N):
        result += newnum.find(j) * (K ** stepen)
        stepen += 1

    while result > 0:
        end.append(result % M)
        result = result // M

    return end[::-1]


alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(to_any(alph, N, K, M))
