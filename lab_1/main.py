import matplotlib.pyplot as plt
import csv
from sympy import symbols, Eq, solve

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

print(solve((eq1, eq2), (a, b)))