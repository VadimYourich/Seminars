# a: int = 0 # int
# b = 'tdfg' # str
# c = 0.5 # float
# t = True # bool
#
# for i in range(5):
#     print('Мама')
#
# i = 0
# while i < 5:
#     print('Мама')
#     i += 1
# n = 567
# print(n // 10)
# print(n % 10)
# sp = list()
# sp = []
# sp.append(5)
# sp.append(8)
# print(sp)
# sp = [1, 5, 3, 89, 3]
# # print(sp[0])
# # print(sp[3])
# # print(sp[-1])
# for i in range(0, len(sp)):
#     print(sp[i], end=' ')
# # print()
# for el in sp:
#     print(el, end=' ')
# # print(*sp)

# sp1 = [1, 5, 3]
# sp2 = sp1.copy() #копия списка
# sp2 = sp1[:] #срез всего списка, получается копия списка

# проверка на полиндром
# n = input('Введите число ')
# n2 = n[::-1]
# if n2 == n:
#     print('Палиндром')
# else:
#     print('Не палиндром')

# заполнение списка с консоли
# print('Вводите числа, по окончанию введите 0: ')
# n = None
# list = []
# while n != 0:
#     n = int(input())
#     list.append(n)
# print(list)

# счётчик элементов списка
# list = [2, 3, 4, 5, 6, 5]
# new_list = []
# for i in list:
#      if list.count(i) == 1:
#          new_list.append(i)
# print(new_list)

# def func(x):
# return x ** 2
#
# res = func(3)
# print(res)

# res = lambda x: x ** 2
# print(res(3))

# def ispositive(x):
#return x > 0
#
# sp = [1, -5, 3, -7, 8]
# res = list(filter(ispositive, sp))
# res = list(filter(lambda s: s > 0, sp))
# print(res)


# def kvadrat(x):
# return x ** 2

# sp = [1, 2, 3, 4, 5]
# res = list(map(kvadrat, sp))
# res = list(map(lambda a: a ** 2, sp))
# print(res)

# Сортировка
# sp = ['rrr', 'z', 'tyjuuu', 'aaaaaaaaaaa']
# sp.sort(key=lambda a: -len(a))
# sp.sort(key=lambda a: len(a), reverse=True)
# print(sp)
#
# sp = [['a', 66], ['b', 66], ['c', 1], ['d', 1]]
# sp.sort(key=lambda x: (-x[1], x[0]))
# print(sp)

# Списочные выражения
# sp = [i * 10 for i in range(1, 100) if i % 4 == 0]
# print(sp)

# a, b, c = [int(i) for i in input("Введите значения A,B,C: ").split()]
#print(a + b + c)

# функция работает с двумя списками, объединяет по-элементно и обрезает по длине меньшего списка
# sp1 = [1, 2, 3, 4, 5, 6]
# sp2 = [10, 20, 30, 40, 33]
# for i, j in zip(sp1, sp2):
#     print(i, j)

# функция для нумерования элементов списка
# sp = ['a', 'b', 'c']
# for i, el in enumerate(sp, 1):
#     print(i, el)

#работа с форматом csv
# import csv
#
##чтение с файла
# lst = []
# with open("file.csv", encoding='utf-8') as r_file:
# reader_object = csv.reader(r_file, delimiter=";")  #delimiter - разделитель
# for row in reader_object:
# lst.append(row)
#
##запись в файл
# with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
# file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")   #lineterminator - удаляет пустые строки
# for row in lst:
# file_writer.writerow(row)

# #запись логов в файл
# import logging
# logging.basicConfig (filename='log.txt',
#                     filemode='a',
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.DEBUG, encoding="UTF-8")

# #обработка ошибок
# try:
#     select = int(input("    Выберите команду: "))
#     if not select in [1, 2, 3, 4, 5, 6, 7]:
#         raise ValueError
#     return select
# except Exception:
#     print("\nВведена неверная команда!")
#     exit()

# #ввод через пробел
# print("\nВведите через пробел номера сотрудников для вывода на экран: ", end='')
# numbers = [int(n) for n in input().split()]