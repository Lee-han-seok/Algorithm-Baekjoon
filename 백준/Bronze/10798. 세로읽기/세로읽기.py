tmp = [['' for i in range(15)] for i in range(5)]
# 입력받기
for i in range(5) :
    ans = input()
    for j in range(len(ans)) :
        tmp[i][j] = ans[j]

tmp_2 = [] # 최종 결과 담을 리스트
for num in range(15) :
    for i in range(5) :
        tmp_2.append(tmp[i][num])
        
print(* tmp_2, sep = '')