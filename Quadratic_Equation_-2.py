import math
a = float(input())
b = float(input())
c = float(input())
d = (b**2)-(4*a*c)
if d > 0:
    x1 = (-b + math.sqrt(d) / (2 * a))
    x2 = (-b - math.sqrt(d) / (2 * a))
    if x1 > x2:
        print('2', x1, x2)
    else:
        print('2', x2, x1)
elif d == 0:
    x1 = (-b + math.sqrt(d) / (2 * a))
    print('1', x1)
elif d < 0:
    print('0')
