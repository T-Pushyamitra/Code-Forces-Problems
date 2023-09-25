
def code(n: int, s: str) -> str:
    name = 'Timur'

    if n != len(name):
        return False

    if 'T' not in s:
        return False
    
    return sorted(name) == sorted(s)





t = int(input())

for i in range(t):
    str_len = int(input())
    string = input()
    result = code(str_len, string)
    if result:
        print("YES")
    else:
        print("NO")
