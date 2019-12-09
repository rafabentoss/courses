a=float(input("Valor de a:"))
b=float(input("Valor de b:"))
c=float(input("Valor de c:"))
import math

d=(b**2)-(4*a*c)

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if x1 < x2:
        print("as raízes da equação são", x1, "e", x2)
    else:
        print("as raízes da equação são", x2, "e", x1)
if d == 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    print("a raiz desta equação é", x1)
if d < 0:
    print("esta equação não possui raízes reais")
