def sum_str(s):
    for i in s:
        if not i.isdigit() and i != ' ':
            s = s.replace(i, '')
    return sum(list(map(int, s.split())))


print(sum_str('abc1d%e2f3 stu7yu'))