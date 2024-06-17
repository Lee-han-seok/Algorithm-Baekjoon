n, m = map(int, input().split(' '))
array_1 = [[] for i in range(n)]
for i in range(n) :
    array_1[i] = input().split(' ')

m, k = map(int, input().split(' '))
array_2 = [[] for i in range(m)]
for i in range(m) :
    array_2[i] = input().split(' ')

# 결과 행렬을 초기화
final_list = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):  # array_1의 행
    for j in range(k):  # array_2의 열
        for l in range(m):  # array_1의 열, array_2의 행
            final_list[i][j] += int(array_1[i][l]) * int(array_2[l][j])

# final_list를 반환
for i in final_list :
    print(*i)