import numpy as np
import math

h = 1
an = np.array([10, 20])
mn = np.array([0, 0])
rn = np.array([0, 0])
Mn = np.array([0, 0])
Rn = np.array([0, 0])
B1=B2=0.5

def partdiff(x, y, delta=1e-5):
    arr = np.array([])
    df_dx = (f(x + delta, y) - f(x, y)) / delta
    df_dy = (f(x, y + delta) - f(x, y)) / delta
    arr = np.append(arr, df_dx)
    arr = np.append(arr, df_dy)
    return arr

def f(x, y):
    return x**2 + y**2

def grad(a):
    return partdiff(a[0], a[1])

def m(n):
    global mn
    #res = B1 * mn[n - 1] + (1 - B1) * grad(an[n - 1])
    res = B1 * np.array(mn[-2], mn[-1]) + (1 - B1) * grad((an[-2], an[-1]))
    mn = np.append(mn, res)
    return res

def r(n):
    global rn
    #res = B2 * rn[n - 1] + (1 - B2) * (grad(an[n - 1]) ** 2)
    res = B2 * np.array(rn[-2], rn[-1]) + (1 - B2) * (grad((an[-2], an[-1])) ** 2)
    rn = np.append(rn, res)
    return res

def M(n):
    global Mn
    res = m(n) / (1 - B1 ** (n))
    Mn = np.append(Mn, res)
    return res

def R(n):
    global Rn
    res = r(n) / (1 - B2 ** (n))
    Rn = np.append(Rn, res)
    return res

def a(n):
    #return an[n-1] - ((h * M(n))) / (np.sqrt(R(n)) + math.e)
    return (an[-2], an[-1]) - ((h * M(n))) / (np.sqrt(R(n)) + math.e)

def finda(n):
    global an
    for i in range(1, n + 1):
        an = np.append(an, a(i))
    return an[-2], an[-1]

print(finda(2))
print(an)