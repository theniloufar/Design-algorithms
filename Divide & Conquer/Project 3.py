t = int(input())
answer = []
for i in range(t):
    n, k= input().split(" ")
    arr = [int(i) for i in input().split()]
    res = []
    target = int(k)

    def DivConq(arr):
        #print(arr)
        if len(arr) == 1:
            if (arr[0] > target) | (arr[0] < -target):
                res.append(1)
                #print(res)
            return
        leftPart = arr[ : (len(arr) // 2)]
        rightPart = arr[(len(arr) // 2) : ]
        #print(leftPart, rightPart)
        S = []
        P = []
        Tp = []
        nTp = []
        Ssum = 0
        for i in range(len(leftPart)-1, -1, -1):
            Ssum +=  leftPart[i]
            S.append(Ssum)
        
        Psum = 0
        for i in range(len(rightPart)):
            Psum +=  rightPart[i]
            P.append(Psum)
            Tp.append(target - Psum)
            nTp.append(-target - Psum)
        
        S.sort()
        Tp.sort()
        #print(S)
        #print(Tp)
        pl = 0
        pr = 0
        while (pl != len(S)) & (pr != len(Tp)):
            #print(S[pl], Tp[pr])
            if S[pl] <= Tp[pr]:
                pl += 1
            else:
                pr += 1
                increase = len(S) - pl
                #print("inc: ", increase)
                res.append(increase)
        S.sort(reverse=True)
        nTp.sort(reverse=True)
        pl = 0
        pr = 0
        while (pl != len(S)) & (pr != len(nTp)):
            #print(S[pl], nTp[pr])
            if S[pl] >= nTp[pr]:
                pl += 1
            else:
                pr += 1
                increase = len(S) - pl
                #print("inc: ", increase)
                res.append(increase)
        #print("res: ", res)
        DivConq(leftPart)
        DivConq(rightPart)
        
    DivConq(arr)
    result = 0
    for num in res:
        result += num
    answer.append(result)

for ans in answer:
    print(ans)