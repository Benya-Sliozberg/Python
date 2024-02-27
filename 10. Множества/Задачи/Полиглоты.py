students = int(input())
listofsets = []
c_students = 0
while c_students != students:
    c_students += 1
    languages = int(input())
    c_languages = 0
    langs = set()
    while c_languages != languages:
        c_languages += 1
        langs.add(input())
    listofsets.append(langs)
s1 = set()
s = listofsets[0].copy()
for i in range(len(listofsets)):
    s = s.intersection(listofsets[i])
    s1 |= listofsets[i]
print(len(s))
print(*sorted(s), sep='\n')
print(len(s1))
print(*sorted(s1), sep='\n')
