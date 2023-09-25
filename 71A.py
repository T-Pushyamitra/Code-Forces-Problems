# https://codeforces.com/problemset/problem/71/A

def code(long_str):
    
    if len(long_str) > 10:
        return long_str[0] + str(len(long_str) - 2) + long_str[-1]
    return long_str


testcases = int(input())

for i in range(testcases):
    result = code(input())
    print(result)