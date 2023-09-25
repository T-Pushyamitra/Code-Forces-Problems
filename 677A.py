def code(*args):
    arr = args[-1]

    result = 0
    for i in arr:
        if i  <= args[1]:
            result += 1
        else:
            result += 2
    return result

if __name__ == "__main__":
    # Take inputs here
    n, h = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    result = code(n, h, arr)  # Pass arguments
    print(result)

