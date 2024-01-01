nums = int(input())

for i in range(nums) :
    candidates = []
    for _ in range(int(input())) :
        candidates.append(int(input()))
    tmp = sorted(candidates, reverse = True)
    tmp_max_idx = candidates.index(max(tmp)) + 1
    if tmp[0] == tmp[1] :
        print('no winner')
    else :
        if max(tmp) / sum(tmp) > 0.5 :
            print(f'majority winner {tmp_max_idx}')
        else : 
            print(f'minority winner {tmp_max_idx}')