n, k = input().split(" ")
arr = [int(i) for i in input().split()]

minimum = min(arr)    
state = []
chocolate = 0
while(chocolate <= int(k)):
    state.append(2)
    if (chocolate >= minimum):
        for num in arr:
            opponent_chocolate = chocolate - int(num)
            if (opponent_chocolate >= 0):
                if(state[opponent_chocolate] == 2):
                    state[int(chocolate)] = 1
    chocolate += 1

chocolate -= 1
if state[chocolate] == 1:
    print("First")
else:
    print("Second")
