def code(*args):
    flat_number = args[0]
    flats_per_floor = args[1]

    flat_number -= 2

    floor_number = 1
    
    while flat_number >= 2:
        flat_number -= flats_per_floor
        floor_number += 1

    return floor_number


if __name__ == "__main__":
    # Take inputs here
    t = int(input())
    for i in range(t):
        result = code(*list(map(int, input().split())))  # Pass arguments
        print(result)

