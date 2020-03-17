import matplotlib.pyplot as plt
import numpy as np
import math
import sympy

# 100 linearly spaced numbers
x = np.linspace(-100, 100, 1000)

y = (x ** 2) / (x ** 2 + 1)

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
# die Asympthote ist die Gerade y = 1.

plt.plot(x, y, 'r')
plt.plot(x, [1] * 1000)

taylor = 0
a = sympy.Symbol('x')
func = (a ** 2) / (a ** 2 + 1)
start = 0
for i in range(3):
    newTerm = ( (a - start) **i / math.factorial(i) ) * func.subs(a, start)
    print(newTerm)
    func = sympy.diff(func, a)
    taylor += newTerm

# show the plot

#plt.plot(x,taylor,'r')

ytaylor = []
for val in x:
    ytaylor.append(taylor.subs(a, val))

plt.plot(x, ytaylor, 'g')
plt.show()

