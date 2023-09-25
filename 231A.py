
def code(arr: list) -> int:
    return 1 if arr.count(1) > 1 else 0


n = int(input())
count = 0

for i in range(n):
    arr = list(map(int, input().split()))
    count += code(arr)    

print(count)