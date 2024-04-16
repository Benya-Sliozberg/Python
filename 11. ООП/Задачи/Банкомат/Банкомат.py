class ATM:
    __max_cash_count = 1000
    def __init__(self, id):
        self.__cash = {5000: 0, 1000: 9, 500: 12, 100: 9, 50: 4}
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
        # Проверка возможности снять данную сумму
        amount_tmp = amount
        cash = {}
        for key, value in self.__cash.items():
            count = amount_tmp // key
            if 0 < count <= value:
                amount_tmp -= key * count
                cash[key] = count
        # Если можем снять такую сумму
        if amount_tmp == 0:
            # Извлекаем из банкомата необходимые купюры
            for key, value in cash.items():
                self.__cash[key] -= value
            return cash
        else:
            raise Exception('Банкомат не может выдать данную сумму')

    def __str__(self):
        banknotes = ''
        for key, value in self.__cash.items():
            banknotes += f'{key:5d} - {value}\n'
        return banknotes

    def load_cash(self, dct):
        for key, value in dct.items():
            self.__cash[key] += value



atm = ATM(4568)
print(atm.total_amount())
print(atm.withdraw(5050))
print(atm)
