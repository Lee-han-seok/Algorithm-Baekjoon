n, m = map(int, input().split(' ')) # N : 스크린 수, M : 바구니 크기
tmp_list = [] # 떨어지는 위치 받아두기
for _ in range(int(input())) :
    tmp_list.append(int(input()))

bucket = m - 1 # 바구니의 크기는 m-1로 해야한다. (바구니 크기 1 : 자기 자신의 위치만, 바구니 크기 2 : 좌우 한칸씩)
left = 1 # 좌측은 1부터 시작해야한다. (처음 바구니는 왼쪽 M칸을 차지하고 있다 => 1부터 M칸을 차지하고 있다.)
right = left + bucket # 우측 위치는 좌측 + bucket의 크기다 
result = 0

for i in tmp_list :
    # 바구니 안에 사과가 떨어지면 움직일 필요 없음
    if left <= i <= right :
        continue
    # 바구니 좌측으로 떨어지면, left - i 만큼 이동        
    elif i < left :
        result += (left - i) # left - i 만큼 이동
        left = i # left는 사과 떨어진 위치로 초기화
        right = i + bucket # right는 사과 떨어진 위치 + bucket 크기
    # 바구니 우측으로 떨어지면, 좌측과 동일한 모습       
    elif i > right :
        result += i - right
        left = i - bucket
        right = i

print(result)