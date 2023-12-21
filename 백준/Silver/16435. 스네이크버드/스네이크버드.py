n, l = map(int, input().split(' '))
height = list(map(int, input().split(' ')))

height.sort() # 오름차순으로 정렬

snake = l
for i in range(n) :
    if snake >= height[i] : # 만약 snakebird가 과일의 높이 이상의 크기라면
        snake += 1 # +1 
    else :
        break # 그렇지 않다면 더이상 성장할 수 없기 때문에 break

print(snake)