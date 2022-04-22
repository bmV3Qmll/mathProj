from sympy import *
import matplotlib.pyplot as plt
import numpy as np

x, y, z, t = symbols('x y z t')
fx = x * exp(x)
firstDerivative = diff(fx, x)
x0 = 0.35
y0 = 0.37
xA = -0.6
expr = firstDerivative * (x - x0) + y0 - fx
xB = nsolve(expr, x, 0)

unnamed2 = fx.subs(x, xB) - fx.subs(x, xA)
deltaD = (1 + firstDerivative**2)**(1 / 2)

def trapezoidal(func, lower, upper):
    INTERVAL_NUM = 10
    sum = 0
    width = (upper - lower) / INTERVAL_NUM
    for i in range(1, INTERVAL_NUM, 1):
        xi = lower + i * width
        sum += func.subs(x, xi)
    return (width / 2) * (func.subs(x, lower) + func.subs(x, upper) + 2 * sum)

dist = trapezoidal(deltaD, xA, xB)
print("Path AB is approximately:", dist, "km")

velocity = 60
time = dist / velocity
print("Time taken:", time, "hour")

