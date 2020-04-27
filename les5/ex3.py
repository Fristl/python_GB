"""Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

my_list = []
d = []
var_2 = 0
with open('my_file_3.txt', 'r', encoding='UTF-8') as file:
    var = len(file.readlines())
    file.seek(0)
    for i in range(var):
        text = file.readline().splitlines()
        my_list.append(text)
    for spam in my_list:
        for itm in spam:
            d.append(itm.split(' '))
    d = dict(d)
    for q, item in d.items():
        if int(item) < 20000:
            print(f'Сотрудник {q} имеет зарплату менее 20000 рублей')
        var_2 += int(item)
        var_3 = len(d)
    average_salary = var_2 / var_3
    print(f'Средняя величина дохода: {average_salary}')
