n = int(input())
money_list = [2, 5]

results = [100001] * (n + 1)

results[0] = 0
for i in range(len(money_list)) :
    for j in range(money_list[i], n + 1) :
        if results[j - money_list[i]] != 100001 :
            results[j] = min(results[j], results[j - money_list[i]] + 1)

if results[n] == 100001 :
    print(-1)
else :
    print(results[n])  