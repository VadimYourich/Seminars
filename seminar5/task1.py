# 1.	В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Входные данные	Выходные данные
# 1 2 3 5 6 7 8 	4
path = 'file.txt'
date = open(path, 'r')
a = date.read().split()
a = list(map(int, a))
print(a)
date.close()
for i in range(1, len(a)):
    if a[i] != a[i - 1] + 1:
        print(a[i - 1] + 1)