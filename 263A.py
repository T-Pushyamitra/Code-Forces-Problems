def code(matrix):
    current_position = (0, 0)
    for i in range(len(matrix)):
        if 1 in matrix[i]:
            current_position = (i, matrix[i].index(1))
    
    return abs(current_position[0] - 2) + abs(current_position[-1] - 2)




matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

result = code(matrix)
print(result)
