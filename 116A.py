def code(*args):
    
    arr = args[0]
    n = args[1]
    current_passengers = 0
    max_capacity = 0

    for i in range(n):
        current_passengers += -arr[i][0] + arr[i][1]
        max_capacity = max(max_capacity, current_passengers)

    return max_capacity


if __name__ == "__main__":
    # Take inputs here
    number_of_stops = int(input())

    arr = []
    for i in range(number_of_stops):
        arr.append(list(map(int, input().split())))
    
    result = code(arr, number_of_stops)  # Pass arguments
    print(result)

