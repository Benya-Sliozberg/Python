# Человек
class Person:
    def __init__(self, full_name):
        self.full_name = full_name



# Работник
class Employee(Person):
    def __init__(self, full_name, salary):
        # Класс наследник обязан всегда вызывать конструктор базового класса
        # super() - обращение к базовому классу
        super().__init__(full_name)
        self.salary = salary

    def __str__(self):
        return f'{self.full_name} {self.salary}'
