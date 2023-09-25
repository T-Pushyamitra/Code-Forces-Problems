t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))

    if (arr[0] + arr[1]) == arr[-1]:
        print("+")
    else:
        print("-")