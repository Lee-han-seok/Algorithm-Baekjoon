h, n = map(int, input().split(' '))
a = []
for i in range(h) :
    a.append(input())

tmp = sorted(a)
#print(tmp)
print(tmp[n-1])