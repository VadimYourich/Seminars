import logging


def choosing_an_action():
    print('Выберете действие:\n1 - чтение\n2 - запись')
    select = int(input())
    while select not in [1, 2]:
        logging.info('Команда выбрана некорректно!')
        select = int(input('Введите 1 или 2 '))
    return select


def format_selection():
    print('Выберете формат файла:\n1 - .txt\n2 - .csv')
    select = int(input())
    while select not in [1, 2]:
        logging.info('Команда выбрана некорректно!')
        select = int(input('Введите 1 или 2 '))
    return select


def print_data(data):
    for i in range(len(data)):
        if i == 0:
            for key in data[i]:
                print('  ' + key, end=' ')
            print()
            print(i + 1, end=' ')
            for key, value in data[i].items():
                print(value, end=' ')
        else:
            print(i + 1, end=' ')
            for key, value in data[i].items():
                print(value, end=' ')
        print()
