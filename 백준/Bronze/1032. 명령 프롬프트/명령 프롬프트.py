limit = int(input())
tmp_str = '' # 문자열 받기
tmp_list = [] # 빈 리스트 생성

# 문자열 입력
for i in range(limit) :
     tmp_list.append(input())

# 각 문자열의 길이만큼 반복
for j in range(len(tmp_list[0])) :
    tmp_list_2 = [] # limit = 문자열의 갯수만큼 for문을 반복하며 해당 자리 문자를 모아둔다.
    for k in range(limit) :
        tmp_list_2.append(tmp_list[k][j])   
    if len(list(set(tmp_list_2))) == 1 : # tmp_list_2에 모인 값들이 모두 동일하다면,
        tmp_str += tmp_list[0][j] # 해당 값을 tmp_str에 붙이고
    else :
        tmp_str += '?' # 모두 같지 않다면, ?를 붙인다.

print(tmp_str)