"""Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран."""

res = 0
my_list = []
with open('my_file_5.txt', 'w', encoding='UTF-8') as file:
    while True:
        try:
            number = float(input('Введите число: '))
        except:
            print('Ошибка ввода, вводите только числа')
            continue
        my_list.append(str(f'{number} '))
        var = input('Хотите завершить ввод? да/нет : ')
        if var == 'да':
            break
    for i in my_list:
        file.writelines(i)

with open('my_file_5.txt', 'r', encoding='UTF-8') as file_2:
    b = file_2.readline()
    b = b.split(' ')
    for itm in b:
        if itm != '':
            res += float(itm)
    print(f'Сумма чисел в файле равна: {res}')
