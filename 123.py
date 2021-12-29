c = a = b = int(input())
d = e = f = g = 0
while c != 0:
    if a < b > c:
        f = e
        if g > f:
            g = f
        e = 1
        d += 1
    else:
        e += 1
    if d == 2:
        g = f
    a = b
    b = c
    c = int(input())
print(g)
