"""Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""

class Date:

    def __init__(self, date: str):
        self.date = date


    @classmethod
    def extraction(cls, date: str):
        try:
            day, month, year = map(int, date.split('-'))
            res = cls(date)
            print(f'{day:>02}.{month:>02}.{year}')
            return res
        except:
            return 'Неверный формат ввода.'

    @staticmethod
    def validation(date: str):
        my_dict_1 = {1: 31, 2: 28, 3: 31, 4: 30,
                     5: 31, 6: 30, 7: 31, 8: 31,
                     9: 30, 10: 31, 11: 30, 12: 31}
        my_dict_2 = {2: 29}

        day, month, year = map(int, date.split('-'))

        if 1 <= day <= 31 and 1 <= month <= 12 and len(str(year)) == 4:
            if (year % 4) == 0 and month == 2 and not day > my_dict_2[month]:
                return 'Проверка пройдена успешно'
            elif not day > my_dict_1[month]:
                return 'Проверка пройдена успешно'
            else:
                return 'Ошибка ввода, проверка не пройдена.'
        else:
            return 'Ошибка ввода, проверка не пройдена.'


Date.extraction('31-10-1510')
print(Date.validation('29-02-2020'))

a = Date.extraction('28-02-2019')
print(a.date)
