import numpy as np
import matplotlib.pyplot as plt
import math

a = np.array([[-1, -1]])
h = 0.01
B1 = 0.5
B2 = 0.5
m = np.array([[0, 0]])
u = np.array([[0, 0]])

def f(x):
    return x[0]**2 + x[1]**2

def df(x): # grad
    df_x1 = 2 * x[0]
    df_x2 = 2 * x[1]
    return df_x1, df_x2

def mt(i):
    global m
    df_x1, df_x2 = df(a[i - 1])
    m = np.append(m, np.array([B1 * m[i - 1] + (1 - B1) * np.array(df_x1, df_x2)]), axis=0)

def ut(i):
    global u
    df_x1, df_x2 = df(a[i - 1])
    u = np.append(u, np.array([B2 * u[i - 1] + (1 - B2) * np.array(df_x1**2, df_x2**2)]), axis=0)

def cm(i):
    return m[i - 1] / (1 - B1 ** i)

def cu(i):
    return u[i - 1] / (1 - B2 ** i)

def adam():
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

        mt(n)
        ut(n)
        
        x1 = a[n - 1][0] - (h / math.sqrt(cu(n)[0] + 1)) * cm(n)[0]
        x2 = a[n - 1][1] - (h / math.sqrt(cu(n)[1] + 1)) * cm(n)[1]

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

adam()