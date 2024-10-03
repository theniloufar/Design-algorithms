import sys
sys.set_int_max_str_digits(0)
n, m = input().split(" ")
arr = [int(i) for i in input().split()]
sevseg = {}
for i in range(len(arr)):
    if arr[i] == 1: sevseg[1] = 2
    if arr[i] == 2: sevseg[2] = 5
    if arr[i] == 3: sevseg[3] = 5
    if arr[i] == 4: sevseg[4] = 4
    if arr[i] == 5: sevseg[5] = 5
    if arr[i] == 6: sevseg[6] = 6
    if arr[i] == 7: sevseg[7] = 3
    if arr[i] == 8: sevseg[8] = 7
    if arr[i] == 9: sevseg[9] = 6

sevseg = sorted(sevseg.items(), key=lambda x:x[1])
minnimum = sevseg[0][1]
power = []
count = []
for i in range(minnimum):
    power.append(0)
    count.append(0)
for p in range(minnimum, int(n)+1):
    temp = 0
    c = 0
    for num in sevseg:
        extra = p - num[1]
        if extra < 0:
            break
        elif extra == 0:
            if temp < num[0]:
                temp = num[0]
                c = 1
        elif (extra >= minnimum) & (power[extra] != 0):
            maximum = max(power[extra]*10 + num[0], num[0]*pow(10, count[extra]) + power[extra])
            if temp < maximum:
                temp = maximum
                c = count[extra] + 1
    power.append(temp)
    count.append(c)
    
print(power[int(n)])
