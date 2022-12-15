# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('Введите натуральную степень многочлена k: '))
ratio_random = []
for i in range(0, k + 1):
    ratio_random.append(random.randint(0, 99))
def polynomial(k, ratio):
    pol = []
    for i in range(0, len(ratio) - 2):
        if ratio[i] == 0:
            continue
        elif ratio[i] == 1:
            x = f'x**{k - i}'
        else:
            x = f'{ratio[i]}x**{k - i}'
        pol.append(x)
    for i in range(len(ratio) - 2, len(ratio) - 1):
        if ratio[i] == 0:
            continue
        elif ratio[i] == 1:
            x = 'x'
        else:
            x = f'{ratio[i]}x'
        pol.append(x)
    for i in range(len(ratio) - 1, len(ratio)):
        if ratio[i] == 0:
            continue
        else:
            x = f'{ratio[i]}'
        pol.append(x)
    return pol

res_polynomial = ' + '.join(polynomial(k, ratio_random)) + ' = 0'
print(res_polynomial)

with open('task4.txt', 'w') as file:
    file.write(res_polynomial)