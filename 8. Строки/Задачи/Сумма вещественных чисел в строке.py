def sum_str(s):
    for i in s:
        if not i.isdigit() and i not in [' ', '.']:
            s = s.replace(i, '')

    lst = s.split()

    return sum(list(map(float, lst)))


print(sum_str('abc1.def1.1 stu7.y11u'))