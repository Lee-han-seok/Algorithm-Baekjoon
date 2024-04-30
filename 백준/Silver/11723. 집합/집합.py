import sys

s = set()    
n = int(input())

for i in range(n) :
    ans = sys.stdin.readline().strip().split()

    if len(ans) == 1 :
        if ans[0] == 'all' :
            s = set([i for i in range(1,21)])
        else :
            s = set()
        continue

    prompt, num = ans[0], int(ans[1])
    if prompt == 'add' :
        s.add(num)
    elif prompt == 'remove' :
        s.discard(num) # remove
    elif prompt == 'check' :
        if num in s :
            print(1)
        else : print(0)
    else :
        if num in s :
            s.discard(num)
        else :
            s.add(num)