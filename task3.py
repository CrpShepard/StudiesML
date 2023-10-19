import matplotlib.pyplot as plt
import numpy as np
import random

W1 = np.array([[0.1, 0.1, 0.1], [0.1, 0.1, 0.1]]) # нейронки 1 слоя
W2 = np.array([[0.1, 0.1], [0.1, 0.1], [0.1, 0.1]]) # нейронка 2 слоя

X = [[-1, -1, -1],
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
    return 2 / (1 + np.exp(-x)) - 1

def df(x):
    return (1 / 2) * (1 + f(x)) * (1 - f(x))

def forward(x):
    sum = np.dot(W1, x)
    fout = np.array([f(x) for x in sum])

    #return f(W2[0] * f(W1[0][0] * x[0] + W1[0][1] * x[1] + W1[0][2] * x[2]) + W2[1] * f(W1[1][0] * x[0] + W1[1][1] * x[1] + W1[1][2] * x[2]))

    sum = np.dot(W2, fout)
    y = f(sum)[0]
    return (y, fout)

def train():
    global W1, W2

    i = random.randint(0, len(X) - 1)
    y, fout = forward(X[i])

    err = y - d[i]
    s = err * df(y)

    #W2[0] = W2[0] - l * s * fout[0]
    #W2[1] = W2[1] - l * s * fout[1]

    W2[0][0] = W2[0][0] - l * s * fout[0]
    W2[0][1] = W2[0][1] - l * s * fout[1]
    W2[1][0] = W2[1][0] - l * s * fout[0]
    W2[1][1] = W2[1][1] - l * s * fout[1]
    W2[2][0] = W2[2][0] - l * s * fout[0]
    W2[2][1] = W2[2][1] - l * s * fout[1]

    sigm = W2 * s * df(fout)[0]
    #print("sigm", sigm)

    W1[0, :] = W1[0, :] - l * np.array(X[i]) * sigm[0][0]
    W1[1, :] = W1[1, :] - l * np.array(X[i]) * sigm[0][0]
    #W1[0][0] = W1[0][0] - l * np.array(X[i]) * sigm[0][0]
    #W1[0][1] = W1[0][1] - l * np.array(X[i]) * sigm[0][1]
    #W1[0][2] = W1[0][2] - l * np.array(X[i]) * sigm[1][0]
    #W1[1][0] = W1[1][0] - l * np.array(X[i]) * sigm[1][1]
    #W1[1][1] = W1[1][1] - l * np.array(X[i]) * sigm[2][0]
    #W1[1][2] = W1[1][2] - l * np.array(X[i]) * sigm[2][1]


def start():
    y1 = np.array([])
    y2 = np.array([])

    print("Before training")

    for i in range(len(X)):
        y, fout = forward(X[i])
        y1 = np.append(y1, y)
        print(y, d[i])

    print("After training")

    for i in range(N):
        train()

    for i in range(len(X)):
        y, fout = forward(X[i])
        y2 = np.append(y2, y)
        print(y, d[i])

    figure, axis = plt.subplots(1, 2)

    print("y1", y1)
    print("y2", y2)

    axis[0].plot(np.arange(-4, 4, 1), y1)
    axis[0].set_xticks(np.arange(-4, 4, 1))
    axis[0].grid(True)
    axis[0].set_title("Before")

    axis[1].plot(np.arange(-4, 4, 1), y2)
    axis[1].set_xticks(np.arange(-4, 4, 1))
    axis[1].grid(True)
    axis[1].set_title("After")

    plt.show()

start()