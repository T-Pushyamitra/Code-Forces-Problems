def code(*args):
    arr, n = args
    for i in range(n):

        if arr[i] > 0:
            return "HARD"
    
    return "EASY"

if __name__ == "__main__":
    # Take inputs here
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    result = code(arr, n)  # Pass arguments
    print(result)

