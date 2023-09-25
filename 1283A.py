# https://codeforces.com/problemset/problem/1283/A

def code(hour, minutes):
    
    # Get the remaning hours for the New year
    remaning_hour = 23 - hour

    # Get the current hour covered minutes
    remaning_minutes = 60 - minutes

    # Add total minutes by converting hours into minutes and add remaning minutes
    return (remaning_hour * 60) + remaning_minutes



# Number of testcase
testcases = int(input())

for i in range(testcases):

    # Hour and minutes inputs 
    hh, mm = list(map(int, input().split()))

    result = code(hh, mm) 

    print(result)


