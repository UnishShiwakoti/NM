import numpy as np
import matplotlib.pyplot as plt
print("To fit a second degree curve y=a+bx+cx^2 to the given data")
X=list(map(float,input("Enter all x values using space:").split()))
Y=list(map(float,input("Enter all y values using space:").split()))
X=np.array(X)
Y=np.array(Y)
if len(X)!=len(Y):
    print("Number of X data and Y data must be equal")
    exit(0)
n = len(X)

print("The mismatch points are:")
A=[[n,sum(X),sum(X**2)],
   [sum(X),sum(X**2),sum(X**3)],
   [sum(X**2),sum(X**3),sum(X**4)]
  ]
B=[[sum(Y)],[sum(X*Y)],[sum(X**2*Y)]]
A=np.array(A)
B=np.array(B)
coeff=np.linalg.solve(A,B)
print(f"coefficent matrix of normal equation:\n{A}")
print(f"column vector of normal equation:\n{B}")
a,b,c=coeff[0],coeff[1],coeff[2]
print(f"curve of best fit:\ny={np.round(a,4)}+{np.round(b,4)}x+{np.round(c,4)}x^2")
x=np.linspace(min(X)-5,max(X)+5,1000)
y=a+b*x+c*x**2
plt.plot(x,y,label='curve of best fit')
plt.scatter(X,Y,label='data points')
plt.grid(True)
plt.axhline(0,color ="red")
plt.axvline(0,color='red')
plt.legend()
plt.show()