import matplotlib.pyplot as plt
import numpy as np
import random

W1 = np.array([[0.1, 0.1, 0.1], [0.1, 0.1, 0.1]]) # нейронки 1 слоя
W2 = np.array([[0.1, 0.1], [0.1, 0.1], [0.1, 0.1]]) # нейронки 2 слоя
W3 = np.array([0.1, 0.1, 0.1]) # выходной слой

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

    sum = np.dot(W2, fout)
    fout2 = np.array([f(x) for x in sum])

    sum = np.dot(W3, fout2)

    y = f(sum)
    return (y, fout, fout2)

def train():
    global W1, W2, W3

    i = random.randint(0, len(X) - 1)
    y, fout, fout2 = forward(X[i])

    err = y - d[i]
    s3 = err * df(y)

    W3[0] = W3[0] - l * s3 * fout2[0]
    W3[1] = W3[1] - l * s3 * fout2[1]
    W3[2] = W3[2] - l * s3 * fout2[2]

    s2 = s3 * W3 * df(fout2)

    W2[0, :] = W2[0, :] - l * s2[0] * f(fout[0])
    W2[1, :] = W2[1, :] - l * s2[1] * f(fout[0])
    W2[2, :] = W2[2, :] - l * s2[2] * f(fout[0])
   
    G1 = s2[0] * W2[0, 0] + s2[1] * W2[1, 0] + s2[2] * W2[2, 0]
    G2 = s2[0] * W2[0, 1] + s2[1] * W2[1, 1] + s2[2] * W2[2, 1]
    s11 = G1 * df(fout[0])
    s12 = G2 * df(fout[1])
        
    W1[0, :] = W1[0, :] - l * s11 * np.array(X[i])
    W1[1, :] = W1[1, :] - l * s12 * np.array(X[i])
    

def start():
    y1 = np.array([])
    y2 = np.array([])

    print("Before training")

    for i in range(len(X)):
        y, fout, fout2 = forward(X[i])
        y1 = np.append(y1, y)
        print(y, d[i])

    print("After training")

    for i in range(N):
        train()

    for i in range(len(X)):
        y, fout, fout2 = forward(X[i])
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