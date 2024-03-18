class Student:
    # Рейтинг студента
    rate = 100
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

student1 = Student('Иван')

print(student1)