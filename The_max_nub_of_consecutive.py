a = int(input())
pr1 = a
pv = 0
m = 0
while a != 0:
    if pr1 == a:
        pv += 1
        if m < pv:
            m = pv
    if pr1 != a:
        pr1 = a
        pv = 1
    a = int(input())
print(m)
