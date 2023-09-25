n, t = list(map(int, input().split()))

while t:

    if n%10 == 0:
        n //= 10
    elif n%10 > 0:
        n -= 1
    
    t -= 1

print(n)