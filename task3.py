import matplotlib.pyplot as plt
import numpy as np
import math

x = [[-1, -1, -1],
     [-1, -1, 1],
     [-1, 1, -1],
     [-1, 1, 1],
     [1, -1, -1],
     [1, -1, 1],
     [1, 1, -1],
     [1, 1, 1]]

d = [-1, 1, -1, 1, -1, 1, -1, -1]

l = 0.01

N = 10000

def f(x):
    return 2 / (1 + math.exp(-x)) - 1

def df(x):
    return (1 / 2) * (1 + f(x)) * (1 - f(x))

