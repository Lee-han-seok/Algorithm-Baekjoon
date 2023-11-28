from collections import Counter

n = input()

tmp_num_1 = 0
tmp = n.count('6') + n.count('9')
if tmp % 2 == 0 :
    tmp_num_1 += tmp // 2
else : 
    tmp_num_1 += (tmp//2 + 1)

n = n.replace('9','')
n = n.replace('6','')

tmp_num_2 = 0
if Counter(n).most_common() ==  []:
    pass
else :
    tmp_num_2 = Counter(n).most_common()[0][1]

if tmp_num_1 <= tmp_num_2 :
    print(tmp_num_2)
else :
    print(tmp_num_1)
