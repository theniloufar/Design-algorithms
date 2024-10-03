n, m = input().split(" ")

arr = []
for i in range(1, int(n)+1):
    arr.append(i)

def DivConq(l, r, m):
    if m < 2:
        return
    elif (l + 1) >= r:
        return
    
    temp = arr[((r+l)//2)-1]
    arr[((r+l)//2)-1] = arr[((r+l)//2)]
    arr[((r+l)//2)] = temp

    m -= 2
    DivConq(l, ((r+l)//2), m)
    DivConq(((r+l)//2), r, m)

if ((int(m) % 2) == 0) | (int(m) >= 2*int(n)):
    print(-1)
else:
    m = int(m) - 1
    DivConq(0, int(n), m)
    for num in arr:
        print(num, end=" ")
    