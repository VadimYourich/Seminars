# 2.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# import random
# quantity = 121
# max_step = 28
# first = random.randint(1,2)
# while quantity > max_step:
#     while True:
#         x = int(input(f'{first} игрок, заберите не более {max_step} конфет: '))
#         if 0 < x <= max_step:
#             quantity -= x
#             print(f'Осталось {quantity} конфет')
#             if first == 1:
#                 first = 2
#             elif first == 2:
#                 first = 1
#             break
#         else:
#             print(f'Максимальное количество конфет за один ход {max_step}!')
# if first == 1:
#     print('Победил 1-й игрок!')
# else:
#     print('Победил 2-й игрок!')


import random
quantity = 121
max_step = 28
first = random.randint(1,2)
while quantity > max_step:
    if first == 2:
        if max_step + 1 < quantity <= max_step * 2 + 1:
            x = quantity - 29
            print(f'Бот забрал {x} конфет')
            quantity -= x
            print(f'Осталось {quantity} конфет')
            first = 1
        elif 0 < quantity <= max_step:
            x = quantity
            print(f'Бот забрал {x} конфет')
            quantity -= x
            print(f'Осталось {quantity} конфет')
            first = 1
        else:
            x = random.randint(1,max_step)
            print(f'Бот забрал {x} конфет')
            quantity -= x
            print(f'Осталось {quantity} конфет')
            first = 1
    else:
        while True:
            x = int(input(f'Заберите не более {max_step} конфет: '))
            if 0 < x <= max_step:
                quantity -= x
                print(f'Осталось {quantity} конфет')
                break
            else:
                print(f'Максимальное количество конфет за один ход {max_step}!')
        first = 2
if first == 1:
    print('Вы победили!')
else:
    print('Победил Бот!')