from collections import deque

N, K = map(int, input().split(' '))

que = deque(list(range(1, N+1))) # 큐로 문제 풀이

tmp_list = []
while que :
    que.rotate(-K + 1) 
    tmp_list.append(str(que.popleft()))

print("<",', '.join(tmp_list),">", sep = '')