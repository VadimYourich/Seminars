# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

print('Вводите числа, по окончанию введите 0: ')
n = None
list = []
while n != 0:
    n = int(input())
    list.append(n)
print(list)
new_list = []
for i in list:
     if list.count(i) == 1:
         new_list.append(i)
print(new_list)