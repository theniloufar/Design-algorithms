n = int(input())
bags = [int(i) for i in input().split()]
matrix = [[0]*int(n) for _ in range(int(n))]
p = 0
round = 1
row = 0
col = 1
h = 2
while (round < n):
    while(row <= n - h):  
         cost = []
         sum = 0
         for i in range(row, col+1):
            sum += int(bags[i])
         for k in range(row, col):
            cost.append(matrix[row][k] + matrix[k+1][col])
         res = (min(cost))  + sum
         matrix[row][col] = res
         row = row + 1
         col = col + 1
    row = 0  
    col = 1
    p += 1
    col += p
    h = h+1
    round = round + 1
print(matrix[0][n-1])    