# Gauss Jordan
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

for i in range(n):
    if a[i, i] == 0:
        for j in range(i + 1, n):
            if a[j, i] != 0:
                a[[j, i]] = a[[i, j]]
                break

    if a[i, i] == 0:
        print("System is inconsistent !")
        sys.exit()

    if a[i, i] != 0:
        a[i] = a[i] / a[i, i]

    for j in range(n):
        if i != j:
            factor = a[j, i]
            a[j] = a[j] - factor * a[i]


print("Final Reduced Row Echelon Form:")
print(a)

print("\nSolutions:")
print(a[:, -1])
