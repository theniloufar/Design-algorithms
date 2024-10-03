n, x = input().split(" ")
arr = [int(i) for i in input().split()]

number_of_cards = int(n) + 1
sum_target = int(n)*int(x) + 1
nums = [[[0 for i in range(int(n)+1)] for i in range(sum_target)] for _ in range(int(number_of_cards))]

for i in range(number_of_cards):
    nums[i][0][0] = 1

for card in range(1, number_of_cards):
    for sum in range(1, sum_target):
        if arr[card-1] <= sum:
            for nu in range(len(nums[card-1][sum])):
                nums[card][sum][nu] += nums[card-1][sum][nu]
            for nu in range(1, len(nums[card-1][sum - arr[card-1]])):
                if (nums[card-1][sum - arr[card-1]][nu-1] != 0) & (nu != 1):
                    nums[card][sum][nu] += (nums[card-1][sum - arr[card-1]][nu-1])
                elif (nums[card-1][sum - arr[card-1]][nu-1] != 0) & (nu == 1):
                    nums[card][sum][nu] += (nums[card-1][sum - arr[card-1]][nu-1])
        else:
            for nu in range(len(nums[card-1][sum])):
                    nums[card][sum][nu] += nums[card-1][sum][nu]

result = 0
counts = nums[int(n)]
for i in range(0, sum_target):
    for c in range(1,len(counts)):
        if (i/c) == int(x):
            result += counts[i][c]
print(result)
