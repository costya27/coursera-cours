n = int(input())
n1 = int(input())
s = 0
while n > n1:
    if n % 2 == 0:
        n -= 1
        print('-1')
    elif n % 2 != 0:
        n = n / 2
        print(':2')
