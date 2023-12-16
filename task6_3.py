import numpy as np

a = np.array([[0, 0]])
h = 0.1
p = 0.5

def Lx2dW0(W0, W1):
    return 8*W0 + 4*W1 - 2

def Lx2dW1(W0, W1):
    return 4*W0 + 4*W1 - 2

def Lx1dW0(W0, W2):
    return 8*W0 + 4*W2 - 2

def Lx1dW1(W0, W2):
    return 4*W0 + 4*W2 - 2

def dLx2W(W0, W1):
    return np.array([Lx2dW0(W0, W1), Lx2dW1(W0, W1)])

def dLx1W(W0, W2):
    return np.array([Lx1dW0(W0, W2), Lx1dW1(W0, W2)])

def an(n):
    return a[n - 1] - h * dLx2W(a[n - 1][0], a[n - 1][1])

def findan(n):
    global a
    for i in range(1, n + 1):
        a = np.append(a, [an(i)], axis=0)

#findan(2)
iter_1 = (a[0] - h * dLx2W(a[0][0], a[0][1])) * p
a = np.append(a, [iter_1], axis=0)
iter_2 = (a[1] - h * 0) * p
a = np.append(a, [iter_2], axis=0)

print(a[2])