'''
def magic(*a, b):
    n = 0
    for i in a:
        n += i**2
    if n % b == 0:
        return('Волшебство случается')
    return('Никакого волшебства')
print(magic(2, 5, 7,b=2))
'''

'''
def to_float(a):
    if isinstance(a, (int,float)):
        return float(a)
    return 'Невозможно преобразовать'
print(to_float(2))
'''

'''
def avg_5(a, b, c, d):
    return round((a + b + c + d) / 4, 5)
print(avg_5(1.7,6.2,2,6))
'''

'''
def mul_to_int(a,b):
    res = a*b
    if float(res).is_integer():
        return int(res)
    return res
print(mul_to_int(2.2, 4))
'''

'''
def round_standard(num):
    if num >= 0:
        sign = 1
    else:
        sign = -1
    return sign * int((abs(num) + 0.5))
print(round_standard(1.6))
'''
'''
def eqv(a, b, c):
    res = a + b
    e = 0.01 / 100
    tol = e * max(abs(a), abs(b))
    return (res - c) <= tol
print(eqv(-0.1, -0.2, -0.3))
'''

'''
def dislike_6(a):
    if (type(a) is float or type(a) is int) and a == 6:
        return 'Только не 6!'
    return True
print(dislike_6(6.0))
'''

'''
def divider(a, b):
    if b == 0:
        return 'Нули в знаменателе не приветсвуются'
    if b != 0:
        n = a/b
        n = n**3
        return n
print(divider(-12.2, 2))
'''
'''
def divider(a, b):
    return b and (a/b)**3 or 'Нули в знаменателе не приветствуются'
print(divider())
'''

'''
my_list = [2, 4, 8]
print(my_list[::-1])
'''

'''
my_list = [2, 4, 8]
my_list.reverse()
print(my_list)
'''


'''
def change(ist):
    ist[0], ist[-1] = ist[-1], ist[0]
    return ist
print(change(['н','л','о','с']))
'''
'''
def change(ist):
    new_start = ist.pop()
    new_end = ist.pop(0)
    ist.append(new_end)
    ist.insert(0, new_start)
    return ist
print(change([1,2,3]))
'''

'''
r = int(input())
p = 3.14159
n = p * r ** 2
print(n)
'''

'''
n, m = input().split()
print(m, n)
'''
'''
def useless(s):
    max = 0
    count = 0
    n = 0
    for i in s:
        if i > max:
            max = i
        count += 1
        n = max / count
    return n
print(useless([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))
'''
'''
def useless(ist):
    return max(ist) / len(ist)
print(useless([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))
'''
'''
def to_float(num):
    if isinstance(num, (int, float)):
        num = float(num)
        return num
    return 'Невозможно преобразовать'
print(to_float(1.2))
'''

'''
player = {'colour': 'green', 'points': 10}
print(player)
for key, valley in player.items():
    print(key,valley)
'''
'''
def to_dict(ist):
    return {element: element for element in ist}
print(to_dict([1, 2, 3, 4]))
'''
'''
my_dict = {'first_one': 'we can do it'}


def biggest_dict(**kwargs):
    my_dict.update(**kwargs)
biggest_dict(k1=22, k2=31, k3=11, k4=91)
biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
print(my_dict)
'''

'''
dic1 = {1:20, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4={}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)
'''


'''
n = int(input())
d = dict()
for x in range(1, n+1):
    d[x]=x*x
print(d)
'''
'''
from collections import Counter
def count_it(sequence):
    return dict(Counter([int(num) for num in sequence]).most_common(3))
print(count_it('1234567890121332887766553535353534444'))
'''

'''
n = []
for i in range(1, 11):
    n.append(i**2)
print(n)

b = [i**2 for i in range(1,11)]
print(b)
'''
'''
from collections import OrderedDict
dct = OrderedDict({1:1,2:2,3:3,4:4,5:5})
first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last=False)
print(dct)
'''

