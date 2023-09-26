def code(*args):
    n,t,queue = args

    while t > 0:

        i = 0
        while i in range(n-1):
            if (queue[i] == 'B' and queue[i+1] == 'G'):
                queue[i], queue[i+1] = queue[i+1], queue[i]
                i += 1
            i += 1
        t -= 1
    
    return queue



if __name__ == "__main__":
    # Take inputs here
    n, t = list(map(int, input().split()))
    queue = list(input())

    result = code(n, t, queue)  # Pass arguments
    print(''.join(result))

