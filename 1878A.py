def code(*args):
    for i in range(args[0]):
        if args[-1][i] == args[1]:
            return "YES"
    
    return "NO"



if __name__ == "__main__":
    # Take inputs here
    t = int(input())

    for i in range(t):
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))[:n]
        result = code(n, k, arr)  # Pass arguments
        print(result)

