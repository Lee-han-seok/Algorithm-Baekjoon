n, m = map(int, input().split()) #2, 3

arr = [[] for i in range(n)]

for i in range(n) :
    arr[i] = list(map(int, input().split(' ')))

for _ in range(int(input())) :
    a, b, c, d = map(int, input().split(' '))
    count = 0
    for j in range(a-1, c) :
        for k in range(b-1, d) :
            count += arr[j][k]
    print(count)