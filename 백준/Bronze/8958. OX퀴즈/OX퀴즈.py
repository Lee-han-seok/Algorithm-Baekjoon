n = int(input())

for _ in range(n):
    ox = list(input())
    score = 0  
    tmp_score = 0
    for ox in ox:
        if ox == 'O':
            score += 1 
            tmp_score += score
        else:
            score = 0
            
    print(tmp_score)