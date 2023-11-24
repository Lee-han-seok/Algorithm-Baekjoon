N = int(input())
A = list(map(int, input().split(' ')))
B, C = map(int, input().split(' '))
super = N

for i in range(N) :
    if A[i] > B :
        super += (A[i] - B) // C # 남은 인원수 대비 우선 몫을 더해준다
        if (A[i] - B) % C != 0 : # 나머지가 0이 아니면, 즉 C보다는 작지만 나머지가 남았을 경우에는 
            super += 1 # 1명이 더 필요하다

print(super)