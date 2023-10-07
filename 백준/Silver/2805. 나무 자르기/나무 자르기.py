n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = 0

while (start <= end) :
    mid = (start + end) // 2
    tmp = []      
    for tree in trees :
        if tree < mid :
            tmp.append(0)
        else :
            tmp.append(tree - mid)
    if sum(tmp) < m :
        end = mid - 1
    elif sum(tmp) >= m :
        start = mid + 1
        result = mid
        
print(result)