class Date:
    def __init__(self, date):
        lst = date.split('.')
        self.day = int(lst[0])
        self.month = int(lst[1])
        self.year = int(lst[2])

    def add_day(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            if self.month == 2:
                self.day += 1
                if self.day > 29:
                    self.day = 1
                    self.month += 1
            elif self.month == 12:
                self.day += 1
                if self.day > 31:
                    self.day = 1
                    self.month = 1
                    self.year += 1
            elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                self.day += 1
                if self.day > 30:
                    self.day = 1
                    self.month += 1
            else:
                self.day += 1
                if self.day > 31:
                    self.day = 1
                    self.month += 1


        else:
            if self.month == 2:
                self.day += 1
                if self.day > 28:
                    self.day = 1
                    self.month += 1
            elif self.month == 12:
                self.day += 1
                if self.day > 31:
                    self.day = 1
                    self.month = 1
                    self.year += 1
            elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                self.day += 1
                if self.day > 30:
                    self.day = 1
                    self.month += 1
            else:
                self.day += 1
                if self.day > 31:
                    self.day = 1
                    self.month += 1


    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'


benya = Date('30.6.2000')
benya.add_day()
print(benya)
