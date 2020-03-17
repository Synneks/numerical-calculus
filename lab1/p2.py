import matplotlib.pyplot as plt
import numpy as np
from simpy import *

plt.style.use('seaborn-white')


def f(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


x = np.linspace(-1000, 1000, 1000)
y = np.linspace(-1000, 1000, 1000)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar
plt.show()