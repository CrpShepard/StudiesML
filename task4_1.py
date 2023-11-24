import numpy as np
import random

a = np.array([[0, 0]])
h = 0.1

x = np.array([-1, 0, 1])
y = np.array([1, 0, -1])

def Fnn(n):
    return a[0] + a[1] * x[n]


