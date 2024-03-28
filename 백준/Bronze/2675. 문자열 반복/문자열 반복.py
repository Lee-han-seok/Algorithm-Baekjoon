trials = int(input())
for i in range(trials) :
    n, words = input().split(' ')
    result = ''
    for i in words :
        result += i * int(n)
    print(result)