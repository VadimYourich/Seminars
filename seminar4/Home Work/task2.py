# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите число N: '))
d = 2
list = []
while N > d:
    while N % d == 0:
        N = N / d
        list.append(d)
    d += 1
    if N == d:
        list.append(d)
        break
print('Простые множители числа N: ', list)