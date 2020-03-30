import scipy.interpolate
import matplotlib.pyplot as plt
import numpy as np

n = 30
x = np.linspace(-1, 1, n)
y = 1 / (1 + 25 * x ** 2)
print(x, y)
sp = scipy.interpolate.interp1d(x, y)
oy = sp(x)

plt.plot(x, y, x, oy)
plt.show()