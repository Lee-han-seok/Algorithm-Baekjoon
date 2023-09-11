#import sys
#input = sys.stdin.readline
num = int(input())
pairs = int(input())

# 각 정점들의 인접한 정점을 모아놓을 비어있는 2차원 배열을 생성
graph = [[] for _ in range(num+1)]

# m개의 그래프 정보를 입력받아 현재 비어있는 인접 리스트에 저장
for _ in range(pairs):
    left, right = map(int, input().split())	
	# 해당 문제는 양방향 그래프이므로 두 점 모두 각각의 인접 리스트에 서로를 추가
    graph[left].append(right)
    graph[right].append(left)

visited = [False] * (num+1)

#print(graph)

def dfs(graph, v, visited) :
    #현재 노드를 방문 처리
    visited[v] = True
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(sum(visited)-1)