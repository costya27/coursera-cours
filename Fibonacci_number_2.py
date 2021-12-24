n = int(input())
fibo = 0
f1 = 1
f2 = 1
i = 2
if n == 0:
    print('0')
if n == 1:
    print('1')
else:
    while fibo < n:
        fibo = f1 + f2
        f1 = f2
        f2 = fibo
        i += 1
    if fibo == n:
        print(i)
    else:
        print('-1')
