def solution(nums):
    sosu = []
    nums_set = []
    length = len(nums)
    
    for i in range(0, length-2) :
        for j in range(i+1, length-1) :
            for k in range(j+1, length) :
                nums_set.append(nums[i] + nums[j] + nums[k])
    
    #nums_set = list(set(nums_set))            

    for i in range(len(nums_set)) :
        is_sosu = True
        for t in range(2, nums_set[i]) :
            if nums_set[i] % t == 0 :
                is_sosu = False
                break
        if is_sosu:
            sosu.append(nums_set[i])

    answer = len(sosu)     

    return answer