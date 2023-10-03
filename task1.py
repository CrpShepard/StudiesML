from sympy import *
import numpy as np
import math
import matplotlib.pyplot as plt

def numerical_derivative(f, x, h=0.001):
    return (f(x + h) - f(x)) / h

def f(x):
    return math.exp(-x)

def task_1():
    h = 0.001
    n = 1
    l = -5.0
    r = 5.0
    x = l
    ymin = math.exp(-x)
    xmax = x
    xp = []
    yp = []
    nfound = n

    while x <= r:
        fx = math.exp(-x)
        a = x - numerical_derivative(f, x) * h

        print("f(x):", fx, "an:", a, "n:", n, "diff", numerical_derivative(f, x))

        if fx < ymin:
            ymin = fx
            xmax = x
            nfound = n


        xp.append(x)
        yp.append(fx)

        x = x + h
        n = n + 1

    print("x:", xmax, "n", nfound)
    plt.plot(xp, yp)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xticks(np.arange(l, r + 1, step=1))
    plt.show()

task_1()