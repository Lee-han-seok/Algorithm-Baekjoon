game_area = int(input())
game_list = []
for _ in range(game_area):
    game_list.append(list(map(int,input().split(' '))))
visited = [[False] * game_area for _ in range(game_area)]

def dfs(x,y):
    if x >= game_area or y >= game_area:
        return False
    game = game_list[x][y]
    if game == -1:
        print('HaruHaru')
        exit(0)

    if not visited[x][y]:
        visited[x][y] = 1
        dfs(x + game, y)
        dfs(x, y + game)

dfs(0, 0)
print('Hing')