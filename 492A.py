n = int(input())
max_height = 0

while n > -1:

    max_height += 1
    n -= max_height * (max_height+1)/2

print(max_height-1)
