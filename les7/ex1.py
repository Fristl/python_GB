"""Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""

class Matrix:

    def __init__(self, matrix_as_list):
        self.matrix = matrix_as_list

    def __str__(self):
        for lines in self.matrix:
            if len(lines) == len(self.matrix[0]):
                continue
            else:
                return 'Введённые данные, нельзя преобразовать к матрице!\n'
        self.my_str = ''
        for line in self.matrix:
            for item in line:
                self.my_str += str(item) + ' '
            self.my_str += '\n'
        return self.my_str



    def __add__(self, other):
        res = []
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            for idx, line in enumerate(self.matrix):
                tmp_res = []
                for index, item in enumerate(line):
                    tmp_res.append(self.matrix[idx][index] + other.matrix[idx][index])
                res.append(tmp_res)
            return Matrix(res)
        else:
            return 'Эти матрицы нельзя сложить! \n'


a = Matrix([[1, 2, 3, 40], [5, 6, 7, 8], [9, 0, 1, 2]])
b = Matrix([[0, 2, 3, 4], [5, 6, 7, 15], [9, 1, 1, 2]])
c = a + b

print(a)
print(b)
print(c)
