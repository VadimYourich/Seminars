# 4.	Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).

x = int(input('Введите номер четверти '))

if x == 1:
    print('в этой четверти X > 0 и Y > 0')
elif x == 2:
    print('в этой четверти X < 0 и Y > 0')
elif x == 3:
    print('в этой четверти X < 0 и Y < 0')
elif x == 4:
    print('в этой четверти X > 0 и Y < 0')
else:
    print('не верный номер')