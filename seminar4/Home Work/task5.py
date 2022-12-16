# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('task5_1.txt') as f1:
    first_pol = f1.read()
with open('task5_2.txt') as f2:
    second_pol = f2.read()
print(first_pol, second_pol, sep='\n')
def delete_symbols(pol):
    pol = pol.split()
    sp_pol = []
    for el in pol:
        if el == '+' or el == '=' or el == '0':
            continue
        else:
            sp_pol.append(el)
    return sp_pol
def dictionary(sp_pol):
    slovar = {}
    for el in sp_pol:
        if 'x**' in el:
            cort = el.split('x')
            if cort[0] == '':
                slovar[f'x{cort[1]}'] = '1'
            else:
                slovar[f'x{cort[1]}'] = f'{cort[0]}'
        elif 'x' in el:
            cort = el.split('x')
            if cort[0] == '':
                slovar[f'x{cort[1]}'] = '1'
            else:
                slovar[f'x{cort[1]}'] = f'{cort[0]}'
        else:
            cort = (el, '**0')
            slovar[f'{cort[1]}'] = f'{cort[0]}'
    return slovar
def summa(sl_1, sl_2):
    sum_sl = {}
    if len(sl_1) >= len(sl_2):
        big_sl = sl_1
        small_sl = sl_2
    else:
        big_sl = sl_2
        small_sl = sl_1
    for key, value in big_sl.items():
        if key in small_sl:
            sum_sl[key] = int(big_sl[key]) + int(small_sl[key])
        else:
            sum_sl[key] = int(big_sl[key])
    for key, value in small_sl.items():
        if key not in big_sl:
            sum_sl[key] = int(small_sl[key])
    sum_sl = dict(sorted(sum_sl.items(), key=lambda x: x[0], reverse=True))
    return sum_sl
def res_polynomial(sum_slov):
    pol = []
    for key, value in sum_slov.items():
        if value == 1:
            c = f'{key}'
        else:
            c = f'{value}{key}'
        if key == '**0':
            c = f'{value}'
        pol.append(c)
    return pol
slovar_1 = dictionary(delete_symbols(first_pol))
slovar_2 = dictionary(delete_symbols(second_pol))
res_sl = summa(slovar_1, slovar_2)
result = ' + '.join(res_polynomial(res_sl)) + ' = 0'
print('Сумма многочленов равна: ')
print(result)
with open('task5_sum.txt', 'w') as file:
    file.write(result)