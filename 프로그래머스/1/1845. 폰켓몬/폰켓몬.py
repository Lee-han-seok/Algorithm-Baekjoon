def solution(nums):
    answer = 0
    tmp_1 = len(nums) / 2
    tmp_2 = len(list(set(nums)))
    # 단순 2로 나눈 값이 고유값의 길이 이하라면 문제 없음.
    if tmp_1 <= tmp_2 :
        answer += tmp_1
    # 만약 단순 2로 나눈 값이 고유값의 길이보다 크다면, 고유값의 개수를 반환해야 함. 
    else :
        answer += tmp_2
    return answer