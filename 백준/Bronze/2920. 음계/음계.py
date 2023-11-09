input = list(map(int, input().split(' ')))
ascending = 1
descending = 1

for i in range(1, len(input)) :
    if input[i] > input[i - 1]:
        descending = 0
    elif input[i] < input[i - 1]:
        ascending = 0

if ascending == 1:
    print('ascending')
elif descending == 1:
    print('descending')
else:
    print('mixed')