n = int(input())
m1, m2, k = n, 0, 0
while n != 0:
    if m2 <= n <= m1 and k == 1:
        m2 = n
    elif m2 <= n and m1 <= n and k == 1:
        m2 = m1
        m1 = n
    n, k = int(input()), 1
print(m2)
