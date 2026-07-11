"""
Power method to find dominat eigen values and vector
"""

import numpy as np
import pandas as pd

n = int(input("Enter order of Square matrix : "))

a = []

print("Enter Square matrix row-wise using space : ")
for i in range(n):
    row = list(map(float, input(f"Enter row {i}: ").split()))
    a.append(row)


a = np.array(a, dtype=float)

print(f"The Square matrix is :\n{a}")

E = float(input("Enter error tolerance : "))
N = int(input("Enter max iterations : "))

x = list(map(float, input("Enter inital vector using space : ").split()))
x = np.array(x)

T = []

old_ev = 0

itr = 1

while itr <= N:
    y = np.dot(a, x)

    max_ev = np.max(np.abs(y))

    x = y / max_ev

    error = abs(max_ev - old_ev)

    T.append([itr, max_ev] + list(x) + [error])

    if error < E:
        break

    old_ev = max_ev

    itr += 1

if itr > N:
    print(f"Solution is not reached in {itr} iterations!")

table = pd.DataFrame(
    T, columns=["iterations", "EigenValue"] + [f"x{i}" for i in range(n)] + ["Error"]
)

print(table.to_string())

print(f"Dominant Eigen Value in {itr} iterations is {round(max_ev,4)}")
print(f"Corresponding Eigen Vector is :\n{x}")
