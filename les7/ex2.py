"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod

class Clothes(ABC):

    @property
    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):

    def __init__(self, parameter):
        self.V = parameter

    @property
    def calculation(self):
        self.res = (self.V / 6.5 + 0.5)
        return self.res


class Suit(Clothes):

    def __init__(self, parameter):
        self.H = parameter

    @property
    def calculation(self):
        self.res = (2 * self.H + 0.3)
        return self.res


a = Coat(100.5)
b = Suit(100.0)

print(f'{a.calculation:.2f}')
print(f'{b.calculation:.2f}')
