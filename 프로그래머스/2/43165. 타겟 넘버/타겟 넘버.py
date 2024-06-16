def solution(numbers, target):
    answer = 0
    tmp = [0]
    for i in numbers :
        tmp_2 = []
        for j in tmp :
            tmp_2.append(j+i)
            tmp_2.append(j-i)
        tmp = tmp_2
    for k in range(len(tmp)) :
        if tmp[k] == target :
            answer += 1
    #answer = tmp
    return answer  