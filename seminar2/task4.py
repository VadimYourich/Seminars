# 4.	Напишите программу, которая проверяет пятизначное число на палиндром.
count = 0
n = input('Введите число')
for i in range(len(n) // 2):
    if n[i] == n[-i - 1]:
        count += 1
if count == len(n) // 2:
    print('Палиндром')
else:
    print('НЕ Палиндром')


