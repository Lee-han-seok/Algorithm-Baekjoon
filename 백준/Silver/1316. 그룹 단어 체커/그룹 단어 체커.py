num = int(input())
texts = []
for i in range(num) :
    texts.append(input())

real_final = 0

for text in texts :
    parts = list(set(text))
    final = 0
    tmp = [[] for i in range(len(parts))]
    #print(parts)

    for j in range(len(parts)) :
        for i in range(len(text)) :
            if text[i] == parts[j] :
                tmp[j].append(i)
    #print(tmp)
    for k in range(len(tmp)) :
        for s in range(len(tmp[k]) - 1):
            if tmp[k][s+1] - tmp[k][s] == 1 :
                pass
            else :
                final += 1
                break
    
    if final > 0 :
        real_final += 1

#print(real_final)

if real_final == 0 :
    print(num)
else :
    print(num - real_final)