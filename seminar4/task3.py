# 3.	Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
count = 1
maximum = max(x, y)
if maximum % x == 0 and maximum % y == 0:
    print(maximum)
else:
    for count in range(2, min(x, y) + 1):
        if (maximum * count) % x == 0 and (maximum * count) % y == 0:
            print(maximum * count)
            break