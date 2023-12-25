scores = []
for _ in range(8) :
    scores.append(int(input()))

scores_sorted = sorted(scores, reverse = True)

tmp = scores_sorted[0:5]

results = []

for i in range(len(tmp)) :
    results.append(scores.index(tmp[i]) +1)

print(sum(scores_sorted[0:5]))
print(*sorted(results))