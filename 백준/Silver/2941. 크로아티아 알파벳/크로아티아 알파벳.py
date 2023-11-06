ca = ['c=', 'c-','d-','lj','nj','s=','z=']

sum_3 = 0
sum_2 = 0

input = input()

# 3개일 경우 처리
for i in range (len(input)-2) :
    if input[i:i+3] == 'dz=' :
        sum_3 += 1
    else :
        continue

# 2개일 경우 처리
for i in range (len(input) - 1) :
    if input[i:i+2] in ca :
        sum_2 += 1
    else :
        continue

print(len(input) - sum_3 - sum_2)