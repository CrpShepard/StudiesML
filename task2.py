import numpy as np
import matplotlib.pyplot as plt

a = [-5.0, 5.0]
b = [-5.0, 5.0]
h = 0.1

def f(x1, x2):
    return x1**2 + x2**2

def df(x1, x2):
    df_x1 = 2 * x1
    df_x2 = 2 * x2
    return df_x1, df_x2

def gs():
    n = 1
    nmin = 1
    miny = f(a[0], b[0])

    z = np.array([]) # z = f(x1, x2) => f(x, y)
    x = np.array([])
    y = np.array([])
    for i in np.arange(a[0], a[1], h):
        for j in np.arange(b[0], b[1], h):
            if miny > f(i, j):
                miny = f(i, j)
                nmin = n

            df_x1, df_x2 = df(i, j)
            x1 = i - h * df_x1
            x2 = j - h * df_x2
            print("f(x):", f(i, j), "x1:", x1, "x2:", x2, "n:", n, "df_x1", df_x1, "df_x2", df_x2)
            n += 1

            z = np.append(z, f(i, j))
            x = np.append(x, x1)
            y = np.append(y, x2)

    print("miny:", miny, "at n:", nmin)

    fig = plt.figure()
    ax = plt.axes(projection ='3d')
 
    ax.plot3D(x, y, z, 'green')

    plt.show()

gs()