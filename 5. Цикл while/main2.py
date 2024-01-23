# Посчитать кол-во цифр в числе и найти их сумму
# 154685
# Кол-во: 6
# Сумма:  29
num = int(input())
count = 0
while num > 0:
    count += 1
    num = num // 10
print(f'Кол-во: {count}')