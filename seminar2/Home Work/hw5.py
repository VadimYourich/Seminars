# Реализуйте алгоритм перемешивания списка(shuffle использовать нельзя, другие методы из библиотеки random - можно).


n = int(input('Введите колличество элементов нового списка: '))
print('Введите', n, 'элементов: ')
sp = []
for i in range(n):
    sp.append(input())
print('Оригинальный список', sp)

import random
for i in range(n):
    t = random.randint(0, n - 1)
    sp[i], sp[t] = sp[t], sp[i]
print('Перемешанный список', sp)

