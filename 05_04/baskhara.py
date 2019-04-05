from math import *

a = float(input())
b = float(input())
c = float(input())

delta = b**2 - (4 * a * c)

if delta > 0:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    print("X1: %.2f\nX2: %.2f" % (x1, x2))
elif delta == 0:
    x = (-b + sqrt(delta)) / (2*a)
    print("X: %.2f" % x)
else:
    print("Nao existe raiz real")
    