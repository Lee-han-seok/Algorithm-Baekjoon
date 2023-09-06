from collections import deque
import sys

n = int(input())
vpss = []
for i in range(n) :
    vpss.append(list(input()))

for vps in vpss :
    tmp = deque([])
    vps = deque(vps)
    for i in vps :
        if i == '(':
            tmp.append(i)
        elif i == ')':
            if tmp:
                tmp.pop()           
            else :
                print('NO')
                break
    else :
        if len(tmp) == 0 :
            print('YES')
        else :
            print('NO')