""" Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

my_list = []
with open('english_numbers.txt', 'r', encoding='UTF-8') as file:
    for i in file:
        i = i.splitlines()
        for q in i:
            var = q.split(' — ')
            my_list.append(var)

my_dict = dict(my_list)
my_new_dict = {}
my_list_ = ['Один', 'Два', 'Три', 'Четыре']
idx = 0

for spam in my_dict.values():
    my_new_dict[my_list_[idx]] = spam
    idx += 1

my_new_list = []
for var_1, var_2 in my_new_dict.items():
    my_new_list.append([var_1, ' — ', var_2, '\n'])

with open('russian_numbers.txt', 'w', encoding='UTF-8')as new_file:
    for itm in my_new_list:
        new_file.writelines(itm)
