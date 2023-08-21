import sys
n = int(input())  # 첫째줄 입력
times = list(map(int, sys.stdin.readline().split()))
times.sort()
result = []
for i in range(n) :
        result.append(sum(times[0:i+1]))

print(sum(result))