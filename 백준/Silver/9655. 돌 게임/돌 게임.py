n = int(input())
rocks_list = [1,3]

results = [1001] * (n + 1)

results[0] = 0
for i in range(len(rocks_list)) :
    for j in range(rocks_list[i], n + 1) :
        if results[j - rocks_list[i]] != 1001 :
            results[j] = min(results[j], results[j - rocks_list[i]] + 1)

if results[n] % 2 == 1 :
    print('SK')
else :
    print('CY')