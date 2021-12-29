n = int(input())
rez = 0
for i in range(1, n+1):
    m = (1 / i**2)
    rez += m
print(rez)
