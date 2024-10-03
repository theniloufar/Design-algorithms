n = int(input())
arr = [int(i) for i in input().split()]
res = []

def DivConq(arr, maximum):
    """print(arr, maximum)"""
    if len(arr) == 0:
        return maximum + 0
    elif len(arr) == 1:
        res.append(maximum + arr[0])
        return
    else:
        left_max = max(arr[ : (len(arr) // 2)]) 
        DivConq(arr[(len(arr) // 2) : ], left_max + maximum)
        
        right_max = max(arr[(len(arr) // 2) : ])
        DivConq(arr[ : (len(arr) // 2)], right_max + maximum)
        """print(left_max, right_max, maximum)"""
        return

DivConq(arr, 0)
print(max(res))