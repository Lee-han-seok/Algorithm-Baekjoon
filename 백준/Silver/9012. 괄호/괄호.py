n = int(input())
vpss = []
for i in range(n) : # 리스트로 받기
    vpss.append(list(input()))

for vps in vpss : # 리스트 1개씩 돌면서
    tmp = [] # 임시 리스트
    for i in vps :
        if i == '(': # 첫번째 값이 '('면
            tmp.append(i) # 임시로 리스트에 저장해둠
        elif i == ')': 
            if len(tmp) != 0: # 만약 첫번째 값 '('가 임시 리스트에 저장되어 있으면
                tmp.pop() # tmp 최신화
            else : # 만약 ')'가 첫번째 값이었다면 혹은 임시저장된 (가 없다면
                print('NO') # vps 성립안된다는 뜻
                break
    else : 
        if len(tmp) == 0 : # 최종적으로 임시 tmp가 다 비어있다면 VPS가 성립되고
            print('YES')
        else : # tmp에 뭐가 남아있으면, 괄호가 온전하지 않은것임
            print('NO')