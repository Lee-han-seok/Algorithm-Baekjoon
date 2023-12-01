from collections import deque

# 각 노드가 연결된 정보를 표현(2차원 리스트)
n, m = map(int, input().split(' '))

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split(' '))
    graph[a].append(b) # 서로 마주하기 때문에 해당 인덱스의 리스트에 값을 추가한다.
    graph[b].append(a)

#print(graph)

def bfs(start) :
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = 1

    while queue: # 큐가 없을때 까지 계속 수행
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i] :
                visited[i] = visited[v] + 1
                queue.append(i)

result = []

for i in range(1, n+1) : 
    visited = [0] * (n+1) # 방문횟수는 친구의 수 + 1
    bfs(i)
    result.append(sum(visited))

# 가장 작은 케빈 베이컨의 수를 가지고 있는 사람의 인덱스 + 1 을 해주어 출력한다.
print(result.index(min(result)) + 1)