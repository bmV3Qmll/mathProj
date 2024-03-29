from turtle import st
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

x, y, z, t = symbols('x y z t')
firstDerivative = 3*(x**2)*(2 - y)
xi = 0
yi = 3
xf = 1

# exact solution
sol = 2+exp(-x**3)
exact = sol.subs(x, 1).evalf()

# Initialize list of coordinates
xset = [xi]
yset = [yi]

def Euler(fxy, h, n, x0, y0):
    # n as number of steps and h as the "width" of each step
    for i in range(n):
        fi = fxy.subs(x, x0).subs(y, y0)
        xi = x0 + h
        yi = y0 + h * fi
        x0 = xi
        y0 = yi
        xset.append(xi)
        yset.append(yi)
    return y0

ran = float(input("Enter step size: "))
# Sanitize input if necessary
# (a)
steps = int((xf - xi) / ran)
yf = Euler(firstDerivative, ran, steps, xi, yi)
print("Approximate by Euler's method: y(1) =", yf)

# (c)
err = abs(yf - exact) / exact * 100
print(f"The corresponding error is: {err}%")

# (d)
plt.plot(xset, yset, label = "Approximation")
x_range = np.arange(0, 1, 0.01)
def extSol(i):
    return 2 + np.exp(-i**3)
plt.plot(x_range, extSol(x_range), label = "Exact Solution")
plt.legend()
plt.show()
