
def sum_str(stroka):
    lst = []
    for i in stroka:
        if i.isalpha():
            stroka = stroka.replace(i, '')
    for j in stroka.split():
        lst.append(int(j))


    return sum(lst)
print(sum_str('abc1de2f3 stu7yu'))