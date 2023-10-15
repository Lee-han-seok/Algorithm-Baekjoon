dp = int(input())

results = [0] * (dp + 1)

for i in range(2, dp + 1) :
    results[i] = results[i - 1] + 1
    if i % 2 == 0 : 
        results[i] = min( results[i // 2] + 1, results[i])
    if i % 3 == 0 :
        results[i] = min( results[i // 3] + 1, results[i])

print(results[dp])