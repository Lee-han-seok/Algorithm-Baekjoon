import math
from collections import Counter
import sys

N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()

# 산술 평균
s_mean = math.floor((sum(numbers) / len(numbers)) + 0.5)
print(s_mean)

# 중앙값
mid = mid = numbers[(len(numbers) // 2)]
print(mid)

# 최빈값
counter = Counter(numbers)
counter_most = counter.most_common()

max_num = []
for i in range (len(counter_most)) :
    max_num.append(counter_most[i][1])
max_num = max(max_num)

mode_nums = []
for i in range(len(counter_most)) :
    if counter_most[i][1] == max_num :
        mode_nums.append(counter_most[i][0])

if len(mode_nums) == 1 :
    print(counter_most[0][0])
else :
    print(counter_most[1][0])

# 범위
scope = max(numbers) - min(numbers)
print(scope)