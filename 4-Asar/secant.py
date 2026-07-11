import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

eqn = input("Enter a function in x using numpy in Python: ")
print()

def f(x):
    try:
        y = eval(eqn)

        if np.any(np.isnan(y)) or np.any(np.isinf(y)):
            raise ValueError(
                "Function is undefined. "
                "log cannot process negative numbers or zero."
            )

        return y

    except Exception as e:
        print("Error:", e)
        exit(0)

a, b = map(float, input("Enter two initial guesses using space: ").split())
print()

fa = f(a)
fb = f(b)

if not (np.isfinite(fa) and np.isfinite(fb)):
    print("Function is undefined at one or both endpoints.")
    print("log cannot process negative numbers or zero.")
    exit(0)

elif fa * fb > 0:
    print("Root does not lie between a and b.")
    print(f"f({a}) = {fa}")
    print(f"f({b}) = {fb}")
    exit(0)
elif abs(f(a) - f(b)) < 1e-10:
    print("Value becomes Infinite change initial guess ! ")
    exit(0)

E = float(input("Enter error tolerance: "))
print()

N = int(input("Enter maximum iterations allowed: "))
print()

# Generate x values for plotting
x = np.linspace(min(a, b) - 5, max(a, b) + 5, 1000)

try:
    y_plot = eval(eqn)
    y_plot = np.where(np.isfinite(y_plot), y_plot, np.nan)
except:
    y_plot = np.full_like(x, np.nan)

itr = 1
Table = []
Mid_Point = []

while itr <= N:
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))

    fc = f(c)

    error = abs(b - a) / 2

    Mid_Point.append(c)

    Table.append([ itr, a, b, c, fa, fb, fc, error ])

    if error < E or abs(fc) < E:
        break

    else:
        a = b
        b = c
        fa = fb
        fb = fc

    if abs(f(a) - f(b)) < 1e-10:
        print("Value becomes Infinite change initial guess ! ")    
        break

    itr += 1

if itr > N:
    print(f"Solution is not reached in {N} iterations")
    print()
else:
    print(f"Approximate root in {itr} iterations is {c}")
    print()

    T = pd.DataFrame(
        Table,
        columns=[ "Iterations", "a", "b", "c", "f(a)", "f(b)", "f(c)", "Error" ])

    print(T.to_string(index=False))
    print()

    Mid_Point = np.array(Mid_Point)
    y_mid = np.zeros_like(Mid_Point)

    plt.figure(figsize=(8, 4))
    plt.plot(x, y_plot, color="red", label=eqn)
    plt.scatter(Mid_Point, y_mid, marker="x", color="blue")
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Secant Method")

    for j in range(len(Mid_Point)):
        plt.text(Mid_Point[j], 0, str(j + 1))

    plt.show()