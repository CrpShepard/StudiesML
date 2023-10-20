import numpy as np
import matplotlib.pyplot as plt
import math

a = np.array([[-1, -1]])
h = 0.01
G = np.array([[0, 0]])

def f(x):
    return x[0]**2 + x[1]**2

def df(x): # grad
    df_x1 = 2 * x[0]
    df_x2 = 2 * x[1]
    return df_x1, df_x2

def Gt(i):
    global G
    df_x1, df_x2 = df(a[i - 1])
    G = np.append(G, np.array([np.array(G[i - 1]) + np.array(df_x1**2, df_x2**2)]), axis=0)

def adagrad():
    global a
    n = 1
    nmin = 1
    miny = f(a[0])

    z = np.array([]) # z = f(x1, x2) => f(x, y)
    x = np.array([])
    y = np.array([])
    
    while True:
        ffx = f(a[n - 1])

        if miny > ffx:
            miny = ffx
            nmin = n

        df_x1, df_x2 = df(a[n - 1])

        Gt(n)
        
        x1 = a[n - 1][0] - (h / math.sqrt(G[n - 1][0] + 1)) * df_x1
        x2 = a[n - 1][1] - (h / math.sqrt(G[n - 1][1] + 1)) * df_x2

        a = np.append(a, np.array([[x1, x2]]), axis=0)

        ffx = f(a[n - 1])

        print("f(x):", ffx, "x1:", x1, "x2:", x2, "n:", n, "df_x1", df_x1, "df_x2", df_x2)
        
        z = np.append(z, ffx)
        x = np.append(x, x1)
        y = np.append(y, x2)

        n += 1

        if abs(df_x1) - h <= 0 and abs(df_x2) - h <= 0:
            break

    print("miny:", miny, "at n:", nmin)

    fig = plt.figure()
    ax = plt.axes(projection ='3d')
 
    ax.plot3D(x, y, z, 'green')

    plt.show()

adagrad()