'''

profile = {'nickname':'sync',
           'location':'Russia',
           'job':'programmist'}
for i, j in profile.items():
    print(i, j)

#213  items - извлечение ключ, значение
'''
'''
def tpl_sort(n):
    for i in n:
        if not isinstance(i, int):
            return n
    return tuple(sorted(n))

print(tpl_sort((11, 4.2, 5)))
'''
'''
def sieve(n):
    n = set(n)
    #n = tuple(n)
    #n = n[::-1]
    return(n)
print(sieve([1,1,4,2]))
'''
'''
def sieve(ist):
    unique = []
    [unique.append(item) for item in reversed(ist) if item not in unique]
    return tuple(unique)
print(sieve([1,1,4,4,4,4,2]))
'''
'''
def del_from_tuple(tpl, elem):
    ist = list(tpl)
    if elem in tpl:
        ist.remove(elem)
    return tuple(ist)
print(del_from_tuple((1,2,1,3), 1))
'''
'''
def tp(a): #Создание функции
    b = []
    for i in a:
        n = sum(i)
        b.append(n)
    print(b)
nums = [(1,2),(2,3),(3,4)]
tp(nums) #Вызов функции
'''

'''
def leng(a):
    return len(a)
print(leng(('1','2','10','b')))
'''
'''
def rem(a):
    print(a)
    b = list(a)
    b.pop(2)
    print(b)
    b.pop(6)
    return tuple(b)
print(rem(('w','3','r','s','o','u','r','c','e')))
'''
'''
def st(str1):
    str1 = list(str1)
    for i in str1:
        str1.append(i)
        return tuple(str1)
print(st('python 3.0'))
'''
'''
l = []
for i in range(1,11):
    l.append(i**2)
print(l)
'''

'''
l = [i**2 for i in range(1,11)]
print(l)
'''

'''
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)
'''

'''
num = [10,20,30,2,(10,20),40]
ctr = 0
for n in num:
    if isinstance(n, tuple):
        break
    ctr += 1
print(ctr)
'''

'''
def tuple_int_str(tuple_str):
    result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
    return result
print(tuple_int_str((('333', '33') , ('1416', '55')))) 
'''
'''
def tuple_int_str(tuple_str):
    result = [list(x) for x in tuple_str]
    return result
print(tuple_int_str([(1, 2), (2, 3), (3, 4)]))
'''
'''
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1, 2, -8]))

'''
'''
def max_num_in_list(ls):
    max = ls[0]
    for i in ls:
        if i > max:
            max = i
    return max
print(max_num_in_list([1, 2, -8, 0]))
'''
'''
def match_words(words):
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1

    return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))
'''
'''
def sort_list_last(ls):
    ctr = ls[0]
    for i in ls:
        if i[-1] > ctr:
            ls.append(i)
    return ls
print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
        
'''
'''
def last(n):
    return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
'''
'''
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
n = []
n = [n.append(i) if i not in a] #
print(n)
'''

'''
original_list = [10, 22, 44, 23, 4]
print(original_list,original_list)
'''
'''
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(0)
color.pop(3)
color.pop()
print(color)
'''
'''
import collections

my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

print("Original List : ", my_list)

ctr = collections.Counter(my_list)

print("Frequency of the elements in the List : ", ctr)
'''


'''
def count_range_in_list(list1, a, b):
    count = 0
    for i in list1:
        if i >= a and i <= b:
            count += 1
    return count
print(count_range_in_list([10, 20, 30, 40, 40, 40, 70, 80, 99], 40, 100))
'''
'''
color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"

print(set(color1) & set(color2))
'''

'''
color = ['red', 'green', 'orange']

print('-'.join(color))

print(''.join(color))
'''
'''
def max_num_in_list(lst):
    max1 = lst[0]
    for i in lst:
        if i > max1:
            max1 = i
    b = lst[0]
    for n in lst:
        if n > b:
            b = n
        if n < max1 and n > b:
            return n
        return max1
print(max_num_in_list([1, 2, -8, 0]))
'''

