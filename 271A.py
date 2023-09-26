def code(*args):
    year = args[0]

    while True:

        year += 1

        a,b,c,d  = year//1000, year//100 % 10, year//10 % 10, year%10

        if (a != b and a != c and a != d and b != c and b != d and c != d):
            break
    return year



if __name__ == "__main__":
    # Take inputs here
    year = int(input())
    result = code(year)  # Pass arguments
    print(result)




