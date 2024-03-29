# Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
# премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров.

class Worker:

    # attributes
    def __init__(self, n, s, p, i=None):
        if i is None:
            i = {"wage": 0, "bonus": 0}
        self.name = n
        self.surname = s
        self.position = p
        self._income = i


class Position(Worker):
    # attributes
    def __init__(self, n, s, p, i):
        super().__init__(n, s, p, i)

    # methods
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position_1 = Position('Sirius', 'Sam', 'Cool Guy', {'wage': 100000, 'bonus': 25000})
print(f"{position_1.get_full_name()}'s total income is {position_1.get_total_income()} $ at a position of a {position_1.position}.")
