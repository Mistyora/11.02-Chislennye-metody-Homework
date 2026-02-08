import math

def f(x):
    return 2 - x - math.log(x)

a, b, h = float(input()), float(input()), float(input())
if a <= 0:
    print("Функция ln(x) определена только для x > 0")

x1 = a
x2 = x1 + h
y1 = f(x1)
print("Уравнение имеет 1 корень на интервале: ")
while x2 <= b:
    y2 = f(x2)
    if y1 * y2 <= 0:
        print(round(x1, 2), round(x2, 2))

    x1 = x2
    x2 += h
    y1 = y2