def solution(n, lost, reserve) :
    remove_set = []
    lost.sort()
    reserve.sort()
    for i in range(len(lost)) :
        for j in range(len(reserve)) :
            if lost[i] == reserve[j] : # 분실한 사람이 여벌 가져온 사람이면
                remove_set.append(reserve[j]) # reserve에서 해당 값 제외해야함
            else : pass
    final_lost = [i for i in lost if i not in remove_set]
    final_reserve = [i for i in reserve if i not in remove_set] # 실제 reserve
    final_lost.sort()
    final_reserve.sort()

    # lost와 final_reserve를 비교하면서 체육시간에 나오지 못할(체육복 못빌리는)인원 계산
    no_football = 0
    for i in range(len(final_lost)) :
        if final_lost[i]-1 in final_reserve:# 만약 여벌옷 가진 사람이 안가져온 사람 번호 -1이면
            final_reserve.remove(final_lost[i] -1) # 현재 final_reserve에서 해당 사람을 빼줘야함 (이미 빌려줬으니까)
            continue
        elif final_lost[i]+1 in final_reserve: # 만약 여벌옷 가진 사람이 안가져온 사람 번호 +1이면
            final_reserve.remove(final_lost[i] +1)# 현재 final_reserve에서 해당 사람을 빼줘야함 (이미 빌려줬으니까)
            continue
        else : 
            no_football += 1
    answer = n - no_football
    return answer  