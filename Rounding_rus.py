n = float(input())
n1 = int(n)
x = (n - n1) * 100
x1 = round(x)
if x1 > 5 and x1 == 5:
    n1 += 1
    print(n1)
elif x1 < 5:
    print(n1)

