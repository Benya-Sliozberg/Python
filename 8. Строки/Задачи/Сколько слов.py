x = input()
count = 1
x = x.strip()
while '  ' in x:
    x = x.replace('  ', ' ')
for i in x:
    if i == ' ':
        count += 1
print(count)