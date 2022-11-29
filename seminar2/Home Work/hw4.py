# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число N: '))
sp = []
for i in range(-n, n + 1):
    sp.append(i)
print(sp)

print('Введите', int(n / 2), 'позиции элементов в диапазоне от ', 0, ' до ', n * 2 + 1, ': ')
sp2 = []
for i in range(int(n / 2)):
    sp2.append(input())
# print(sp2)

file = open('file.txt','w')
def value(items):
    for item in items:
        print(item, file=file)
    file.close()

value(sp2)

pr = 1
with open('file.txt') as f:
    for line in f:
        pr *= sp[int(line)]
print('Произведение элементов на указанных позициях равно: ', pr)


