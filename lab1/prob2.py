

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
x = np.arange(-10000, 10000, 8.25)
y = np.arange(-10000, 10000, 8.25)
x, y = np.meshgrid(x, y)
Z = (1 - x ) ** 2 + (100 * (y - x ** 2) ** 2)

# Plot the surface.
surf = ax.plot_surface(x, y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


plt.show()
