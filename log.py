n = int(input())
if n == 1:
    print('0')
else:
    k = 1
    while k <= n:
        k = k * 2
        if k >= n:
            break
    m = 0
    p = 1
    while p != k:
        p = p * 2
        m = m + 1
    print(m)
