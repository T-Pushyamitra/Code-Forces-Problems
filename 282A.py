def code(expressions: list):
    output = 0
    for expression in expressions:
        if expression[0] == '+' or expression[-1] == "+":
            output += 1
        else:
            output -= 1
    return output

t = int(input())
arr = []
for i in range(t):
    arr.append(input())

print(code(arr))
