import numpy as np
import sympy as sp
from sympy import symbols, lambdify, nsimplify, simplify

num = int(input("Enter the number of data points: "))
x_data = np.zeros(num)
y = np.zeros((num, num))

print("Enter the data points (x and y values):")
for i in range(num):
    x_data[i], y[i][0] = map(float, input(f"({i + 1}): ").split())

for order in range(1, num):
    for i in range(num - order):
        y[i][order] = (y[i + 1][order - 1] - y[i][order - 1]) / (
            x_data[i + order] - x_data[i]
        )

print("Forward Difference Table:")
for i in range(num):
    row = [f"{y[i][j]:.6g}" for j in range(num - i)]
    print(f"x[{i}] = {x_data[i]:.6g}: ", "\t".join(row))

x = symbols("x")
xp = float(input("Enter the interpolation point xp: "))

poly = y[0][0]
for order in range(1, num):
    term = y[0][order]
    for j in range(order):
        term *= x - x_data[j]
    poly += term

poly = simplify(nsimplify(poly, rational=True, tolerance=1e-10))
f = lambdify(x, poly, "numpy")

print("Newton interpolation polynomial:", poly) 
print(f"Value of the polynomial at x = {xp}: {f(xp):.6f}")