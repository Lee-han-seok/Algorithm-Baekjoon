a = int(input())
b = int(input())
c = int(input())

x = str(a * b * c)

tmp = [0 for i in range(10)]

for i in range(len(x)) :
    tmp[int(x[i])] += 1

print(*tmp, sep = '\n')