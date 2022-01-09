from sympy import *
epsilon = 10**-4
t = symbols('t')
s = symbols('s')
a = 0
b = 1


def Volter():
    countIteration = 1
    x = Lambda(t, 0)
    prev = Lambda(t, 0)
    x = Lambda(t, integrate( (t - s) * x(s), (s, a, t)) + 1)
    while ((maximum(x(t) - prev(t), t, Interval(a, b)) > epsilon) or (maximum(prev(t) - x(t), t, Interval(a, b)) > epsilon)):
        prev = x
        x =  Lambda(t, integrate( (t - s) * x(s), (s, a, t)) + 1)
        countIteration += 1

    return x, countIteration


x, countIteration = Volter()
print("Решение : ", x(t))
print("Количество итераций : ", countIteration)