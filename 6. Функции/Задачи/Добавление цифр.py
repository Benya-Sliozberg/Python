def add_right_digit(number, digit):
    number = number * 10 + digit
    return number


def digit_count(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count


def add_left_digit(number, digit):
    number = number + 10**digit_count(number) * digit
    return number
print(add_left_digit(41, 9))