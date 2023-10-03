import numpy as np

h = 0.1
a = np.array([1, 2])
g = 2

def partdiff(x, y, delta=1e-5):
    arr = np.array([])
    df_dx = (f(x + delta, y) - f(x, y)) / delta
    df_dy = (f(x, y + delta) - f(x, y)) / delta
    arr = np.append(arr, df_dx)
    arr = np.append(arr, df_dy)
    return arr

def grad(a):
    return partdiff(a[0], a[1])

def f(x, y):
    return x ** 2 + y ** 2

def an(n):
    return g * np.array(a[-2], a[-1]) - h * grad((a[-2], a[-1]))

def finda(n):
    global a
    for i in range(1, n + 1):
        a = np.append(a, an(i))
    return a[-2], a[-1]

print(finda(2))
print(a)