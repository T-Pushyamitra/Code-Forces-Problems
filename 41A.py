def code(*args):
    
    n = len(args[0])
    m = len(args[1])

    if n != m:
        return "NO"
    
    i = 0
    while i < len(args[0]):
        if args[0][i] != args[1][n - i - 1]:
            return "NO"
        i += 1
    return "YES"


if __name__ == "__main__":
    # Take inputs here
    str1 = input()
    str2 = input()
    result = code(str1, str2)  # Pass arguments
    print(result)

