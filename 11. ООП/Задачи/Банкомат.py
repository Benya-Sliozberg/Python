class ATM:
    def __init__(self, id):
        self.__cash = {1000: 9, 500: 12, 100: 9, 50: 4}
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if id < 0:
            raise ValueError('Недопустимое значение')
        self.__id = id

    def total_amount(self):
        total_sum = 0
        for key, value in self.__cash.items():
            total_sum += key * value
        return total_sum

    def withdraw(self, amount):
        andrey = self.__cash.copy()
        for banknote in andrey:
            while amount >= banknote and andrey[banknote] > 0:
                amount -= banknote
                andrey[banknote] -= 1
        if amount == 0:
            return 'Осталось в банкомате:', andrey
        return 'Не удалось снять деньги'



atm = ATM(4568)
atm.id = 1000
print(atm.id, atm.total_amount(),atm.withdraw(5050))