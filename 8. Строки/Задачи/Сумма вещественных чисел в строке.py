def sum_str(stroka):
    lst = []
    result = []
    timestr = ''
    counthelp = 0
    counthelp1 = 0
    for i in stroka:
        if i.isalpha():
            stroka = stroka.replace(i, '')
    for j in stroka.split():
        lst.append(j)
    for b in lst:
        for newb in b:
            if newb == '.' and newb not in timestr:
                timestr += newb
            elif newb =='.' and newb in timestr:
                continue
            else:
                timestr += newb
            if timestr[-1] == b[-1]:
                result.append(float(timestr))
                timestr = ''


    return sum(result)
print(sum_str('abc1.de2.f3 stu7yu'))