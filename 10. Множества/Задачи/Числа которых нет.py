nums = {'0','1','2','3','4','5','6','7','8','9'}
s = input()
setn = set()
for i in s:
    if i.isalpha():
        s = s.replace(i,'')
for i in s:
    setn.add(i)
print(*(nums.difference(setn)))