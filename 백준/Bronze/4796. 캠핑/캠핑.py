camps = []
while True :
    l, p, v = map(int, input().split())    
    if l == 0 & p == 0 & v ==0 :
        break 
    else :
        if v % p > l :
            camp = (v // p * l) + l
            camps.append(camp)
        else : 
            camp = (v // p * l) + (v%p)
            camps.append(camp)

for i in range(len(camps)) :
    print(f'Case {i+1}: {camps[i]}')