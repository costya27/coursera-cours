n = int(input())
a = 0
b = 1
i = 1
f = a + b
while i != n:
    f = a + b
    a = b
    b = f
    i += 1
print(f)
