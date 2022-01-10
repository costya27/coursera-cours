p = float(input())
x = int(input())
y = int(input())
k = int(input())
y2 = str('0.' + str(y))
y3 = float(y2)
n = x + y3
sum1 = ((n * p) / 100) + n
print(int(sum1), int(sum1 * 100 % 100))
