S = input()
tmp = [-1] * 26

word = list()
for i in range(len(S)) :
    if tmp[ord(S[i]) - 97] == -1 :
        tmp[ord(S[i]) - 97] = i

print(*tmp, sep = ' ')