# https://codeforces.com/problemset/problem/486/A

def code(n):

    # If Even number, return positive number
    if (n % 2 == 0):
        return n // 2
    
    # If Odd number, return negative number
    return -(n+1)//2


n = int(input())
result = code(n)
print(result)

