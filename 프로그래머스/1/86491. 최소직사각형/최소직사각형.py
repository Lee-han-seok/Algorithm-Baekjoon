def solution(sizes):
    answer = 0
    h = []
    l = []
    for i in range(len(sizes)) :
        h.append(max(sizes[i]))
        l.append(min(sizes[i]))
    answer = max(h) * max(l)    
    return answer