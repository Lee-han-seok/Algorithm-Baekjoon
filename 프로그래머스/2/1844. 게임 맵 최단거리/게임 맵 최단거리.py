from collections import deque

def solution(maps) :
    answer = 0    
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    def bfs(x, y) :
        que = deque()
        que.append((x, y))
    
        while que :
            x, y = que.popleft()
            
            for i in range(4) :
                nx, ny = x + dx[i], y + dy[i]
                
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) :
                    continue
                if maps[nx][ny] == 0 : continue
                if maps[nx][ny] == 1 :
                    maps[nx][ny] = maps[x][y] + 1
                    que.append((nx, ny))
        return maps[len(maps)-1][len(maps[0])-1]
    answer = bfs(0,0)
    
    if answer == 1 : return  -1
    else : return answer




















# from collections import deque
# def solution(maps):
#     answer = 0    
#     # 상하좌우
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
    
#     def bfs(x, y) :
#         que = deque()
#         que.append((x, y))
        
#         # que에 값이 없을 때 까지
#         while que :
#             x, y = que.popleft()
            
#             # 그 자리에서 상하좌우 확인
#             for i in range(4) :
#                 nx = x + dx[i]
#                 ny = y + dy[i]
                
#                 # 맵을 벗어나면 무시해야 함
#                 if nx < 0 or nx >= len(maps) or ny >= len(maps[0]) or ny < 0 : continue
#                 # 벽이어도 무시해야함
#                 if maps[nx][ny] == 0 : continue
                
#                 # 처음 지나가는 길이면 1을 더해주고 nx ny를 갱신해줌
#                 if maps[nx][ny] == 1 :
#                     maps[nx][ny] = maps[x][y] + 1
#                     que.append((nx, ny))
                    
#         return maps[len(maps) - 1][len(maps[0]) - 1]
#     answer = bfs(0,0)    
    
    
#     if answer == 1 :
#         return -1
#     else : return answer