# 4.	Напишите программу, которая будет преобразовывать десятичное число в двоичное
# (встроенными методами пользоваться нельзя).
#
# Пример:
# o	45 -> 101101
# o	3 -> 11
# o	2 -> 10

# n = int(input('Введите целое число: '))
# osn = 2
# list = []
# while n != 0:
#     list.append(n % osn)
#     n //= osn
# list.reverse()
# print(*list, sep='')

n = int(input('Введите целое число: '))
osn = 2
res = ''
while n > 0:
    res = str(n % osn) + res
    n //= osn
print(res)


# n = int(input('Введите целое число: '))
# x = bin(n)
# print(x)
# print(int(x, 2))