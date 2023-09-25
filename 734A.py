def code(*args):
    
    a_total_wins = 0
    d_total_wins = 0
    for i in range(args[1]):
        if args[0][i] == 'A':
            a_total_wins += 1
        else:
            d_total_wins += 1
    
    winner = a_total_wins - d_total_wins

    if winner < 0:
        return "Danik"
    elif winner == 0:
        return "Friendship"
    else:
        return "Anton"




if __name__ == "__main__":
    # Take inputs here
    n = int(input())
    score_list = input()

    result = code(score_list, n)  # Pass arguments
    print(result)

