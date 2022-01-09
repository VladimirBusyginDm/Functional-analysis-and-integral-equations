import matplotlib.pyplot as plt
import numpy as np

epsilon = pow(10, -4)
f = lambda x : 3*x + np.log(1 + pow(x, 2)) + np.sin(x) + np.cos(x) - 7
phi = lambda x : -(np.log(1 + pow(x, 2)) + np.sin(x) + np.cos(x) - 7) / 3
x = np.linspace(-5, 5, 100)
plt.plot(x, phi(x))
plt.show()


def method(startValue):
    countIteration = 1
    x0 = startValue
    x = phi(x0)
    while(abs(phi(x) - x) >= epsilon):
        countIteration += 1
        x = phi(x)
    return x, countIteration


def Dihotomia() :
    x0, x1 = 1000000, -10000000
    x = 0
    while(True) :
        x = (x0 + x1) / 2
        if (abs(f(x0)) < 0.5):
            break
        elif (f(x0) * f(x) < 0) :
            x1 = x
        else :
            x0 = x

    return x0, x1


border1, border2 = Dihotomia()
print("Границы : [", border2, ",",border1,"]")
x0 = (border1 + border2)/2
print("x0 = ", x0)
x, countIter = method(x0)
print("Решение : ", x, "\nИтерации : ", countIter)
print("Невязка = ", f(x))


