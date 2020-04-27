"""Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке."""

with open('my_file_2.txt', 'r', encoding='UTF-8') as file:
    text = file.readlines()
    print(f'В файле {len(text)} строк(и)')
    file.seek(0)
    for itm, i in enumerate(text):
        b = i.split(' ')
        print(f'В {itm+1} строке {len(b)} слов(а)')
