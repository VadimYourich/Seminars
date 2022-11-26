# 4.	Напишите программу, которая проверяет пятизначное число на палиндром.


# f = 1
# n = input('Введите число ')
# for i in range(len(n) // 2):
#     if n[i] != n[-i - 1]:
#         print('НЕ Палиндром')
#         f = 0
#         break
# if f:
#     print('Палиндром')


# count = 0
# n = input('Введите число ')
# for i in range(len(n) // 2):
#     if n[i] == n[-i - 1]:
#         count += 1
# if count == len(n) // 2:
#     print('Палиндром')
# else:
#     print('НЕ Палиндром')


n = input('Введите число ')
n2 = n[::-1]
if n2 == n:
    print('Палиндром')
else:
    print('НЕ Палиндром')

