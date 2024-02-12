import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import csv
from sympy import symbols, Eq, solve

x = []
y = []
year = []

filename = open('lab_1/linreg.csv', 'r')
file = csv.DictReader(filename)

with open('lab_1/linreg.csv', 'r') as source:
    for row_number, row in enumerate(source.readlines()):
        if row_number > 0 and row_number < 22:
            data = row.replace('\n', '').split('\t')
            x.append(float(data[3].replace(',', '.')))
            y.append(float(data[2].replace(',', '.')))
            year.append(int(data[1]))

x_sqr = 0
xy = 0

for i in range(0, len(x)):
    x_sqr += x[i] ** 2
    xy += x[i] * y[i]

a, b = symbols('a,b')
eq1 = Eq((x_sqr * a + sum(x) * b), xy)
eq2 = Eq((sum(x) * a + 21 * b), sum(y))

params = solve((eq1, eq2), (a, b))

y_plt = []

for i in range(0, len(x)):
    y_plt.append(params[a] * x[i] - params[b])

print(year, y_plt)
plt.plot(year, y_plt, 'ro')
plt.plot(year, y_plt)
plt.ticklabel_format(style='plain', axis='x', useOffset=False)
plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
plt.xlabel('Year')
plt.ylabel('y')
plt.grid()
plt.show()