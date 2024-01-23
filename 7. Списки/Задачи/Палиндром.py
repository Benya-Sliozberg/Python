x = input()
x = x.replace(' ','')
if x == x[::-1]:
    print(f'YES')
else:
    print(f'NO')