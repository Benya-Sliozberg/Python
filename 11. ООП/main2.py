class ATM:
    def __init__(self, id):
        # Доступ к полю cash будет запрещён
        self.__cash = {'10': 0, '50': 0, '100': 0}
        self.__id = id

    # Свойство для получения информации - getter
    # Изменить значение с помощью getter не получится
    @property
    def id(self):
        return self.__id

    # Свойство для установления значения - setter
    @id.setter
    def id(self, id):
        if id < 0:
            raise ValueError('Недопустимое значение')
        self.__id = id


atm = ATM(4568)
atm.id = -1000
print(atm.id)
