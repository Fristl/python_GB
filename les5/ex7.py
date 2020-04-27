"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json

text = []

with open('my_file_7.txt', 'r', encoding='UTF-8') as file:
    for i in file:
        text.append(i.split(' '))

for itm in text:
    spam = len(itm[3]) - 1
    itm[3] = (itm[3])[:spam]

profit = []
average_profit = 0
name_firm = []

for item in text:
    try:
        res = float(item[2]) - float(item[3])
        profit.append(res)
        name_firm.append(item[0])
    except:
        print('Проверьте правильность записи данных в файл')
        break

sum_firm = 0
for idx in profit:
    if idx >= 0:
        average_profit += idx
        sum_firm += 1

average_profit = average_profit / sum_firm

my_dict = dict(zip(name_firm, profit))

average_profit_dict = {}
average_profit_dict['average_profit'] = average_profit

result_list = [my_dict, average_profit_dict]

with open('file_7.json', 'w', encoding='UTF-8') as file_json:
    json.dump(result_list, file_json)
