N, M, K, X = map(int, input().split(' '))

from collections import deque

visited = [0] * (N+1)
distance = [-1] * (N+1)
distance[X] = 0 # 시작 지점은 0으로 바꿔둔다

def bfs(graph, start, visited) :
    queue = deque([start])
    while queue: # 큐가 없을때 까지 계속 수행
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v] :
            if distance[i] == -1 : # 방문한 적 없으면
                distance[i] = distance[v] + 1
                queue.append(i)

graph =[[] for i in range(N+1)]

# 그래프 입력 받기
for _ in range(M):
   a, b =  map(int, input().split(' '))  
   graph[a].append(b)

# BFS 함수 실행
bfs(graph, X , visited)

# print(distance, visited)

# 결과를 받는 리스트
result = []
for i in range(len(distance)) :
    if distance[i] == K :
        result.append(i)

# 리스트가 비어있으면 -1 출력
if result == [] :
    print(-1)
# 값이 있다면 순서대로 출력, 인덱스 순서이기 때문에 별도 정렬은 X
else :
    for i in range(len(result)) :
        print(result[i])