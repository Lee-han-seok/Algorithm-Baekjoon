from collections import deque

n = int(input())
deq = deque(list(range(1,n+1)))
drops = []

while True :
    drops.append(deq[0])
    if len(deq) == 1 :
        break
    else :
        deq.popleft()
        deq.rotate(-1)
    
for drop in drops :
    print(drop, end = ' ')