import numpy as np

a = np.array([[0, 0]])
h = 0.1
c = 1

def LregdW0(W0, W1):
    return 6*W0 + 6*W1 + 2*c*W0 - 12

def LregdW1(W0, W1):
    return 6*W0 + 10*W1 + 2*c*W1 - 16

def dLregW(W0, W1):
    return np.array([LregdW0(W0, W1), LregdW1(W0, W1)])

def an(n):
    return a[n - 1] - h * dLregW(a[n - 1][0], a[n - 1][1])

def findan(n):
    global a
    for i in range(1, n + 1):
        a = np.append(a, [an(i)], axis=0)

findan(2)
print(a[2])

