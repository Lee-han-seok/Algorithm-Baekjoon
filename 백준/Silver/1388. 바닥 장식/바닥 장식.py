n,m = map(int, input().split())
graph = [] 	# 2차원 리스트의 맵 정보 저장할 공간
for _ in range(n):
    graph.append(list(input()))

count = 0

# 가로 접근, 세로에 해당하는 '|'는 무시
# 바로 직전값과 다르다면, +1을 더한다. / 만약 '-'와 계속 같다면, 그냥 넘어간다.
for i in range(n) :
    tmp = ''
    for j in range(m) :
        if graph[i][j] == '-' :
            if graph[i][j] != tmp :
                count += 1
        tmp = graph[i][j]

# 세로 접근, 가로에 해당하는 '-'는 무시
# 바로 직전값과 다르다면, +1을 더한다. / 만약 '|'와 계속 같다면, 그냥 넘어간다.

for k in range(m) :
    tmp = ''
    for q in range(n) :
        if graph[q][k] == '|' :
            if graph[q][k] != tmp :
                count += 1
        tmp = graph[q][k]

print(count)