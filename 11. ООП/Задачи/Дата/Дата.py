class Date:
    def __init__(self, date: str):
        lst = date.split('.')
        self.day = int(lst[0])
        self.month = int(lst[1])
        self.year = int(lst[2])

    def get_next_day(self):
        a = (1 - (self.year % 4 + 2) % (self.year % 4 + 1))
        b = ((self.year % 100 + 2) % (self.year % 100 + 1))
        c = (1 - (self.year % 400 + 2) % (self.year % 400 + 1))
        return (28 + ((self.day + (self.day / 8)) % 2) + 2 % self.day + ((1 + a * b + c) / self.day) +
                (1 / self.day) - ((a * b + c) / self.day))

    def add_day(self):
        self.day += 1
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            if self.month == 2 and self.day == 29:
                self.day = 1
                self.month += 1
        else:
            if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                if self.day > 30:
                    self.day = 1
                    self.month += 1
            else:
                if self.day > 31:
                    self.day = 1
                    self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'


from datetime import date, timedelta, datetime

start_date = datetime(1700, 2, 28)
for day in range(100000):
    current_date = start_date + timedelta(days=day)
    next_date = start_date + timedelta(days=day+1)
    date = Date(current_date.strftime('%d.%m.%Y'))
    date.add_day()
    str_date = str(date)
    if Date(next_date.strftime('%d.%m.%Y')).__str__() != str_date:
        print('ERROR')
        print(current_date)
