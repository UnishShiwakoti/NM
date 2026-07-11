# Gauss Elimintaion with partial pivoting
import sys

import numpy as np

np.set_printoptions(suppress=True, precision=4)

# step 1 : take augmented matrix input from user
n = int(input("Enter no. of elements :"))

a = []

print("Enter augmented matrix row-wise using space : ")
for i in range(n):
    row = list(map(float, input(f"Enter row {i}: ").split()))
    a.append(row)


a = np.array(a, dtype=float)

print(f"\nAugmented matrix is : \n{a}")

# step 2 : convert to upper triangular matrix
for i in range(n):
    pivot_index = np.argmax(abs(a[i:n, i])) + i

    if pivot_index != i:
        a[[pivot_index, i]] = a[[i, pivot_index]]

    if a[i, i] == 0:
        print("System is inconsistent !")
        sys.exit()

    for j in range(i + 1, n):
        factor = a[j, i] / a[i, i]
        a[j] = a[j] - factor * a[i]

print(f"\nUpper triangular matrix is :\n{a}")

# step 3 : Back-substitution
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    s = np.sum(a[i, i + 1 : n] * x[i + 1 : n])
    x[i] = (a[i, n] - s) / a[i, i]


print("Required solution : ")

for i in range(n):
    print(f"x{i} = {round(x[i],4)}")
