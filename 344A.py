def code(*args):
    n, magnets = args

    i = 1

    groups = 0
    current_magnet = magnets[0]

    while i < n:
        if magnets[i] != current_magnet:
            current_magnet = magnets[i]
            groups += 1

        i += 1
    return groups + 1

# Solution - 2 
def code1(*args):
    n, magnets = args

    i, j = 0, 1

    group = 0

    # Find where two pointers has same value.
    while i < len(magnets) and j < len(magnets):
        if magnets[i] == magnets[j]:
            group += 1

        i += 1
        j += 1 
    
    return group + 1

if __name__ == "__main__":
    # Take inputs here
    n = int(input())

    # Input for Solution - 2
    magnets = ''
    for _ in range(n):
        magnets += input()

    # magnets = [int(input()) for _ in range(n)]
    result = code1(n, magnets)  # Pass arguments
    print(result)

