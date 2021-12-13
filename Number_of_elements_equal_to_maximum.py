# n == numbers; m == max number; i == numbers of max number;
n = int(input())
m = 0
i = 0
while n != 0:
    n = int(input())
    if n > m:
        m = n
        i = 0
    if n == m:
        i += 1
print(i)
