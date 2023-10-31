credits = []
scores = []
for i in range(20) :
    name, credit, score = input().split(' ')
    if score == 'P' :
        continue
    else :
        credits.append(float(credit))
        if score == 'A+' :
            scores.append(4.5)
        elif score == 'A0' :
            scores.append(4.0)
        elif score == 'B+' :
            scores.append(3.5)
        elif score == 'B0' :
            scores.append(3.0)
        elif score == 'C+' :
            scores.append(2.5)
        elif score == 'C0' :
            scores.append(2.0)
        elif score == 'D+' :
            scores.append(1.5)
        elif score == 'D0' :
            scores.append(1.0)
        else :
            scores.append(0.0)

results = []

for i in range(len(credits)) :
    results.append(credits[i] * float(scores[i]))

print(round(sum(results) / sum(credits),5))