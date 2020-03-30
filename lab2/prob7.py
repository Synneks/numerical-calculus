import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def CS(n):
    x = np.linspace(-1,1,n+1)
    y = 1 / (1 + ( 25 * ( x ** 2 ) ))
    print(len(x))
    cs = CubicSpline(x, y)
    xs = np.arange(-1, 1, 1/n)


    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x, y, 'o')
    plt.plot(xs, 1 / (1 + ( 25 * ( xs ** 2 ) )))
    plt.plot(xs, cs(xs), label="S")

    plt.xlim(-0.5, 9.5)
    plt.legend(loc='upper right', ncol=2)
    plt.show()

CS(10)
CS(20)
CS(30)