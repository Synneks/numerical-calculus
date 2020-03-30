import scipy.interpolate
import matplotlib.pyplot as plt
import numpy as np

n = 71
x = np.arange(0, n, 1)
ox = np.arange(0, n, 1)
y = np.cos(((2 * x + 1) * np.pi) / (2 * n + 1))

yn = scipy.interpolate.barycentric_interpolate(x, y, ox)
plt.title = 'Barycentric n = 69'
plt.plot(ox, yn)
plt.show()
