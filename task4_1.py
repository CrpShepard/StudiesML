import numpy as np

a = np.array([[0, 0]])
h = 0.1

def LdW0(W0):
    return 6 * W0

def LdW1(W1):
    return 4 * W1 + 4

def dLW(W0, W1):
    return np.array([LdW0(W0), LdW1(W1)])

def an(n):
    return a[n - 1] - h * dLW(a[n - 1][0], a[n - 1][1])

def findan(n):
    global a
    for i in range(1, n + 1):
        a = np.append(a, [an(i)], axis=0)

findan(2)
print(a[2])