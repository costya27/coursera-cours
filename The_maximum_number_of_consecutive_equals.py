n = int(input())
i = 0
m = 0
while n != 0:
    n = int(input())
    if n > m:
        m = n
        i = 0
    elif n == m:
        i += 1