'''
lst = [1, 1, 2, 3, 3, 4, 5]
print(set(lst))
'''
'''

def second_largest(numbers):
    if len(numbers) < 2:
        return

    if len(numbers) == 2 and numbers[0] == numbers[1]:
        return

    dup_items = set()
    uniq_items = []

    for x in numbers:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)

    uniq_items.sort()
    return uniq_items[-2]


print(second_largest([1, 2, 3, 4, 4]))
print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
'''


'''
def lst(lss):
    count = 0
    for i in lss:
        if isinstance(i, int):
            count += 1
    return count
print(lst([1,'ab',3,1.12,-12,'7']))
'''

'''
def pos_add(a, b):
    return abs(a) + abs(b)
print(pos_add(-3,4))
'''
'''
def num_sum(a):
   # 1. Определяем принадлежность значения 'a' к целому числу, но не к булеву типу
   if isinstance(a, int) and not isinstance(a, bool):
       # 2. Преобразуем число в положительное, а потом - строку
       a_to_str = str(abs(a))
       # 3. Задаем начальную сумму 0
       s = 0
       # 4. В цикле складываем все числа
       for i in a_to_str:
           s += int(i)
       return s
   return 'Это не целое число'

# Тесты
print(num_sum(-146))
print(num_sum('-11'))
print(num_sum(True))
'''
'''
def magic(*a,k):
    b = 0
    for i in a:
        b += i**2
        if b % k == 0:
            return 'Волшебство случается'
    return 'Никакого волшебства'
print(magic(2,5,7,k = 5))
'''
'''
def to_float(num):
    if isinstance(num, int or bool):
        return float(num)
    if isinstance(num, float):
        return num
    return 'Это не число'
print(to_float(12))
print(to_float(-1.762))
print(to_float(True))
print(to_float('Не число'))
print(to_float('2.2'))
'''
'''
def count_element_in_list(input_list, x):
    ctr = 0
    for i in range(len(input_list)):
        if x in input_list[i]:
            ctr += 1
    return ctr

list1 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]

print(count_element_in_list(list1, 1))
'''
'''
def sortinglst(lst):
    b = []
    for i in lst:
        b.append(sorted(i))
    return b
print(sortinglst([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))
'''

'''
def remove_list_range(input_list, left_range, right_range):
    result = [i for i in input_list if (min(i) >= left_range and max(i) <= right_range)]
    return result


list1 = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
left_range = 13
right_range = 17

print(remove_list_range(list1, left_range, right_range))
'''

'''
def sorting(lst):
    if lst == sorted(lst):
        return 'Указанный список отсортирван верно'
    return 'Указанный список отсортирван неверно'
print(sorting([1, 2, 4, 6, 8, 10, 12, 14, 1, 17]))
'''

'''
def extract_nth_element(test_list, n):
    result = [x[n] for x in test_list]
    return result


students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
print(extract_nth_element(students, 0))
'''

'''
def all_unique(test_list):
    if len(test_list) > len(set(test_list)):
        return False
    return True
'''
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
for i in list2:
        if i in list1:
            list1.remove(i)
print(list1)
'''
'''
l = ['red', 'black', 'white', 'green', 'orange']

n = input()
for i in l:
    if n in i:
        print('True')
'''
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
#l = [x for x in list2 if x in list1]
#print(l)

def reverse_strings_list(string_list):
    result = [x[::-1] for x in string_list]
    return result

colors_list = ["Red", "Green", "Blue", "White", "Black"]
print(reverse_strings_list(colors_list))
'''
'''
def tuple_max_val(nums):
    result_max = max([abs(x * y) for x, y in nums])
    result_min = min([abs(x * y) for x, y in nums])
    return result_max, result_min

nums = [(2, 7), (2, 6), (1, 8), (4, 9)]
print(tuple_max_val(nums))
'''
'''
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])
'''
'''
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

L = [t for t in L if t]
print(L)
'''
'''
count = -1
num = [10, 20, 30, (10, 20), 40]
for i in num:
    count += 1
    if isinstance(i, tuple):
        break

print(count)
'''
'''
def cnt(l):
    b = 1
    for i in l:
        b *= i
    return b
print(cnt((4, 3, 2, 2, -1, 18)))
'''
'''
def preob(l):
    b = ''
    for i in l:
        b += str(i)
    return b
print(preob((1, 2, 3)))
'''

