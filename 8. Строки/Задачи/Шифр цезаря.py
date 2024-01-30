alph = 'abcdefghijklmnopqrstuvwxyz'
c = input()
k = int(input()) % len(alph)
newalph = alph[k:] + alph[0:k]

result = ''
for i in c:
    if i == ' ':
        result += ' '

    else:
        if not i.isalpha():
            result += i
        elif i == i.upper():
            i = i.lower()
            ind = alph.find(i)
            result += newalph[ind].upper()
        else:
            ind = alph.find(i)
            result += newalph[ind]
print(result)