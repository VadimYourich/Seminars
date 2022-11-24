#2.	Напишите программу для.проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x = 0
y = 0
z = 0
for х in range(1):
    for y in range(1):
        for z in range(1):
            if not(x or y or z) == (not x) and (not y) and (not z):
                print('true')
            else:
                print('false')