'''
def preob(l):
    b = []
    for i in l:
        b.append(list(i))
    return b
print(preob([(1, 2), (2, 3), (3, 4)]))
'''
'''
def compare_sets(s1, s2):
    for i in s1:
        if i in s2:
            return False
    return True
x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}
print(compare_sets(x, y))
'''
'''
sn1 = {1, 2, 3, 4, 5}
sn2 = {4, 5, 6, 7, 8}

for i in sn1 & sn2:
    sn1.remove(i)

print("sn1: ", sn1)
print("sn2: ", sn2)
'''

'''
def longest_Common_Prefix(strs):
    min_length = min([len(word) for word in strs])
    for i in range(min_length):
        chars = set([word[i] for word in strs])

        if len(chars) > 1:
            return strs[0][:i]
    return strs[0][:min_length]


strs = ["pqrefgh", "pqrsfgh"]
print(longest_Common_Prefix(strs))
'''
'''
def missing_numbers(set_nums1, set_nums2):
    return set(set_nums1) - set(set_nums2), set(set_nums2) - set(set_nums1)

set_nums1 = {1, 2, 3, 4, 5, 6}
set_nums2 = {3, 4, 5, 6, 7, 8}

print(missing_numbers(set_nums1, set_nums2))
'''
'''
def prset(pr):
    return list(set(pr))
print(prset(['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']))
'''
'''
def third_largest(nums):
    nums = set(nums)
    if len(nums) < 3:
        return None
    nums = list(nums)
    nums.sort(reverse=True)
    return nums[2]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(third_largest(nums))
'''
'''
d = {1: 10, 2: 5}

def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')

is_key_present(5)
is_key_present(9)
'''
'''
def count_dups(nums):
    element = []
    freque = []

    if not nums:
        return element
    running_count = 1
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            running_count += 1
        else:
            freque.append(running_count)
            element.append(nums[i])
            running_count = 1
    freque.append(running_count)
    element.append(nums[i + 1])

    return element, freque

nums = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
print(count_dups(nums))
'''
'''
b1 = []
b = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print(list(set(b1) | set(b)))
'''
'''
origlst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
newlst = []
for i in origlst:
    if i not in newlst:
        newlst.append(i)
print(newlst)
'''

'''
b = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
ccount = 0
c1count = 0
for i in b:
    cc = i.count(1)
    cc1 = i.count(7)
    ccount += cc
    c1count += cc1
print(ccount,c1count)
'''
'''
b = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
b1 = []
for i in b:
    b1.append(sorted(i))
print(b1)
'''

'''
b = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
indmin = int(input())
indmax = int(input())
countmin = 0
countmax = len(b) - indmax - 1
while countmin < indmin:
    b.pop(0)
    countmin += 1
while countmax < indmax:
    b.pop(-1)
    countmax += 1
print(max(b), min(b))
'''
'''
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
id = 0
success = 0
for i in student:
    id += i['id']
    success += i['success']
print(id, success)
'''
'''
num_list = [1, 2, 3, 4]
new_dict = current = {}


for name in num_list:
    current[name] = {}
    current = current[name]

print(new_dict)
'''
'''
student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}
a = {'class', 'name'}
b = {'name', 'Alex'}
c = {'roll_id', 'name'}
for i in a:
    if i in student:
        print(True)
    else:
        print(False)
'''
'''
b = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
b = list(b.items())
amin = 0
amax = 0
a = []
a1 = []
for j in b:
    for g in j:
        if isinstance(g, int):
            a.append(g)
        if isinstance(g, str):
            a1.append(g)
amin = min(a)
amax = max(a)
index = 0
index1 = 0
count = -1
for p in a:
    count += 1
    if p == amin:
        index = count
    if p == amax:
        index1 = count

print(b[index],b[index1])
'''
'''
def test(keys, values):

    return dict(zip(keys, values))

l1 = ['a', 'b', 'c', 'd', 'e', 'f']
l2 = [1, 2, 3, 4, 5]
'''

