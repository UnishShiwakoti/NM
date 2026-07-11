print("LU Decomposition Method of Solving system of linear equations ")

import sys

import numpy as np

n = int(input("Enter number of variables : "))

a = []
for i in range(n):
    row = list(map(float, input(f"Enter row {i} : ").split()))

    a.append(row)

a = np.array(a)

print(f"The augmented matrix is : \n{a}")

L = np.zeros((n, n))  # n * n zero matrix
U = np.zeros((n, n))  # n * n zero matrix

for i in range(n):
    for j in range(n):
        if i == 0:
            U[i][j] = a[i][j]

        if i == j:
            L[i][j] = 1

        if i != j and i < j:
            L[i][j] = 0
        if i != j and i > j:
            U[i][j] = 0
        if j == 0 and i >= 1:
            L[i][j] = a[i][j] / U[j][j]

        s = 0
        for k in range(j):
            if i >= 1 and j >= 1 and i <= j:
                s = s + L[i][k] * U[k][j]

        if i >= 1 and j >= 1 and i <= j:
            U[i][j] = a[i][j] - s

        S = 0
        for t in range(j):
            if i >= 1 and j >= 1 and i > j:
                S = S + L[i][t] * U[t][j]

        if i >= 1 and j >= 1 and i > j:
            L[i][j] = (a[i][j] - S) / U[j][j]


print("The upper triangular matrix is U :")
print(f"{U}")

print("The lower triangular matrix is L :")
print(f"{L}")


B = a[:, -1]

# 2. Forward substitution to solve LY = B
Y = np.zeros(n)
for i in range(n):
    sum_L = 0
    for j in range(i):
        sum_L += L[i][j] * Y[j]
    Y[i] = B[i] - sum_L

print("\nThe intermediate vector Y is:")
print(Y)

# 3. Backward substitution to solve UX = Y
X = np.zeros(n)
for i in range(n - 1, -1, -1):
    sum_U = 0
    for j in range(i + 1, n):
        sum_U += U[i][j] * X[j]
    X[i] = (Y[i] - sum_U) / U[i][i]

print("\nThe solution vector X is:")
print(X)
