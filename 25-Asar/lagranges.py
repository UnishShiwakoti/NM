import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

X = list(map(float, input("Enter all x values using space : ").split()))
Y = list(map(float, input("Enter all y values using space : ").split()))
if len(X) != len(Y):
    print("Mismatched data points")
    exit(0)
n = len(X)
print("Data points are :")
print("X", end="\t")
for i in range(n - 1):
    print(f"{X[i]}", end="\t")
print("Y", end="\t")
for i in range(n - 1):
    print(f"{Y[i]}", end="\t")
print("\n\n")
x = sp.symbols("x")
lp = 0
for i in range(n):
    bp = 1
    for j in range(n):
        if j != i:
            bp = bp * (x - X[j]) / (X[i] - X[j])
    lp = lp + Y[i] * bp
lag_poly = sp.nsimplify(lp.evalf(), rational=True, tolerance=1e-10)
lag_poly1 = sp.simplify(lag_poly)
print(f"Lagrange Polynomial :\n {lag_poly1}")

lag_poly2 = sp.lambdify(x, lag_poly1, "numpy")
xp = float(input("Enter x-value to interpolate : "))
int_value = lag_poly2(xp)
print(f"Interpolated value at {xp} = {round(int_value, 4)}")
w = np.linspace(min(X) - 5, max(X) + 5, 1000)
plt.plot(w, lag_poly2(w), label="Lagrange Curve")
plt.scatter(X, Y, label="Data Points", color="g")
plt.scatter(xp, lag_poly2(xp), label="interpolated value", color="orange")
plt.grid(True)
plt.legend()
plt.axhline(0, color="red")
plt.axvline(0, color="red")
plt.savefig("myplot.png")
plt.show()
