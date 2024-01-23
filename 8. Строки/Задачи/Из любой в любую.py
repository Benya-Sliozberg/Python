N = input()
K, M = list(map(int, input().split()))


def to_any(N, K, M):
    alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_num = ''
    degree = 0
    result = 0

    # Перевод в десятичную из K
    for j in N[::-1]:
        result += alph.find(j) * (K ** degree)
        degree += 1

    # Перевод из десятичной в M
    while result > 0:
        new_num = alph[result % M] + new_num
        result = result // M

    return new_num


print(to_any(N, K, M))
