input_list = list(input().split(' '))
new_list = [[] for i in range(len(input_list))]

for i in range(len(input_list)) :
    for j in range(len(input_list[i])) :
        # 만약, 입력값이 알파벳이라면
        if input_list[i][j].upper() != input_list[i][j].lower() :
            # 소문자라면
            if input_list[i][j].islower() :
                new_list[i] += chr(97+(ord(input_list[i][j])+13-97)%26)
            # 대문자라면
            elif input_list[i][j].isupper() :
                 new_list[i] += chr(65+(ord(input_list[i][j])+13-65)%26)
        # 알파벳이 아닌 모든 경우는 그대로 출력
        else :
            new_list[i] += input_list[i][j]

print(' '.join([''.join(i) for i in new_list]))