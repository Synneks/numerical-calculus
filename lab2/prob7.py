import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def CS(n):
    x = np.linspace(-1,1,n+1)
    y = 1 / (1 + ( 25 * ( x ** 2 ) ))
    print(len(x))
    cs = CubicSpline(x, y)
    xs = np.linspace(-1,1,n+1)

    plt.plot(xs, cs(xs), label="S")

   
    plt.show()

#CS(10)
#CS(20)
CS(30)