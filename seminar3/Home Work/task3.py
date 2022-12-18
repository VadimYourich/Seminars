# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5, 10.01]
# list_dr = []
# for i in range(0, len(list)):
#     if (list[i] - int(list[i])) != 0:
#         list_dr.append(round((list[i] - int(list[i])), 2))
# max_dr = max(list_dr)
# min_dr = min(list_dr)
# print(list)
# print((max_dr - min_dr))

list = [1.1, 1.2, 3.1, 5, 10.01]
list_dr = [round(abs(i - int(i)), 4) for i in list if int(i) != i]
print(list)
print(list_dr)
print(max(list_dr) - min(list_dr))