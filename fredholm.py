from sympy import *

lambda_param = 1/3
a = 0
b = 1
epsilon = 10**-3
t = symbols('t')
s = symbols('s')


def Fredgolm():
        countIteration = 1
        x = Lambda(t, 0)  # start value x0() = 0
        prev = Lambda(t, 0)
        x = Lambda(t, lambda_param * integrate(cos(pi * (t - s)) * x(s), (s, a, b)) + 1)
        while( (maximum(x(t) - prev(t), t, Interval(a, b)) > epsilon) or (maximum(prev(t) - x(t), t, Interval(a, b)) > epsilon) ):
                prev = x
                x = Lambda(t, lambda_param * integrate( cos(pi*(t - s))*x(s), (s, a, b)) + 1 )
                countIteration += 1
        return x, countIteration


x, count = Fredgolm()
print("Решение = ", x(t))
print("Количество итераций = ", count)