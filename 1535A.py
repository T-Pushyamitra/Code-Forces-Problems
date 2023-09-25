
def code(arr: list, n: int) -> bool:

    first_win = max(arr[:2])
    second_win = max(arr[2:])

    if first_win < min(arr[2:]) or second_win < min(arr[:2]):
        return False

    return True    


t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    n = len(arr)
    result = code(arr, n)
    
    if result:
        print("YES")
    else:
        print("NO")
