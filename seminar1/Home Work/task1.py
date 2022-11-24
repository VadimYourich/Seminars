# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Введите цифру, соответствующую дню недели: '))
if number == 6 or number == 7:
    print('это выходной!')
elif number > 0 and number < 6:
    print('это рабочий день)')
else:
    print('нет такого дня недели!')