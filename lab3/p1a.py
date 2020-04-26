import matplotlib.pyplot as plt

def compute_function_coeff(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    a = sum((x[i] - x_mean) * y[i] for i in range(len(x))) / sum((xi - x_mean) ** 2 for xi in x)

    b = sum(x[i] * (y_mean * x[i] - x_mean * y[i]) for i in range(len(x))) / sum((xi - x_mean) ** 2 for xi in x)

    return (a, b)


def plot_function(x, y):
    (a, b) = compute_function_coeff(x, y)

    xx = [i for i in range(0, 200)]
    yy = [a * xx[i] + b for i in range(0, 200)]

    plt.plot(xx, yy)
    plt.show()


x = [i for i in range(1, 19)]
y = [1, 1, 3, 3, 3, 3, 4, 6, 6, 9, 13, 15, 17, 29, 47, 59, 89, 123]

plot_function(x, y)