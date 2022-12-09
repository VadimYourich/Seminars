# 4.	Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк
# некое число.
# Входные данные	Выходные данные
# 12
# Строка1
# Строка2
# Строка3
# Строка45
# Стр12ка	        да

# number = 12
# list = []
# f = 0
# print('Введите элементы списка')
# for i in range(5):
#     list.append(input())
# for i in range(5):
#     if str(number) in list[i]: #if list[i] == str(number): если нужно, соответствие всей строки
#         f = 1
# if f:
#     print('Да')
# else:
#     print('Нет')

list = []
print('Введите элементы списка')
for i in range(5):
    list.append(input())
if any('12' in el for el in list):
    print('Yes')
else:
    print('No')