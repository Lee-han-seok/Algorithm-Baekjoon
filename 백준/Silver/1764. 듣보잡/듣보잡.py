n,m  = map(int, input().split(' '))

d = set()
b = set()

for i in range(n):
    d.add(input())

for i in range(m):
    b.add(input())

result = sorted(list(set(b) & set(d)))

print(len(result))
for i in (result) :
    print(i)