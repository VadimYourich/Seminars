# 2.	Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет,
# можно ли из этих отрезков составить треугольник.
# Входные данные	        Выходные данные
# triangle(1, 1, 2)	    Это не треугольник
# triangle(7, 6, 10)      Это треугольник

a = 5
b = 4
c = 3
def triangle(a, b, c):
    if a + b > c and b + c > a and c + a >b:
        return True
    return False
print(triangle(a, b, c))