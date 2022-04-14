import matplotlib.pylab as plt
import numpy as np


def funtion_1(x):
    return 0.01 * x ** 2 + 0.1 * x


def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


x = np.arange(0.0, 20.0, 0.1)
y = funtion_1(x)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()

print(numerical_diff(funtion_1,5))
print(numerical_diff(funtion_1,10))