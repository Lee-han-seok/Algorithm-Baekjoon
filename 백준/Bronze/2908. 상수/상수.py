a, b = input().split(' ')#'734', '893'

reverse_a = ''
for i in range(len(a)-1, -1, -1) :
    reverse_a += a[i]

reverse_b = ''
for i in range(len(b)-1, -1, -1) :
    reverse_b += b[i]

print(max(int(reverse_b), int(reverse_a)))