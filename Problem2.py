from sympy import *
import matplotlib.pyplot as plt
import numpy as np

x, y, z, t = symbols('x y z t')
fx = x * exp(x)                 # car's position
firstDerivative = diff(fx, x)   # slope 
x0 = 0.35                       # statue's x coordinate
y0 = 0.37                       # statue's y coordinate
xA = -0.6                       # initial position of car
expr = firstDerivative * (x - x0) + y0 - fx     # tangent line equation

xB = nsolve(expr, x, 0)         # car's x coordinate at point B

deltaDistance = (1 + firstDerivative**2)**(1 / 2)  


def trapezoidal(func, lower, upper):
    INTERVAL_NUM = 1000                     # the more the merrier
    sum = 0
    width = (upper - lower) / INTERVAL_NUM  
    for i in range(1, INTERVAL_NUM, 1):
        xi = lower + i * width
        sum += func.subs(x, xi)
    return (width / 2) * (func.subs(x, lower) + func.subs(x, upper) + 2 * sum)

dist = trapezoidal(deltaD, xA, xB)              # approximate the integral
print("Path AB is approximately:", dist, "km")

velocity = 60                       # in km/h
time = dist / velocity
print("Time taken:", time, "hour")

