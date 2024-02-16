import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import csv
from sympy import symbols, Eq, solve
import numpy as np
from sklearn.linear_model import LinearRegression

N = 2
x = []
y = []

filename = open('lab_1/linreg.csv', 'r')
file = csv.DictReader(filename)

with open('lab_1/linreg.csv', 'r') as source:
    for row_number, row in enumerate(source.readlines()):
        if row_number > 0 and row_number < 22:
            data = row.replace('\n', '').split('\t')
            x.append(float(data[3].replace(',', '.')))
            y.append(float(data[2].replace(',', '.')))

x_sqr = 0
xy = 0

for i in range(0, len(x)):
    x_sqr += x[i] ** 2
    xy += x[i] * y[i]

a, b = symbols('a,b')
eq1 = Eq((x_sqr * a + sum(x) * b), xy)
eq2 = Eq((sum(x) * a + 21 * b), sum(y))

params = solve((eq1, eq2), (a, b))

print(params)

y_plt = []
x_plt = []

for i in range(0, len(x)):
    y_plt.append(y[i] + 2 * N)
    x_plt.append(x[i] + 5 * N)

x_data = np.array(x_plt).reshape(-1, 1)
y_data = np.array(y_plt)

model = LinearRegression()
model.fit(x_data, y_data)

y_pred = model.predict(np.arange(120, 180).reshape(-1, 1))
x2 = np.arange(120, 180)

plt.plot(x_data, y_data, '.')
plt.plot(x2, y_pred)
#plt.ticklabel_format(style='plain', axis='x', useOffset=False)
#plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
#plt.xlabel('Year')
#plt.ylabel('y')
#plt.grid()
plt.show()