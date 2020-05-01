"""Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра."""

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки ручкой. Рисуем {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашём. Рисуем {self.title}')



class Handle(Stationery):

    def draw(self):
        return f'Рисует маркер. Русуем чудо {self.title}'

obj_1 = Stationery('Cow')
obj_1.draw()

obj_2 = Pen('Dog')
obj_2.draw()

obj_3 = Pencil('Cat')
obj_3.draw()

obj_4 = Handle('CatDog')
print(obj_4.draw())
