# https://codeforces.com/problemset/problem/281/A

def code(str):

    # Return string, If the first letter is upper case
    if str[0].isupper():
        return str
    
    # Transform the first letter to upper and return the string
    return str[0].upper() + str[1:]




input_str = input()
result = code(input_str)
print(result)