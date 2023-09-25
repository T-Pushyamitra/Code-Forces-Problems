import math

n = int(input())

m = int((math.sqrt(8*n+1) - 1)//2)

print(m)
for i in range(1, m):
    print(i, end=" ")
    n -= i

print(n)