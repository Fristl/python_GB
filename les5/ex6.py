"""Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета
и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

import re

my_dict = {}

with open('my_file_6.txt', 'r', encoding='UTF-8') as file:
    text = file.readlines()
    i = [var.split(' ') for var in text]

for txt in i:
    eny_var = len(txt[0]) - 1
    txt[0] = (txt[0])[:eny_var]
    my_dict[txt[0]] = txt[1:]

for key, val in my_dict.items():
    my_list = []
    for itm in val:
        my_list.append(itm.split('('))
    my_dict[key] = my_list

my_list_2 = []
for item_ in my_dict.values():
    res = 0
    for spam in item_:
        for var_itm in spam:
            if var_itm.isdigit():
                res += int(var_itm)
    my_list_2.append(res)

idx = 0
for key_2 in my_dict.keys():
    my_dict[key_2] = my_list_2[idx]
    idx += 1

print(my_dict)

print('__________________________________________________\nЗатем я узнал про модуль re\n')


my_list_result = []
my_new_list = []
with open('my_file_6.txt', 'r', encoding='UTF-8') as file_2:
    for var_3 in file_2:
        my_new_list.append(var_3)

for _spam_ in my_new_list:
    spam_list = re.findall('\d+', _spam_)
    new_res = 0
    for spam_1 in spam_list:
        new_res += int(spam_1)
    my_list_result.append(new_res)

for index, more_spam in enumerate(my_new_list):
    my_new_list[index] = more_spam.split(':')

my_new_dict = dict(my_new_list)

result = dict(zip(my_new_dict.keys(), my_list_result))
print(result)
