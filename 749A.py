def code(*args):
    n = args[0]

    result = []

    # For Odd number
    if (n%2 == 1):
        n //= 2
        n -= 1
        result.extend([str(n+1), '3'])
    else:
        n //= 2
        result.append('2')
    
    for _ in range(1,n):
        result.append('2')
    
    return result


if __name__ == "__main__":
    # Take inputs here
    n = int(input())
    result = code(n)  # Pass arguments
    print(len(result))
    print(" ".join(result))


