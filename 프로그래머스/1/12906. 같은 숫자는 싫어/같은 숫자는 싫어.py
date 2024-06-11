#arr = [1, 1, 3, 3, 0, 1, 1]
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)) :
        if arr[i] != arr[i-1] :
            answer.append(arr[i])
        else : pass
    return answer










# def solution(arr):
#     answer = []
#     answer.append(arr[0])
#     for i in range(len(arr)-1) :
#         if arr[i] == arr[i+1] :
#             pass
#         if arr[i] != arr[i+1] :
#             answer.append(arr[i+1])
#     return answer