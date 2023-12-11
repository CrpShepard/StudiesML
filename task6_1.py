import numpy as np

x = np.array([
    [50, 0, 1],
    [60, 1, 2],
    [80, 1, 3],
    [100, 0, 4]
    ])

new_x = np.array([90, 1, 1])

def MinMaxScaler():
    norm_x = np.empty((0, len(x[0])), float)

    for i in range(len(x)):
        row = np.empty(0, float)
        for j in range(len(x[i])):
            a = np.min(x.T[j])
            b = np.max(x.T[j])
            xi = (x[i][j] - a) / (b - a)
            row = np.append(row, xi)
        
        norm_x = np.append(norm_x, [row], axis=0)

    new_norm_x = np.empty(0, float)
    for i in range(len(new_x)):
        a = np.min(x.T[i])
        b = np.max(x.T[i])
        xi = (new_x[i] - a) / (b - a)
        new_norm_x = np.append(new_norm_x, xi)

    print('MinMaxScaler')
    print('norm_x:', norm_x, '\n')
    print('new_norm_x:', new_norm_x)

def Zscore():
    norm_x = np.empty((0, len(x[0])), float)
    
    for i in range(len(x)):
        row = np.empty(0, float)
        for j in range(len(x[i])):
            avg_x = np.average(x.T[j])
            sx = np.std(x.T[j], ddof=1)
            xi = (x[i][j] - avg_x) / sx
            row = np.append(row, xi)
        
        norm_x = np.append(norm_x, [row], axis=0)

    new_norm_x = np.empty(0, float)
    for i in range(len(new_x)):
        avg_x = np.average(x.T[i])
        sx = np.std(x.T[i], ddof=1)
        xi = (new_x[i] - avg_x) / sx
        new_norm_x = np.append(new_norm_x, xi)

    print('Zscore')
    print('norm_x:', norm_x, '\n')
    print('new_norm_x:', new_norm_x)


#MinMaxScaler()
Zscore()
