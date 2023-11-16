num_list, changes = map(int, input().split(' '))

nums = list(range(1, num_list+1))


for i in range(changes) :
    a,b = map(int, input().split(' '))
    if a == b :
        pass
    else :
        c, d = nums[a-1], nums[b-1]
        nums[a-1] = d
        nums[b-1] = c

for i in range(len(nums)) :
    print(nums[i])