'''
def test(n):
    return all(abs(int(x) - int(y)) == 2 for x, y in zip(str(n), str(n)[1:]))
'''
'''
number = int(input())
lst = []
minnum = ' '
maxnum = ' '
for i in str(number):
    lst.append(int(i))
for j in sorted(lst):
    if j != 0:
        minnum += str(j)

b = sorted(lst)
b1 = b[::-1]
for p in b1:
    maxnum += str(p)
print(f'Минимальное число:', minnum)
print(f'Максимальное число:', maxnum)
'''
'''
def function1(): #Первая функция
    print("Hello World!")
    def function2(): #Функция которую нужно вызвать из первой функции.
        print("World is answer: Hello!")
        return function2


function1()()
'''
'''
tpl = []
first = (1, 2, 3, 4)
second = (3, 5, 2, 1)
third = (2, 2, 3, 1)
first = list(first)
second = list(second)
third = list(third)
for i in range(len(first)):
    tpl.append(first[i] + second[i] + third[i])
print(tuple(tpl))
'''
'''
def convert_to_int(lst):
    result = [dict([a, int(x)] for a, x in b.items()) for b in lst]
    return result

def convert_to_float(lst):
    result = [dict([a, float(x)] for a, x in b.items()) for b in lst]
    return result

nums_int = [
    {'x': '10', 'y': '20', 'z': '30'},
    {'p': '40', 'q': '50', 'r': '60'}
]
print(convert_to_int(nums_int))

nums_float = [
    {'x': '10.12', 'y': '20.23', 'z': '30'},
    {'p': '40.00', 'q': '50.19', 'r': '60.99'}
]
print(convert_to_float(nums_float))
'''

'''
b = [(1, 2), (2, 3), (3, 4)]
newb = []
for i in b:
    newb.append(sum(list(i)))
print(newb)
'''
'''
def first_repeated_word(str1):
    temp = set()
    for word in str1.split():
        if word in temp:
            return word
        else:
            temp.add(word)
print(first_repeated_word("ab ca bc ab"))
print(first_repeated_word("ab ca bc ab ca ab bc"))
print(first_repeated_word("ab ca bc ca ab bc"))
print(first_repeated_word("ab ca bc"))
'''

'''
def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1
            char_order.append(c)

    for c in char_order:
        if ctr[c] == 1:
            return c

    return None

print(first_non_repeating_character('abcdef'))
print(first_non_repeating_character('abcabcdef'))
print(first_non_repeating_character('aabbcc'))
'''
'''
lst = ['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']
temp = set()
for i in lst:
    temp.add(i)
print(sorted(temp))
'''
'''
x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}

if len(set(x | y)) == len(x) + len(y):
    print(True)
else:
    print(False)
if len(set(z | y)) == len(z) + len(y):
    print(True)
else:
    print(False)
if len(set(x | z)) == len(x) + len(z):
    print(True)
else:
    print(False)
'''
'''
def match_words(word):
    count = 0
    for i in word:
        if i[0] == i [-1]:
            count += 1
    return count

print(match_words(['abc', 'xyz', 'aba', '1221']))
'''
'''
my_dict = {'first one': 'we can do it'}
def biggest_dict(**kwargs):
    my_dict.update(**kwargs)


print(biggest_dict(k1=22, k2=31, k3=11, k4=91))
print(biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey'))
print(my_dict)
'''
'''
def count_it(sequence):
    num_frequency = {int(item): sequence.count(item) for item in sequence}
    sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])
    return dict(sorted_num_frequency[-3:])


print(count_it('1111111111222'))
print(count_it('123456789012133288776655353535353441111'))
print(count_it('007767757744331166554444'))
'''

