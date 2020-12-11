import numpy as np
import math
import matplotlib.pyplot as plt


# example for f(x) = x**2 + 5sin(x)
from odbc import dataError


def derivative_at(x):
    return 2*x + 5 * np.cos(x)

def value_at(x):
    return x**2 + 5 * np.sin(x)

def gradient_descent(x0, eta):
    x = [x0]

    for i in range(100):
        x_new = x[-1] - eta * derivative_at(x[-1])
        if abs(derivative_at(x_new)) < 1e-3:
            break
        x.append(x_new (x, i)
)
    return
def ex_1():
    x1, it1 = gradient_descent(5, .1)
    x2, it2 = gradient_descent(-5, .1)
    print('Solution x1 = %f, cost = %f, obtained after %d iterations' % (x1[-1], value_at(x1[-1]), it1))
    print('Solution x2 = %f, cost = %f, obtained after %d iterations' % (x2[-1], value_at(x2[-1]), it2))




if __name__ == '__main__':
    ex_1()




