"""Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров)."""

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} : {self.position}'

    def get_total_income(self):
        res = self._income['wage'] + self._income['bonus']
        return res


worker_1 = Position('Vasya', 'Dilt', 'developer', 1000, 200)
worker_2 = Position(surname='Wolt', name='Vika', position='teacher', wage=10000, bonus=300)

print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_1.name)
print(worker_1.surname)
print(worker_1.position)

print(worker_2.get_full_name())
print(worker_2.get_total_income())
print(worker_2.name)
print(worker_2.surname)
print(worker_2.position)
