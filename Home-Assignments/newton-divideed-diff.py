import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

print("Newton's Divided Difference Interpolation")
n = int(input("Enter the number of data points: "))
X = np.zeros(n)
Y = np.zeros((n, n))

print("\nEnter values for x and y:")
for i in range(n):
    X[i], Y[i, 0] = map(float, input(f"Enter x{i} and y{i} (space-separated): ").split())

# Generate divided difference table
for i in range(1, n):
    k=i
    for j in range(n - i):
        Y[j, i] = (Y[j + 1, i - 1] - Y[j, i - 1]) / (X[k] - X[j])

print("\nDivided Difference Table:")
for i in range(n):
    print(f"{X[i]:8.3f}", end=" | ")
    for j in range(n - i):
        print(f"{Y[i, j]:8.3f}", end=" | ")
    print()

# Construct the polynomial
x = sp.symbols('x')
xp = float(input("enter interpolation point xp"))
s=0
for i in range(1,n):
    product_term = 1
    for j in range(i):
        product_term *= (x - X[j])
    s = s + product_term+ Y[0][i]
p= Y[0][0]+s

nfp = sp.nsimplify(p.evalf(),rational= True,tolerance=1e-10)
fp = sp.simplify(nfp)
f= sp.lambdify(X,p,"numpy")

print("Newton's Divided Difference polymial")
print(fp)
print(f"interpolated value at x ={xp} is {f(xp):6f}")

