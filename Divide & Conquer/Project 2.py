n = int(input())
arr = [int(i) for i in input().split()]

def DivConq(arr, inversions):
    """print(arr, inversions)"""
    if len(arr) < 2:
        return arr, int(inversions)
    sorted_leftright = []
    inversions_combine = 0
    pl = 0
    pr = 0
    
    leftPart, inversions_left = DivConq(arr[ : (len(arr) // 2)], inversions)
    rightPart, inversions_right = DivConq(arr[(len(arr) // 2) : ], inversions)
    """print(leftPart, inversions_left, rightPart, inversions_right)"""
    
    while (pl != len(leftPart)) & (pr != len(rightPart)):
        if leftPart[pl] <= rightPart[pr]:
            sorted_leftright.append(leftPart[pl])
            pl += 1
        else:
            sorted_leftright.append(rightPart[pr])
            pr += 1
            increase = len(leftPart) - pl
            inversions_combine += increase
    if pl == len(leftPart):
        while pr != len(rightPart):
            sorted_leftright.append(rightPart[pr])
            pr += 1
    elif pr == len(rightPart):
        while pl != len(leftPart):
            sorted_leftright.append(leftPart[pl])
            pl += 1
    
    total_inversions = inversions_combine + inversions_left + inversions_right
    """print(sorted_leftright)"""
    return sorted_leftright, total_inversions

list, result = DivConq(arr, 0)
print(result)