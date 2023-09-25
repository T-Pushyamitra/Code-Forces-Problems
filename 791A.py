def code(limak, bob):
    year = 0

    while limak <= bob:
        year += 1
        limak *= 3
        bob *= 2
    return year

limak, bob = list(map(int, input().split()))
print(code(limak=limak, bob=bob))
