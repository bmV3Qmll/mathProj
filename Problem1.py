from sympy import *
import matplotlib.pyplot as plt
import numpy as np
x, y, z, t = symbols('x y z t')
a, b, c, d = symbols("a, b, c, d")
xt = t**3 - 4*t -2
yt = -2*(t**2) + 1

eq1 = factor(simplify(xt.subs(t, a) - xt.subs(t, b)))
eq2 = factor(simplify(yt.subs(t, a) - yt.subs(t, b)))

Eq1 = Eq(eq1, 0)
Eq2 = Eq(eq2, 0)

sol1 = solveset(Eq1, b)
sol2 = solveset(Eq2, b)

#print(sol1)
#print(sol2)

inters = set([])

for expr1 in sol1:
    if expr1 == a:
        continue
    for expr2 in sol2:
        if expr2 == a:
            continue
        innerSol = solveset(Eq(expr1, expr2), a)
        for p in innerSol:
            inters.add(p)

if len(inters) == 0:
    print("No intersection.")
else:
    t0 = inters.pop()
    x0 = xt.subs(t, t0)
    y0 = yt.subs(t, t0)
    print(f"Intersect at ({x0}, {y0})")
    deri = diff(yt, t) / diff(xt, t)
    slope = deri.subs(t, t0)
    tangent = slope * (x - x0) + y0
    print("The tangent at this point: y = ", tangent)

t_range = np.arange(-3, 3, 0.01)

def fx(i):
    return i**3 - 4*i - 2

def fy(i):
    return -2*(i**2) + 1

plt.plot(fx(t_range), fy(t_range))
plt.show()
