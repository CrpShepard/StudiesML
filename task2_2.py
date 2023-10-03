import math

hn = [1]
T = 1
an = [1]

def diff(f, x, h):
    return (f(x + h) - f(x)) / h

def f(x):
    return x**2

def h(n):
    global hn
    hn.append(hn[0] * (math.exp(-n / T)))

def a(n):
    return an[n - 1] - diff(f, an[n - 1]) * hn[n - 1]

def finda(n):
    for i in range(1, n + 1):
        h(i)
        an.append(a(i))
    return an

finda(3)
print("an", an)
print("h", hn)