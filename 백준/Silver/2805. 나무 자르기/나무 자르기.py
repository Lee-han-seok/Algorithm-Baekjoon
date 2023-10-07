n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0 # 시작값
end = max(trees) # 0과 최댓값의 절반인 값부터 탐색하도록 함
result = 0 # 최종 결과

while (start <= end) :
    mid = (start + end) // 2
    tmp = []      
    for tree in trees :
        if tree < mid :
            tmp.append(0)
        else :
            tmp.append(tree - mid)
    if sum(tmp) < m : # 만약 잘린 나무의 합이 부족하다면, 높이를 낮춰야 함.
        end = mid - 1
    elif sum(tmp) >= m : # 만약 잘린 나무의 합이 부족하지 않다면, 높이를 높여보는 시도를 할 수 있음.
        start = mid + 1
        result = mid # 만약 잘린 나무의 합이 조건과 정확히 일치한다면, 조건문은 반복되다가 끝날 것임.
        
print(result)
