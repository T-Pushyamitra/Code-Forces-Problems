# https://codeforces.com/problemset/problem/158/A

def code(arr: list, k: int) -> int:
    k_val = arr[k-1]
    total_contestants = 0
    for points in arr:
        if points != 0 and points >= k_val:
            total_contestants += 1
    return total_contestants

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))[:n]
result = code(arr, k)
print(result)