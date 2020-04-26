import matplotlib.pyplot as plt
import numpy as np
import math

SAMPLES = 31

x = np.linspace(1, 18, 18)
ox = np.linspace(1, SAMPLES, SAMPLES)
y = np.array([1, 1, 3, 3, 3, 3, 4, 6, 6, 9, 13, 15, 17, 29, 47, 59, 89, 123])

def compute_function_coeff_kQ(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    a = sum((x - x_mean) * y) / sum((x - x_mean) ** 2)
    b = sum(x * (y_mean * x - x_mean * y)) / sum((x - x_mean) ** 2)

    return (a, b)


(a, b) = compute_function_coeff_kQ(x, y)
oy_lin = a * ox + b

line1, = plt.plot(ox, oy_lin, color='red', label='Linear')

y_log = np.log(y)
(a_log, b_log) = compute_function_coeff_kQ(x, y_log)

oy_exp = np.exp(a_log * ox + b_log)
line2, = plt.plot(ox, oy_exp, color='orange', label='Exponential')

x_trunc = np.array([1, 4, 7, 10, 13, 16])
y_trunc = np.array([1, 3, 4, 9, 17, 59])

(a_trunc, b_trunc) = compute_function_coeff_kQ(x_trunc, y_trunc)
oy_trunc_lin = a * ox + b

line3, = plt.plot(ox, oy_trunc_lin, color='black', label='Truncated linear')

y_trunc_log = np.log(y_trunc)
(a_trunc_log, b_trunc_log) = compute_function_coeff_kQ(x_trunc, y_trunc_log)
oy_trunc_exp = np.exp(a_trunc_log * ox + b_trunc_log)

line4, = plt.plot(ox, oy_trunc_exp, color='blue', label='Truncated exponential')

plt.legend(handles=[line1, line2, line3, line4])
plt.show()

# Vorhersage fur die 30-te Tag.
# Die exponentielle ist fast 3 mal grosser (2999) als die aktuelle Wert (1029).
# Die lineare ist 135.
print(oy_lin[30])
print(oy_exp[30])

# Fur die fehlenden Daten
# Die exponentielle ist ~2 mal grosser (1977) als die aktuelle Wert (1029).
# Die linieare ist die gleiche mit der berechnet mit allen Daten.
print(oy_trunc_lin[30])
print(oy_trunc_exp[30])