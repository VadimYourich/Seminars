a: int = 0 # int
b = 'tdfg' # str
c = 0.5 # float
t = True # bool
#
# for i in range(5):
#     print('Мама')
#
# i = 0
# while i < 5:
#     print('Мама')
#     i += 1
# n = 567
# print(n // 10)
# print(n % 10)
# sp = list()
# sp = []
# sp.append(5)
# sp.append(8)
# print(sp)
sp = [1, 5, 3, 89, 3]
# print(sp[0])
# print(sp[3])
# print(sp[-1])
for i in range(0, len(sp)):
    print(sp[i], end=' ')
print()
for el in sp:
    print(el, end=' ')
print(*sp)

sp1 = [1, 5, 3]
sp2 = sp1.copy() #копия списка
sp2 = sp1[:] #срез всего списка, получается копия списка
