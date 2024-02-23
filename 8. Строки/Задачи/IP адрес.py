"""
У пользователя запрашивается IP адрес в формате: [0-255].[0-255].[0-255].[0-255]
Необходимо вывести его двоичное представление.
Каждое число в IP адресе 8 битное.

Пример
Вход:
    127.0.0.1
Выход:
    01111111 00000000 000000000 00000001
"""


def ip_bin(ip):
    return ' '.join([bin(int(num))[2:].zfill(8) for num in ip.split('.')])


print(ip_bin('127.0.0.1'))
