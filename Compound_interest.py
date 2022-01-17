p = int(input())
x = int(input())
y = int(input())
k = int(input())
z = x * 100
a = y + z
n = 1
while n <= k:
    a = a + int(a * (p / 100))
    n = n + 1
b = a // 100
c = a % 100
print(b, c)
