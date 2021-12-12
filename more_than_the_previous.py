n = int(input())
i = 0
p = n
while n != 0:
    n = int(input())
    if n > p:
        i = i + 1
    elif n <= p:
        i = i
    p = n
print(i)
