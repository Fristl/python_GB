"""Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

my_list = []
while True:
    b = input('Введите текст: ')
    my_list.append(b)
    if b == '':
        break

with open('my_file_1.txt', 'w') as file:
    for itm in my_list:
        file.write(itm + '\n')
