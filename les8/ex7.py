"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real: int, imaginary: int):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return complex((self.real + other.real), (self.imaginary + other.imaginary))

    def __mul__(self, other):
        return complex((self.real * other.real - self.imaginary * other.imaginary),
                       (self.imaginary * other.real + self.real * other.imaginary))

num_1 = ComplexNumber(5, 2)
num_2 = ComplexNumber(13, 21)

assert num_1 + num_2 == complex(5, 2) + complex(13, 21)
assert num_1 * num_2 == complex(5, 2) * complex(13, 21)
