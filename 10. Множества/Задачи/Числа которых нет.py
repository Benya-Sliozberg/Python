nums = {'0','1','2','3','4','5','6','7','8','9'}
s = input()
s1 = ''
setn = set()
for i in s:
    if i.isalpha():
        s = s.replace(i,'')
for i in s:
    setn.add(i)
if len(nums.difference(setn)) == 0:
    print('NO')
else:
    for i in nums.difference(setn):
        s1 += str(i)
    print(*(sorted(s1)[::-1]))