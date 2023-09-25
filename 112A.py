def code(*args):
    if len(args[0]) != len(args[1]):
        return -1

    if args[0].lower() < args[1].lower():
        return -1
    elif args[0].lower() == args[1].lower():
        return 0
    return 1




if __name__ == "__main__":
    # Take inputs here
    str1 = input()
    str2 = input()
    result = code(str1, str2)  # Pass arguments
    print(result)

