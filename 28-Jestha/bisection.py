import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


eqn = input("Enter a function in x using numpy in Python: ")
print()
def f(x):
    try:
        return eval(eqn)
    except (SyntaxError,NameError,RuntimeError):
        print("Invalid Syntax ! ")
        exit(0)
a, b = map(float,input("Enter two inital guesses using space : ").split())
print()

x = np.linspace(a-5,b+5,1000)

if f(a) * f(b)>0:
    print()
    exit(0)
E = float(input("Enter error Tolerance : "))
print()
N = int(input("Enter maximum itearations Allowed :"))
print()

itr = 1

Table = []

Mid_Point = []


while(itr<=N):
    c = (a+b)/2
    error= abs(a-b)
    Mid_Point.append(c)
    Table.append([itr,a,b,c,f(round(a,4)),f(round(b,4)),f(round(c,4)),error])
    if error <E:
        break
    elif f(a) * f(c) > 0:
        a  = c
    else:
        b = c
    itr += 1

if itr > N:
    print(f"Solution is not reached in {N} itreations")
    print()
else:
    print(f"Approx root in {itr} iterations is {c}")
    print()
    T = pd.DataFrame(Table,columns=['Iterations','a','b','c','f(a)','f(b)','f(c)','Error'])
    print(T.to_string(index=False))
    print()

    Mid_Point = np.array(Mid_Point)
    y = np.zeros_like(Mid_Point)
    
    plt.figure(figsize=(8,4))
    plt.plot(x,f(x),label=r'$e^x+sin(x)-9$',color='red')
    plt.scatter(Mid_Point,y,marker='x')
    plt.axhline(0) # x axis
    plt.axvline(0) # y axis
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.xlabel('x')
    plt.xlabel('y')

    for j in range(len(Mid_Point)):
        plt.text(Mid_Point[j],0,str(j+1))

    plt.show()

