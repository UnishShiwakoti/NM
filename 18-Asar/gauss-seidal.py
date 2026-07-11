"""
Gauss Seidal technique of solving system of linear equations
"""

import sys
import numpy as np
import pandas as pd

np.set_printoptions(suppress=True, precision=4)

n = int(input("Enter no. of elements : "))

a = []

print("Enter augmented matrix row-wise using space : ")
for i in range(n):
    row = list(map(float, input(f"Enter row {i}: ").split()))
    a.append(row)


a = np.array(a, dtype=float)

print(f"The augmented matrix is :\n{a}")

E = float(input("Enter error tolerance : "))
N = int(input("Enter max iterations : "))

x = list(map(float, input("Enter inital value using space : ").split()))

itr = 1
iteration_table = []

for i in range(n):
    pivot_index = np.argmax(abs(a[i:n, i])) + i

    if pivot_index != i:
        a[[i, pivot_index]] = a[[pivot_index, i]]

    if a[i, i] == 0:
        print("System is inconsistent !")
        sys.exit()

print(f"Pivoted System : \n{a}")

while itr <= N:
    x_old = np.copy(x)
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s = s + a[i, j] * x[j]

        x[i] = (a[i, -1] - s) / a[i, i]

    error = abs(x - x_old)

    iteration_table.append([itr] + list(x) + list(error))

    if np.all(error < E):
        break

    itr += 1

if itr > N:
    print(f"Solution is not reached in {itr} iterations!")

else:
    table = pd.DataFrame(
        iteration_table,
        columns=["Iteration"]
        + [f"x{i}" for i in range(n)]
        + [f"Error{i}" for i in range(n)],
    )

    print(table.to_string())

    print(f"Approx solution in {itr} iteration : ")
    for i in range(n):
        print(f"x{i} = {round(x[i],4)}")
# Program End
