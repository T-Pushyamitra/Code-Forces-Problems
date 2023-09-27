def code(*args):
    n, arr = args
    result = 0

    for i in range(n):
        result += 1 if (arr[i][1] - arr[i][0]) >= 2 else 0

    return result



if __name__ == "__main__":
    # Take inputs here
    n = int(input())

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    result = code(n, arr[:n])  # Pass arguments
    print(result)

