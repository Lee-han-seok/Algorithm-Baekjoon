import math
import sys
N = int(input())

if N == 0 :
    print(0)
else :
    vote = []
    for n in range(N):
        vote.append(int(sys.stdin.readline()))
    cut = int(math.floor((len(vote)*0.3) / 2 + 0.5))
    vote.sort()
    result = vote[cut:len(vote)-cut]
    print(math.floor((sum(result) / len(result)) + 0.5))