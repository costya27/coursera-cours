n = int(input())
i = 0
sc = 0
p = n
while n != 0:
    n = int(input())
    if n > p:
        i = i + 1
    elif n <= p:
        i = i
    p = n
    if i == n:
        sc += 1
print(sc)
