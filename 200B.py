def code(*args):
    arr, n = args

    result = float(sum(arr)/n) 

    return "{:.12f}".format(result) 




if __name__ == "__main__":
    # Take inputs here
    n = int(input())
    arr = list(map(int, input().split()))
    result = code(arr, n)  # Pass arguments
    print(result)

