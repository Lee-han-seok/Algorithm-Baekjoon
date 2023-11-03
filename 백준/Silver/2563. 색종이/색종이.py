num = int(input())

empty_square = [[0 for i in range(100)] for j in range(100)]

for i in range(num):
    left, low = map(int, input().split(' '))
    for j in range(left-1, left+9) :
        for k in range(low-1, low + 9) :
            if empty_square[j][k] == 0 :
                empty_square[j][k] += 1 
            else :
                pass

sum = 0
for z in empty_square:
    for number in z:
        sum += number

print(sum)