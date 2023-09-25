def code(arr, n):
    for i in range(n):
        if 'C' in arr[i] or 'M' in arr[i] or 'Y' in arr[i]:
            return False
    return True




n, m = list(map(int, input().split()))
arr = []

for i in range(n):
    arr.append(input().split())

result = code(arr, n)

if result:
    print("#Black&White")
else:
    print("#Color")
