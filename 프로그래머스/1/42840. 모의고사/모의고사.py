def solution(answers):
    answers = answers
    no_math_1 = [1,2,3,4,5] * 2000
    no_math_2 = [2,1,2,3,2,4,2,5] * 1250 
    no_math_3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    math_1, math_2, math_3 = 0, 0, 0

    for i in range(len(answers)) :
        if no_math_1[i] == answers[i] : math_1 += 1
        if no_math_2[i] == answers[i] : math_2 += 1
        if no_math_3[i] == answers[i] : math_3 += 1
    
    tmp = [math_1, math_2, math_3]
    
    answer = []
    
    for i in range(len(tmp)) :
        if tmp[i] == max(tmp) :
            answer.append( i+1 )

    return answer
