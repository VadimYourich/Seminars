# 3.	Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.
#sum = 0


# list=[]
# for i in range(10,100):
#     if i%9==0:
#         list.append(i)
# print(list)

li = [i for i in range(10,100) if i%9==0]
# print(sum(list))
res = list(map(lambda x:x**2,filter(lambda x:x%9==0,range(10,100))))
print(sum(res))